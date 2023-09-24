from string import maketrans


def generate_domain_without_pro(source_file, destination_file, actions):
    chars_to_remove = '([,])\''
    chars_to_add = len(chars_to_remove) * ' '
    trans_table = maketrans(chars_to_remove, chars_to_add)

    with open(source_file, 'r') as f:
        source_file_content = f.read()
        len_file = len(source_file_content) - 1

    for action in actions:
        where_to_look = source_file_content.find(action.name)
        start_index = source_file_content.find('(probabilistic', where_to_look)
        end_index = source_file_content.find('(:', start_index, len_file)
        if end_index == -1:
            end_index = len_file

        if start_index != -1:
            old = source_file_content[start_index:end_index]

            prob_index = action.prob_list.index(max(action.prob_list))
            if action.addlists[prob_index] == []:
                prob_list = action.prob_list[:]
                prob_list[prob_index] = 0
                prob_index = action.prob_list.index(max(prob_list))

            addlists = ['(' + str(add).translate(trans_table) + ')' for add in
                        action.addlists[prob_index]]
            dellists = ['(' + str(add).translate(trans_table) + ')' for add in
                        action.dellists[prob_index]]
            if len(dellists) > 0:
                not_list = ['(not ' + deli + ')' for deli in dellists]
            else:
                not_list = ''

            new = '(and' + ' '.join(addlists) + ' '.join(not_list) + '))\n'

            if end_index == len_file:
                source_file_content = source_file_content.replace(old, new + ')')
            else:
                source_file_content = source_file_content.replace(old, new)

    with open(destination_file, 'w') as f:
        f.write(source_file_content)


def generate_problem_without_reveal(source_file, predicates):
    destination_file = 'new_problem_file.pddl'
    with open(source_file, 'r') as f:
        source_file_content = f.read()
        len_file = len(source_file_content) - 1

    start = source_file_content.find('(:reveal')
    end = source_file_content.find('(:', start)
    if end == -1:
        end = len_file
    if start != -1:
        del_lines = source_file_content[start:end]

        if end == len_file:
            source_file_content = source_file_content.replace(del_lines, ')')
        else:
            source_file_content = source_file_content.replace(del_lines, '')

    add_lines = ' '.join(['(' + p[0] + ' ' + ' '.join(p[1]) + ')\n' for p in predicates])
    where_to_add = source_file_content.find('(:init') + 6
    source_file_content = source_file_content[:where_to_add] + add_lines + source_file_content[where_to_add:]

    with open(destination_file, 'w') as f:
        f.write(source_file_content)

    return destination_file


def add_predicates_to_state(stsate, predicates):
    for p in predicates:
        stsate[p[0]].add(p[1])


def generate_problem(source_file, state):
    destination_file = 'new_problem_file.pddl'
    with open(source_file, 'r') as f:
        source_file_content = f.read()

    start_index = source_file_content.find('(:init')
    end_index = source_file_content.find('(:', start_index + 1)

    old = source_file_content[start_index:end_index]
    new = '(:init' + '\t' + '\n\t'.join(predicates_from_state(state)) + ')'
    source_file_content = source_file_content.replace(old, new)

    with open(destination_file, 'w') as f:
        f.write(source_file_content)
    return destination_file


def predicates_from_state(state):
    return [("(%s %s)" % (predicate_name, " ".join(map(str, pred)))) for predicate_name, predicate_set in
            state.iteritems() for pred in predicate_set if predicate_name != '=']
