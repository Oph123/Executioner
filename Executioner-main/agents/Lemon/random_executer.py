import random


class RandomExecuter:
    def __init__(self, services):
        self.services = services
        self.state_list, self.count_dict = [], {}

    def next_action(self):
        if self.services.goal_tracking.reached_all_goals():
            return None
        valid_action = self.services.valid_actions.get()
        if len(valid_action) == 0:
            return None

        state = self.services.perception.state
        state_index = self.state_to_index(state)
        if state_index == -1:
            self.state_list.append(state)
            state_index = len(self.state_list) - 1
            self.count_dict[state_index] = dict(zip(valid_action, [0] * len(valid_action)))

        return self.choose_and_update_action(state_index)

    def choose_and_update_action(self, state_index):
        min_val = min(self.count_dict[state_index].itervalues())
        min_action = [k for k, v in self.count_dict[state_index].iteritems() if v == min_val]
        choosen_action = random.choice(min_action)
        self.count_dict[state_index][choosen_action] += 1
        return choosen_action

    def state_to_index(self, state):
        try:
            return self.state_list.index(state)
        except Exception:
            return -1
