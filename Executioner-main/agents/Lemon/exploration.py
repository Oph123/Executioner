import pickle
import random


class Exploration:
    def __init__(self, services, reveal_file, reveal_information_file):
        self.services = services
        self.reveal_file = reveal_file
        self.reveal_information_file = reveal_information_file
        self.state_list, self.count_dict = self.load()
        self.information_dict = self.load_information()

    def next_action(self):
        self.information_learned()
        if len(self.information_dict["unlearned"]) == 0:
            self.save()
            return None
        valid_action = self.services.valid_actions.get()
        if len(valid_action) == 0:
            self.save()
            return None
        state = self.services.perception.state
        state_index = self.state_to_index(state)
        if state_index == -1:
            self.state_list.append(state)
            state_index = len(self.state_list) - 1
            self.count_dict[state_index] = dict(zip(valid_action, [0] * len(valid_action)))

        return self.choose_and_update_action(state_index)

    def information_learned(self):
        state = self.services.perception.state
        unlearneds = self.information_dict["unlearned"][:]
        for unlearned in self.information_dict["unlearned"]:
            if unlearned[1] in state[unlearned[0]]:
                self.information_dict["learned"].append(unlearned)
                unlearneds.remove(unlearned)
        self.information_dict["unlearned"] = unlearneds

    def choose_and_update_action(self, state_index):
        min_val = min(self.count_dict[state_index].itervalues())
        min_action = [k for k, v in self.count_dict[state_index].iteritems() if v == min_val]
        choosen_action = random.choice(min_action)
        self.count_dict[state_index][choosen_action] += 1
        return choosen_action

    def load(self):
        try:
            with open(self.reveal_file, "rb") as f:
                return pickle.load(f)
        except Exception:
            return [], {}

    def load_information(self):
        """
        :return:
        """
        try:
            with open(self.reveal_information_file, "rb") as f:
                return pickle.load(f)
        except Exception:
            return {
                "learned": [],
                "unlearned": sum([reveal.effects for reveal in self.services.parser.revealable_predicates], []),
            }

    def save(self):
        if not len(self.information_dict["unlearned"]) == 0:
            with open(self.reveal_file, "wb") as f:
                pickle.dump([self.state_list, self.count_dict], f)

        with open(self.reveal_information_file, "wb") as f:
            pickle.dump(self.information_dict, f)

    def state_to_index(self, state):
        try:
            return self.state_list.index(state)
        except Exception:
            return -1


def is_learned(file):
    try:
        with open(file, "rb") as f:
            inf = pickle.load(f)
            return len(inf["unlearned"]) == 0, inf["learned"]
    except Exception:
        return False, []
