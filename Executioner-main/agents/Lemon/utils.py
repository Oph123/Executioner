import os
import pickle

import pddlsim

import static


def get_reveal_files_name(domain_name,problem_name):
    env_name, _ = problem_name.split('-')

    file_name = domain_name + '_' + env_name + '.pddl'

    return [static.reveal_dir + '/' + file_name, static.reveal_information_dir + '/' + file_name]


def get_deterministic_files_name(domain_name,problem_name,parser_goals):
    env_name, _ = problem_name.split('-')

    goals = ''
    for goal in parser_goals:
        if isinstance(goal, pddlsim.parser_independent.Disjunction):
            goals += 'or('
            for g in goal.parts:
                if isinstance(g, pddlsim.parser_independent.Not):
                    goals += ' not ' + g.content.predicate + str(g.content.args)
                else:
                    goals += g.predicate + str(g.args)
            goals += ')'
        elif isinstance(goal, pddlsim.parser_independent.Literal):
            goals += goal.predicate + str(goal.args)
        elif isinstance(goal, pddlsim.parser_independent.Not):
            goals += ' not ' + goal.content.predicate + str(goal.content.args)

    if os.path.exists('policy_mapping.pickle'):
        with open('policy_mapping.pickle', 'rb') as f:
            i, domain_env_goal_dict = pickle.load(f)
    else:
        i, goal_list, domain_env_goal_dict = 0, [], {}

    if (domain_name, env_name, goals) in domain_env_goal_dict.keys():
        id = domain_env_goal_dict[(domain_name, env_name, goals)]
    else:
        domain_env_goal_dict[(domain_name, env_name, goals)] = i
        id = i
        i = i + 1

    with open('policy_mapping.pickle', 'wb') as f:
        pickle.dump([i, domain_env_goal_dict], f)

    state_file_name = static.state_dir + '/' + domain_name + '_' + env_name + '.pickle'
    transition_file_name = static.trantition_dir + '/' + domain_name + '_' + env_name + '.pickle'
    reward_file_name = static.reward_dir + '/' + str(id) + '.pickle'
    policy_file_name = static.policy_dir + '/' + str(id) + '.pickle'

    return [state_file_name, transition_file_name, reward_file_name, policy_file_name]
