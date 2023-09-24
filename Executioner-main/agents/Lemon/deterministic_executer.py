import os
import pickle
import random

import planner
import static
from generate_pddl_file import generate_domain_without_pro, generate_problem


class DeterministicExecuter():
    def __init__(self, services, apply_action, files_name):
        self.services = services
        self.apply_action = apply_action
        self.without_learning = False
        self.prev_state = None
        self.prev_action = None
        self.count = 0
        self.count_policy = 0
        self.policy_prev_state = None

        self.new_domain_file_name = static.domain_dir + '/' + self.services.parser.domain_name + '.pddl'
        if not os.path.exists(self.new_domain_file_name):
            generate_domain_without_pro(self.services.parser.domain_path, self.new_domain_file_name,
                                        self.services.parser.actions.values())
            self.without_learning = True
        if self.is_policy_exist(files_name):
            self.state_list, self.policy = self.load_files(files_name)
            self.is_up_to_date = False
        else:
            self.without_learning = True
            self.steps = self.calc_plane()

    def next_action(self):
        if self.services.goal_tracking.reached_all_goals():
            return None
        valid_actions = self.services.valid_actions.get()
        if len(valid_actions) == 0:
            return None
        # This problem has not been learned before
        if self.without_learning:
            if self.steps == None:
                self.steps = self.calc_plane()
                if self.steps == None:
                    next_action = random.choice(valid_actions)
                else:
                    next_action = str(self.steps.pop(0).lower())

            elif self.prev_state != None and self.prev_state == self.services.perception.state and self.count < 20:
                self.count += 1
                return self.prev_action
            elif self.prev_state != None and self.prev_state == self.services.perception.state and not self.count > 20:
                self.count = 0
                self.steps = self.calc_plane()
                if self.steps == None:
                    next_action = random.choice(valid_actions)
                else:
                    next_action = str(self.steps.pop(0).lower())

            elif self.prev_state != None and (len(self.steps) == 0 or self.is_unexpected_state()):
                self.steps = self.calc_plane()
                if self.steps == None:
                    next_action = random.choice(valid_actions)
                else:
                    next_action = str(self.steps.pop(0).lower())
            else:
                next_action = str(self.steps.pop(0).lower())
            self.prev_state = self.services.perception.state
            self.prev_action = next_action
            return next_action

        # this problem learned before
        else:
            state = self.services.perception.state
            state_index = self.state_to_index(state)
            if state_index in self.policy.keys():
                if self.policy_prev_state == state:
                    self.count_policy += 1
                if self.count_policy > 20:
                    self.count_policy = 0
                    return random.choice(valid_actions)
                self.is_up_to_date = False
                self.prev_state = None
                self.prev_action = None
                self.policy_prev_state = state
                return self.policy[state_index]
            else:
                if not self.is_up_to_date:
                    self.steps = self.calc_plane()
                    self.is_up_to_date = True
                if self.steps == None:
                    self.steps = self.calc_plane()
                    if self.steps == None:
                        next_action = random.choice(valid_actions)
                    else:
                        next_action = str(self.steps.pop(0).lower())


                elif self.prev_state != None and self.prev_state == self.services.perception.state and self.count < 20:
                    self.count += 1
                    return self.prev_action
                elif self.prev_state != None and self.prev_state == self.services.perception.state and not self.count > 20:
                    self.count = 0
                    self.steps = self.calc_plane()
                    if self.steps == None:
                        next_action = random.choice(valid_actions)
                    else:
                        next_action = str(self.steps.pop(0).lower())

                elif self.prev_state != None and self.prev_state == state:
                    return self.prev_action
                elif self.prev_state != None and (len(self.steps) == 0 or self.is_unexpected_state()):
                    self.steps = self.calc_plane()
                    if self.steps == None:
                        next_action = random.choice(valid_actions)
                    else:
                        next_action = str(self.steps.pop(0).lower())
                else:
                    next_action = str(self.steps.pop(0).lower())
                self.prev_state = self.services.perception.state
                self.prev_action = next_action
                return next_action

    def load_files(self, files_name):
        with open(files_name[0], 'rb') as f:
            s = pickle.load(f)
        with open(files_name[3], 'rb') as f:
            p = pickle.load(f)
        return s, p

    def is_policy_exist(self, files_name):
        return os.path.exists(files_name[3])

    def calc_plane(self):
        problem_file_name = generate_problem(self.services.pddl.problem_path, self.services.perception.state)
        try:
            steps = planner.make_plan(self.new_domain_file_name, problem_file_name)
            if type(steps[0]) is dict:
                steps = [action['name'] for action in steps]
            return steps
        except Exception:
            return None

    def state_to_index(self, state):
        try:
            return self.state_list.index(state)
        except Exception:
            return -1

    def is_unexpected_state(self):
        state = self.services.perception.state

        t = self.apply_action.apply_prob_action_to_state(self.prev_action, self.prev_state)
        prop_list = [prob[0] for prob in t]
        index = prop_list.index(max(prop_list))
        return t[index][1] != state
