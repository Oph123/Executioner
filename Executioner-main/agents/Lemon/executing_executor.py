#Esti Pollak 208694869
import os
import sys

from pddlsim.executors.executor import Executor
import json

import exploration
import planner
from apply_action import ApplyAction
from deterministic_executer import DeterministicExecuter
from generate_pddl_file import generate_domain_without_pro, generate_problem, generate_problem_without_reveal, \
    add_predicates_to_state
from random_executer import RandomExecuter
from utils import get_reveal_files_name, get_deterministic_files_name


class ExecutingExecutor(Executor):

    def __init__(self):
        super(ExecutingExecutor, self).__init__()


    def initialize(self, services):
        self.services = services
        self.solution_type = self.solution_type()
        if self.solution_type=='run_planer':
            self.steps = planner.make_plan(self.services.parser.domain_path,self.services.parser.problem_path)
            if len(self.steps)>0 and type(self.steps[0]) is dict:
                self.steps = [action['name'] for action in self.steps]

        if self.solution_type=='create_file_and_run_planer':
            problem_file = generate_problem_without_reveal(self.services.parser.problem_path,self.inf)
            self.steps = planner.make_plan(self.services.parser.domain_path,problem_file)
            if len(self.steps)>0 and type(self.steps[0]) is dict:
                self.steps = [action['name'] for action in self.steps]
            self.solution_type = 'run_planer'

        if self.solution_type=='run_random':
            self.randomExecuter = RandomExecuter(self.services)

        if self.solution_type=='create_file_and_run_policy':
            files_name = get_deterministic_files_name(self.services.parser.domain_name,
                                                      self.services.parser.problem_name,
                                                      self.services.parser.goals[0].parts)
            apply_action = ApplyAction(self.services)
            add_predicates_to_state(self.services.perception.state,self.inf)
            self.deterministicExecuter = DeterministicExecuter(self.services, apply_action, files_name)

        if self.solution_type == 'run_policy':
            files_name = get_deterministic_files_name(self.services.parser.domain_name,
                                                      self.services.parser.problem_name,
                                                      self.services.parser.goals[0].parts)
            apply_action = ApplyAction(self.services)
            self.deterministicExecuter = DeterministicExecuter(self.services,apply_action,files_name)

    def solution_type(self):
        is_deterministic = False
        is_revealable = False
        is_reveal_learned = False
        if len(self.services.parser.revealable_predicates) > 0:
            is_revealable = True
            reveal, reveal_inf = get_reveal_files_name(self.services.parser.domain_name,self.services.parser.problem_name)
            is_reveal_learned, self.inf = exploration.is_learned(reveal_inf)

        for action in self.services.parser.actions.values():
            if hasattr(action, "prob_list"):
                is_deterministic = True
                break

        if not is_deterministic:
            if not is_revealable:
                return 'run_planer'
            else:
                if is_reveal_learned:
                    return 'create_file_and_run_planer'
                else:
                    return 'run_random'
        else:#deterministic world
            if is_revealable:#deterministic world and reveal env
                if is_reveal_learned:
                    return 'create_file_and_run_policy'
                else:
                    return 'run_random'
            else:#only deterministic world
                return 'run_policy'



    def next_action(self):
        if self.services.goal_tracking.reached_all_goals():
            return None
        if self.solution_type == 'run_planer':
            return self.steps.pop(0).lower()
        if self.solution_type=='run_random':
            return self.randomExecuter.next_action()
        if self.solution_type == 'run_policy':
            return self.deterministicExecuter.next_action()
        if self.solution_type=='create_file_and_run_policy':
            add_predicates_to_state(self.services.perception.state,self.inf)
            return self.deterministicExecuter.next_action()








