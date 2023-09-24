# Esti Pollak 208694869
import atexit
import os
import pickle
import signal

import exploration
import pddlsim
import static
from apply_action import ApplyAction
from exploration import Exploration
from generate_pddl_file import (add_predicates_to_state,
                                generate_domain_without_pro)
from pddlsim import simulator
from pddlsim.executors.executor import Executor
from Rmax import Rmax
from utils import get_deterministic_files_name, get_reveal_files_name


class LearningExecutor(Executor):
    def __init__(self):
        super(LearningExecutor, self).__init__()

    def initialize(self, services):
        self.services = services
        self.apply_action = ApplyAction(self.services)
        self.solution_type = self.solution_type()
        if self.solution_type == "simple" or self.solution_type == "all learned":
            exit(128)
        if self.solution_type == "exploration":
            self.initialize_revealable()
        if self.solution_type == "learned and rmax":
            add_predicates_to_state(self.services.perception.state, self.inf)
            self.initialize_deterministic()
        if self.solution_type == "rmax":
            self.initialize_deterministic()

    def solution_type(self):
        is_deterministic = False
        is_revealable = False
        is_learned = False
        if len(self.services.parser.revealable_predicates) > 0:
            is_revealable = True
            reveal, reveal_inf = get_reveal_files_name(
                self.services.parser.domain_name, self.services.parser.problem_name
            )
            is_learned, self.inf = exploration.is_learned(reveal_inf)

        for action in self.services.parser.actions.values():
            if hasattr(action, "prob_list"):
                is_deterministic = True
                break

        if not is_deterministic and not is_revealable:
            return "simple"
        if is_revealable and not is_learned:
            return "exploration"
        if not is_deterministic and is_revealable and is_learned:
            return "all learned"
        if is_deterministic and is_revealable and is_learned:
            return "learned and rmax"
        return "rmax"

    def initialize_revealable(self):
        reveal, reveal_inf = get_reveal_files_name(self.services.parser.domain_name, self.services.parser.problem_name)
        self.exploration = Exploration(self.services, reveal, reveal_inf)

    def initialize_deterministic(self):
        files_name = get_deterministic_files_name(
            self.services.parser.domain_name, self.services.parser.problem_name, self.services.parser.goals[0].parts
        )
        domain, problem = self.services.pddl.domain_path, self.services.pddl.problem_path
        domain_name = self.services.parser.domain_name
        new_domain_file_name = static.domain_dir + "/" + domain_name + ".pddl"
        if not os.path.exists(new_domain_file_name):
            generate_domain_without_pro(domain, new_domain_file_name, self.services.parser.actions.values())
        self.rmax = Rmax(self.apply_action, files_name, new_domain_file_name, problem, self.services)

    def next_action(self):
        if self.solution_type == "exploration":
            try:
                return self.exploration.next_action()
            except KeyboardInterrupt:
                self.handle_iterrupt_reveal()
        if self.solution_type == "rmax":
            try:
                return self.rmax.next_action()
            except KeyboardInterrupt:
                self.handle_iterrupt_rmax()
        if self.solution_type == "learned and rmax":
            add_predicates_to_state(self.services.perception.state, self.inf)
            return self.rmax.next_action()

    def handle_iterrupt_rmax(self):
        print("Gah")
        self.rmax.save_files()
        exit(0)

    def handle_iterrupt_reveal(self):
        print("Gah")
        self.exploration.save()
        exit(0)
