import glob
import os
from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Collection

import click
import pddl
from pddl import logic
from pddl.custom_types import name
from pddl.logic import Predicate
from pddl.logic.base import And, BinaryOp, Not, Or, UnaryOp
from pddl.logic.effects import AndEffect
from pddl.logic.predicates import EqualTo
from pddl.logic.terms import Constant, Term, Variable
from pddl.parser.domain import Action, Domain, Requirements
from pddl.parser.problem import Problem

PADDING = "_"
PARAMETER_PREFIX = "p"
EQUALITY_PREDICATE = "eq"

SUPPORTED_REQUIREMENTS = {
    Requirements.STRIPS,
    Requirements.TYPING,
    Requirements.NEG_PRECONDITION,
    Requirements.DIS_PRECONDITION,
    Requirements.EQUALITY,
    Requirements.CONDITIONAL_EFFECTS,
}


def remove_empty_lines(s: str) -> str:
    """Remove empty lines from string."""
    return "\n".join(filter(str.strip, s.splitlines()))


def _sort_and_print_collection(prefix, collection: Collection, postfix, to_string: Callable = str):
    if len(collection) > 0:
        return prefix + " ".join(sorted(map(to_string, collection))) + postfix
    else:
        return ""


def _print_predicates_with_types(predicates: Collection):
    result = ""
    for p in sorted(predicates):
        if p.arity == 0:
            result += f"({p.name})"
        else:
            result += f"({p.name}"
            for t in p.terms:
                result += f" ?{t.name} - {' '.join(t.type_tags)}" if t.type_tags else f" ?{t.name}"
            result += ") "
        result += " "
    return result.strip()


def _print_objects_with_types(objects: Collection):
    result = ""
    for o in sorted(objects):
        result += f"{o.name} - {' '.join(o.type_tags)}" if o.type_tags else f"{o.name}"
        result += " "
    return result.strip()


def domain_to_string(domain: Domain) -> str:
    return (
        f"(define (domain {domain.name})"
        f"(:predicates {' '.join(str(predicate) for predicate in domain.predicates)})"
        f"{' '.join(str(action) for action in domain.actions)})"
    )


def problem_to_string(problem: Problem) -> str:
    return (
        f"(define (problem {problem.name})"
        f"(:domain {problem.domain_name})"
        f"(:objects {' '.join(str(problem_object) for problem_object in problem.objects)})"
        f"(:init {' '.join(str(predicate) for predicate in problem.init)})"
        f"(:goal {str(problem.goal)}))"
    )


def make_domain_mutatable(domain: Domain):
    domain._predicates = set(domain._predicates)
    domain._constants = set(domain._constants)
    domain._requirements = set(domain._requirements)
    domain._actions = set(domain._actions)


def uniquify(id: name, max_length: int) -> name:
    return id.ljust(max_length + 1, PADDING)


def is_constant(term: Term) -> bool:
    return type(term) is Constant


def get_max_predicate_length(domain: Domain) -> int:
    return max([len(predicate.name) for predicate in domain.predicates] + [0])


def get_max_type_length(domain: Domain) -> int:
    return max([len(object_type) for object_type in domain.types] + [0])


def get_max_parameter_length(action: Action) -> int:
    return max([len(parameter.name) for parameter in action.parameters] + [0])


def remove_negation_from_precondition(
    formula: Not | Or | And | UnaryOp | BinaryOp | Predicate, register_negated_predicate: Callable[[name, int], name]
) -> Or | And | UnaryOp | BinaryOp | Predicate:
    match formula:
        case Not(argument=And(operands=formulas)):
            return Or(
                *[Not(remove_negation_from_precondition(formula, register_negated_predicate)) for formula in formulas]
            )
        case Not(argument=Or(operands=formulas)):
            return And(
                *[Not(remove_negation_from_precondition(formula, register_negated_predicate)) for formula in formulas]
            )
        case Not(argument=Predicate(name=predicate, terms=terms)):
            return Predicate(register_negated_predicate(predicate, len(terms)), *terms)
        case UnaryOp(argument=subformula):
            return type(formula)(remove_negation_from_precondition(subformula, register_negated_predicate))
        case BinaryOp(operands=formulas):
            return type(formula)(
                *[remove_negation_from_precondition(formula, register_negated_predicate) for formula in formulas]
            )
        case _:
            return formula


def add_negated_predicates_to_effect(
    formula: Not | UnaryOp | AndEffect | Predicate, negated_predicate_map: dict[name, name]
) -> AndEffect | UnaryOp | Predicate:
    match formula:
        case Not(argument=Predicate(name=predicate, terms=terms)):
            if predicate in negated_predicate_map:
                return AndEffect(formula, Predicate(negated_predicate_map[predicate][0], *terms))
            else:
                return formula
        case UnaryOp(argument=subformula):
            return type(formula)(add_negated_predicates_to_effect(subformula, negated_predicate_map))
        case AndEffect(operands=formulas):
            formulas = [add_negated_predicates_to_effect(formula, negated_predicate_map) for formula in formulas]
            elements = []

            for formula in formulas:
                match formula:
                    case AndEffect(operands=formulas):
                        for formula in formulas:
                            elements.append(formula)
                    case _:
                        elements.append(formula)

            return AndEffect(*elements)
        case Predicate(name=predicate, terms=terms):
            if predicate in negated_predicate_map:
                return AndEffect(formula, ~Predicate(negated_predicate_map[predicate][0], *terms))
            else:
                return formula


def remove_domain_negative_preconditions_requirement(domain: Domain) -> dict[name, name]:
    negated_predicate_map = {}
    max_predicate_length = get_max_predicate_length(domain)

    def register_negated_predicate(predicate: name, arity: int) -> name:
        if predicate in negated_predicate_map:
            return negated_predicate_map[predicate][0]
        else:
            negated_predicate_name = uniquify(predicate, max_predicate_length)

            negated_predicate_map[predicate] = (negated_predicate_name, arity)
            domain.predicates.add(
                Predicate(negated_predicate_name, *[Variable(f"{PARAMETER_PREFIX}{value}") for value in range(arity)])
            )

            return negated_predicate_name

    # We must do two passes here: one to generate all the needed
    # negated predicates and one to properly use them in effects.
    # Combining the passes will cause some effects to not actually
    # use the negated predicates other actions rely on.
    for action in domain.actions:
        action._precondition = remove_negation_from_precondition(action.precondition, register_negated_predicate)

    for action in domain.actions:
        action._effect = add_negated_predicates_to_effect(action.effect, negated_predicate_map)

    domain._requirements -= {Requirements.NEG_PRECONDITION}

    return negated_predicate_map


def remove_equality_from_formula(
    formula: UnaryOp | BinaryOp | EqualTo | Predicate, equality_predicate: name
) -> UnaryOp | BinaryOp | Predicate:
    match formula:
        case UnaryOp(argument=subformula):
            return type(formula)(remove_equality_from_formula(subformula, equality_predicate))
        case BinaryOp(operands=formulas):
            return type(formula)(*[remove_equality_from_formula(formula, equality_predicate) for formula in formulas])
        case EqualTo(left=left, right=right):
            return Predicate(equality_predicate, left, right)
        case _:
            return formula


# TODO: Consider not registing the equality predicate later on if only the negation of it is used
def remove_domain_equality_requirement(domain: Domain) -> name | None:
    if Requirements.EQUALITY in domain.requirements:
        equality_predicate_name = uniquify(EQUALITY_PREDICATE, get_max_predicate_length(domain))
        domain.predicates.add(Predicate(equality_predicate_name, Variable("a"), Variable("b")))

        for action in domain.actions:
            action._precondition = remove_equality_from_formula(action.precondition, equality_predicate_name)

        domain._requirements.discard(Requirements.EQUALITY)

        return equality_predicate_name


def remove_formula_constants(
    formula: UnaryOp | BinaryOp | AndEffect | Predicate, register_constant: Callable[[name], name]
):
    match formula:
        case UnaryOp(argument=formula):
            remove_formula_constants(formula, register_constant)
        case BinaryOp(operands=formulas):
            for formula in formulas:
                remove_formula_constants(formula, register_constant)
        case AndEffect(operands=formulas):
            for formula in formulas:
                remove_formula_constants(formula, register_constant)
        case Predicate(terms=terms):
            formula._terms = [register_constant(term) if is_constant(term) else term for term in terms]


def remove_domain_constants(domain: Domain) -> dict[name, name]:
    max_type_length = get_max_type_length(domain)
    constant_type_map = {}

    for action in domain.actions:
        max_parameter_length = get_max_parameter_length(action)
        constant_map = {}

        def register_constant(constant: Constant) -> name:
            nonlocal constant_map
            nonlocal constant_type_map

            if constant.name in constant_map:
                return constant_map[constant.name]
            else:
                if constant.name not in constant_type_map:
                    constant_type = uniquify(constant.name, max_type_length)
                    domain._types._types[constant_type] = "object"
                    domain._types._all_types.add(constant_type)

                    constant_type_map[constant.name] = constant_type
                else:
                    constant_type = constant_type_map[constant.name]

                constant_parameter = Variable(
                    uniquify(constant.name, max_parameter_length),
                    {
                        constant_type,
                    },
                )
                action._parameters += (constant_parameter,)
                constant_map[constant.name] = constant_parameter

                return constant_parameter

        remove_formula_constants(action.precondition, register_constant)
        remove_formula_constants(action.effect, register_constant)

    domain._constants = set()

    return constant_type_map


def remove_predicate_types(domain: Domain):
    for predicate in domain.predicates:
        for term in predicate.terms:
            term._type_tags = set()


def untype_actions(domain: Domain, type_predicates: dict[name, name]):
    for action in domain.actions:
        for parameter in action.parameters:
            for type_tag in parameter.type_tags:
                action._precondition &= Predicate(type_predicates[type_tag], parameter)

            parameter._type_tags = set()


def supertypes(domain: Domain, object_type: name) -> set[name]:
    types = set()

    supertype = domain.types[object_type]

    if supertype and supertype != "object":
        types.add(supertype)
        types.update(supertypes(domain, supertype))

    return types


# This returns both the type to predicate mapping and the type to supertypes mapping
def remove_domain_typing_requirement(domain: Domain) -> tuple[dict[name, name], dict[name, set[name]]]:
    max_length = get_max_predicate_length(domain)

    def type_to_predicate(object_type) -> name:
        new_name = uniquify(object_type, max_length)
        parameter = logic.variables("x")
        domain.predicates.add(Predicate(new_name, *parameter))

        return new_name

    supertype_map = {object_type: supertypes(domain, object_type) for object_type in domain.types}
    type_predicates = {object_type: type_to_predicate(object_type) for object_type in domain.types}

    domain._types._types = {}
    domain._types._all_types = set()

    remove_predicate_types(domain)
    untype_actions(domain, type_predicates)

    domain._requirements.discard(Requirements.TYPING)

    return type_predicates, supertype_map


@dataclass
class DomainMetadata:
    equality_predicate: name | None
    constant_types: dict[name, name]
    type_predicates: dict[name, name]
    supertypes: dict[name, set[name]]
    negated_predicate_map: dict[name, tuple[name, int]]


def strip_domain(domain: Domain) -> DomainMetadata:
    make_domain_mutatable(domain)

    equality_predicate = remove_domain_equality_requirement(domain)
    constants_types = remove_domain_constants(domain)
    type_predicates, supertypes = remove_domain_typing_requirement(domain)
    negated_predicate_map = remove_domain_negative_preconditions_requirement(domain)

    return DomainMetadata(equality_predicate, constants_types, type_predicates, supertypes, negated_predicate_map)


def make_problem_mutable(problem: Problem):
    problem._init = set(problem._init)
    problem._objects = set(problem._objects)


def add_constants_to_problem(problem: Problem, constant_types: dict[name, name]):
    for constant_name, constant_type in constant_types.items():
        problem.objects.add(
            Constant(
                constant_name,
                constant_type,
            )
        )


def add_equality_predicate_to_problem(problem: Problem, equality_predicate: name):
    if equality_predicate:
        for problem_object in problem.objects:
            problem.init.add(Predicate(equality_predicate, problem_object, problem_object))


def untype_problem(problem: Problem, type_predicates: dict[name, name], supertypes: dict[name, set[name]]):
    for problem_object in problem.objects:
        if problem_object.type_tag:
            types = set()

            problem.init.update(
                set(
                    Predicate(type_predicates[object_type], problem_object)
                    for object_type in supertypes[problem_object.type_tag] | {problem_object.type_tag}
                )
            )

            for object_type in types:
                problem.init.add(Predicate(type_predicates[object_type], problem_object))

            problem_object._type_tags = set()


def combinations(group: list, length) -> list[tuple]:
    if length == 0:
        return [()]
    elif len(group) == 0:
        return []
    else:
        output = []

        for item in group:
            for combination in combinations(group[1:], length - 1):
                output.append((item,) + combination)

        return output


def remove_problem_negative_preconditions(problem: Problem, negated_predicate_map: dict[name, name]):
    truths = defaultdict(lambda: [])

    for fact in problem.init:
        truths[fact.name].append(fact.terms)

    for predicate, negated_predicate_metadata in negated_predicate_map.items():
        negated_predicate, arity = negated_predicate_metadata

        for combination in combinations(list(problem.objects), arity):
            if combination not in truths[predicate]:
                problem.init.add(Predicate(negated_predicate, *combination))


def strip_problem(problem: Problem, metadata: DomainMetadata):
    make_problem_mutable(problem)

    add_constants_to_problem(problem, metadata.constant_types)
    add_equality_predicate_to_problem(problem, metadata.equality_predicate)
    untype_problem(problem, metadata.type_predicates, metadata.supertypes)
    remove_problem_negative_preconditions(problem, metadata.negated_predicate_map)


def standardise_file(file_path):
    with open(file_path, "r") as file:
        text = file.read().casefold()  # Apparently PDDL is case-insensitive

    with open(file_path, "w") as file:
        file.write(text)


def strip_group(files: list[str]):
    domain_metadata = {}
    problems = {}

    for file_path in files:
        standardise_file(file_path)

        try:
            domain = pddl.parse_domain(file_path)
        except Exception as domain_error:
            try:
                problems[file_path] = pddl.parse_problem(file_path)
            except Exception as problem_error:
                raise ExceptionGroup(
                    f"Could not parse {file_path} as either a domain or a problem",
                    [domain_error, problem_error],
                )
        else:
            if domain.requirements <= SUPPORTED_REQUIREMENTS:
                domain_metadata[domain.name] = strip_domain(domain)

                with open(file_path, "w") as file:
                    file.write(domain_to_string(domain))
            else:
                print(f"The domain at {file_path} uses unsupported requirements and so was not stripped")

    for file_path, problem in problems.items():
        if problem.domain_name in domain_metadata:
            metadata = domain_metadata[problem.domain_name]
            strip_problem(problem, metadata)

            with open(file_path, "w") as file:
                file.write(problem_to_string(problem))
        else:
            print(
                f"The problem in {file_path} uses a domain with unsupported requirement "
                "or that was unavailable and so wasn't stripped"
            )


@click.command()
@click.argument("directory", type=click.STRING)
@click.version_option("0.1.0")
def cli(directory: str):
    files = glob.glob(os.path.join(directory, "**", "*.pddl"), recursive=True)
    strip_group(files)
