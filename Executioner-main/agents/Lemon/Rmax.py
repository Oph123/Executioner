import os
import pickle
import random

import numpy as np
import planner
from generate_pddl_file import generate_problem


class Rmax:
    def __init__(self, apply_action, files_name, domain_file, problem_file, services):
        self.files_name = files_name
        self.services = services
        self.state_list, self.transition, self.is_target_exist, self.reward, self.policy = self.load_files()
        self.prev_state = None
        self.prev_action = None
        self.prev_valid_action = None
        self.path = None
        self.is_first = True
        self.domain_file = domain_file
        self.problem_file = problem_file
        self.Rmax = 1.1
        self.initial_state = self.services.parser.initial_state
        self.is_target_exist = False
        if not self.is_target_exist:
            self.calc_path()
        self.apply_action = apply_action
        self.count = 0

    def next_action(self):
        if self.services.goal_tracking.reached_all_goals():
            self.update()
            self.is_target_exist = True
            self.save_files()
            return None
        valid_actions = self.services.valid_actions.get()
        if len(valid_actions) == 0:
            self.update()
            self.save_files()
            return None

        state = self.services.perception.state
        if not self.is_first:
            self.update()
            if self.prev_state == state and self.count < 20:
                self.count += 1
                return self.prev_action
            else:
                self.count = 0
                if not self.is_target_exist:
                    if self.path == None or not self.max_prob_state() == state:
                        self.calc_path()
                    else:
                        next_action = self.get_next(state, valid_actions)
        else:
            self.is_first = False

        if not self.is_target_exist:
            if self.path == None:
                next_action = random.choice(valid_actions)
            else:
                next_action = str(self.path.pop(0).lower())
                # self.policy[self.state_to_index(state)]=next_action
        else:
            next_action = self.get_next(state, valid_actions)

        self.prev_state = state
        self.prev_action = str(next_action)
        self.prev_valid_action = valid_actions

        return next_action

    def get_next(self, state, valid_actions):
        state_index = self.state_to_index(state)
        if not state_index in self.reward.keys():
            return random.choice(valid_actions)

        rewards = list(self.reward[state_index].values())
        keys = list(self.reward[state_index].keys())
        max_reward = max(rewards)
        max_action = keys[rewards.index(max_reward)]
        if max_reward != self.Rmax:
            self.policy[state_index] = max_action
        return max_action

    def max_prob_state(self):
        state_index = self.state_to_index(self.prev_state)
        prop_list = [prob[0] for prob in self.transition[state_index][self.prev_action]]
        index = prop_list.index(max(prop_list))
        return self.transition[state_index][self.prev_action][index][1]

    def update(self):
        state_index = self.state_to_index(self.prev_state)
        if not state_index in self.transition.keys():
            self.transition[state_index] = self.calc_transition_prob(self.prev_state, self.prev_valid_action)

            reward = dict(zip(self.prev_valid_action, [self.Rmax] * len(self.prev_valid_action)))
            self.reward[state_index] = reward

        if not state_index in self.reward.keys():
            reward = dict(zip(self.prev_valid_action, [self.Rmax] * len(self.prev_valid_action)))
            self.reward[state_index] = reward

        if self.reward[state_index][self.prev_action] == self.Rmax:
            effects = self.transition[state_index][self.prev_action]
            if len(effects) == 1:
                self.reward[state_index][self.prev_action] = 1 if self.is_path_exist(effects[0][1]) else 0
            else:
                total_reward = 0
                for effect in effects:
                    reward = 1 if self.is_path_exist(effect[1]) else 0
                    total_reward += effect[0] * reward
                self.reward[state_index][self.prev_action] = total_reward
            if (
                not state_index in self.policy.keys()
                or self.reward[state_index][self.prev_action] > self.reward[state_index][self.policy[state_index]]
            ):
                self.policy[state_index] = self.prev_action

    def is_path_exist(self, state):
        new_problem_file_name = generate_problem(self.problem_file, state)
        try:
            plan_steps = planner.make_plan(self.domain_file, new_problem_file_name)
        except Exception:
            return False
        return True

    def calc_path(self):
        state = self.services.perception.state
        # get to state at least once
        problem_file_name = generate_problem(self.problem_file, state)
        try:
            self.path = planner.make_plan(self.domain_file, problem_file_name)
        except Exception:
            self.path = None
            return

        if type(self.path[0]) is dict:
            self.path = [action["name"] for action in self.path]

    def calc_transition_prob(self, state, valid_action):
        transition = dict()
        for action in valid_action:
            transition[action] = self.apply_action.apply_prob_action_to_state(action, state)
        # transition[self.prev_action] = self.apply_action.apply_prob_action_to_state(self.prev_action, state)
        return transition

    def state_to_index(self, state):
        try:
            return self.state_list.index(state)
        except Exception:
            self.state_list.append(state)
            return len(self.state_list) - 1

    def load_files(self):
        try:
            with open(self.files_name[0], "rb") as f:
                s = pickle.load(f)
        except Exception:
            s = []
        try:
            with open(self.files_name[1], "rb") as f:
                t = pickle.load(f)
        except Exception:
            t = {}
        try:
            with open(self.files_name[2], "rb") as f:
                is_target_exist, r = pickle.load(f)
        except Exception:
            is_target_exist, r = False, {}
        try:
            with open(self.files_name[3], "rb") as f:
                p = pickle.load(f)
        except Exception:
            p = {}

        return s, t, is_target_exist, r, p

    def save_files(self):
        with open(self.files_name[0], "wb") as f:
            pickle.dump(self.state_list, f)
        with open(self.files_name[1], "wb") as f:
            pickle.dump(self.transition, f)
        with open(self.files_name[2], "wb") as f:
            pickle.dump([self.is_target_exist, self.reward], f)
        with open(self.files_name[3], "wb") as f:
            pickle.dump(self.policy, f)
