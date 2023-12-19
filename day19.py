import re

FILE = "input.txt"

def check_rule(key, operand, value, part):
    if operand == '>':
        return int(part[key]) > int(value)
    else:
        return int(part[key]) < int(value)

def get_paths(workflow, last_rules=[]):
    if workflow == 'A' or workflow == 'R':
        return [{workflow: last_rules}]

    cur_flow = workflows.get(workflow)
    negated_rules = []
    paths = []

    for *rule, n in cur_flow[:-1]:
        paths.extend(get_paths(n, last_rules + negated_rules + [rule]))

        if rule[1] == '>':
            negated_rules.append([rule[0], '<', f"{int(rule[2])+1}"])
        elif rule[1] == '<':
            negated_rules.append([rule[0], '>', f"{int(rule[2])-1}"])

    paths.extend(get_paths(cur_flow[-1], last_rules + negated_rules))
    
    return paths

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        workflows, machine_parts = [list_.split('\n') for list_ in file.read().split('\n\n')]

        workflows = [re.findall("([a-z]+){((?>[a-z]+[<>]\d+:[a-zA-Z]+,)+)([a-zA-Z]+)}", flow)[0] for flow in workflows]
        workflows = {flow[0]: re.findall("(?>([a-z]+)([<>])(\d+):([a-zA-Z]+))", flow[1]) + [flow[2]] for flow in workflows}

        machine_parts = [{key: val for key, val in re.findall('([xmas])=(\d+)', part)} for part in machine_parts]

        accepted_parts = []

        for part in machine_parts:
            next_workflow = 'in'
            while next_workflow not in ['A', 'R']:
                start_flow = workflows.get(next_workflow)
                rules = start_flow[:-1]
                default = start_flow[-1]
                passes_rule = False
                for k, o, v, n in rules:
                    passes_rule = check_rule(k, o, v, part)
                    if passes_rule:
                        next_workflow = n
                        break
                if not passes_rule:
                    next_workflow = default
            if next_workflow == 'A':
                accepted_parts.append(part)
        
        print("Part 1:", sum(sum(map(int, part.values())) for part in accepted_parts))

    # part two 
    with open(FILE) as file:
        workflows, _ = [list_.split('\n') for list_ in file.read().split('\n\n')]

        workflows = [re.findall("([a-z]+){((?>[a-z]+[<>]\d+:[a-zA-Z]+,)+)([a-zA-Z]+)}", flow)[0] for flow in workflows]
        workflows = {flow[0]: re.findall("(?>([a-z]+)([<>])(\d+):([a-zA-Z]+))", flow[1]) + [flow[2]] for flow in workflows}

        paths_to_approved = [d['A'] for d in get_paths('in') if 'A' in d]

        approved_combinations = 0
        for path in paths_to_approved:
            limits = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
            for k, o, v in path:
                if o == '<':
                    limits[k] = (limits[k][0], min(int(v), limits[k][1]) - 1)
                if o == '>':
                    limits[k] = (max(int(v), limits[k][0]) + 1, limits[k][1])
            x, m, a, s = [z - y + 1 for y, z in limits.values()]
            approved_combinations += x*m*a*s

        print("Part 2:", approved_combinations)