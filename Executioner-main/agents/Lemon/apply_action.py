import pddlsim

REACH_GOAL = 'reach-goal'


class ApplyAction:
    def __init__(self, services):
        self.services = services
        self.actions = self.services.parser.actions
        self.objects = self.services.parser.objects

    def apply_prob_action_to_state(self, action_sig, state, check_preconditions=True):
        action_name, param_names = self.parse_action(action_sig)
        if action_name.lower() == REACH_GOAL:
            return state
        action = self.actions[action_name]
        params = map(self.get_object, param_names)

        param_mapping = action.get_param_mapping(params)

        if isinstance(action, pddlsim.parser_independent.Action):
            copy_state = self.services.parser.copy_state(state)
            for (predicate_name, entry) in action.to_delete(param_mapping):
                predicate_set = copy_state[predicate_name]
                if entry in predicate_set:
                    predicate_set.remove(entry)

            for (predicate_name, entry) in action.to_add(param_mapping):
                copy_state[predicate_name].add(entry)
            return [[1, copy_state]]
        else:
            assert isinstance(action, pddlsim.parser_independent.ProbabilisticAction)
            ans = []
            for index in range(len(action.prob_list)-1):
                copy_state = self.services.parser.copy_state(state)
                for (predicate_name, entry) in action.to_delete(param_mapping, index):
                    predicate_set = copy_state[predicate_name]
                    if entry in predicate_set:
                        predicate_set.remove(entry)

                for (predicate_name, entry) in action.to_add(param_mapping, index):
                    copy_state[predicate_name].add(entry)

                ans += [[action.prob_list[index], copy_state]]
            return ans

    @staticmethod
    def parse_action(action):
        action_sig = action.strip('()').lower()
        parts = action_sig.split(' ')
        action_name = parts[0]
        param_names = parts[1:]
        return action_name, param_names

    def get_object(self, name):
        """ Get a object tuple for a name """
        if name in self.objects:
            return (name, self.objects[name])


class PreconditionFalseError(Exception):
    pass


class Action(object):
    def __init__(self, name, signature, addlist, dellist, precondition):
        self.name = name
        self.signature = signature
        self.addlist = addlist
        self.dellist = dellist
        self.precondition = precondition

    def action_string(self, dictionary):
        params = " ".join([dictionary[var[0]] for var in self.signature])
        return "(" + self.name + " " + params + ")"

    @staticmethod
    def get_entry(param_mapping, predicate):
        names = [x for x in predicate]
        entry = tuple([param_mapping[name][0] for name in names])
        return entry

    def entries_from_list(self, preds, param_mapping):
        return [(pred[0], self.get_entry(param_mapping, pred[1])) for pred in preds]

    def to_delete(self, param_mapping):
        return self.entries_from_list(self.dellist, param_mapping)

    def to_add(self, param_mapping):
        return self.entries_from_list(self.addlist, param_mapping)

    def get_param_mapping(self, params):
        param_mapping = dict()
        for (name, param_type), obj in zip(self.signature, params):
            param_mapping[name] = obj
        return param_mapping


class ProbabilisticAction(object):
    def __init__(self, name, signature, addlists, dellists, precondition, prob_list):
        self.name = name
        self.signature = signature
        self.addlists = addlists
        self.dellists = dellists
        self.precondition = precondition
        self.prob_list = prob_list

    def action_string(self, dictionary):
        params = " ".join([dictionary[var[0]] for var in self.signature])
        return "(" + self.name + " " + params + ")"

    @staticmethod
    def get_entry(param_mapping, predicate):
        names = [x for x in predicate]
        entry = tuple([param_mapping[name][0] for name in names])
        return entry

    def entries_from_list(self, preds, param_mapping):
        return [(pred[0], self.get_entry(param_mapping, pred[1])) for pred in preds]

    def to_delete(self, param_mapping, effect_index):
        return self.entries_from_list(self.dellists[effect_index], param_mapping)

    def to_add(self, param_mapping, effect_index):
        return self.entries_from_list(self.addlists[effect_index], param_mapping)

    def get_param_mapping(self, params):
        param_mapping = dict()
        for (name, param_type), obj in zip(self.signature, params):
            param_mapping[name] = obj
        return param_mapping


