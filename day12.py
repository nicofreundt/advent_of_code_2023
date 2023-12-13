FILE = "input.txt"

STATE_MEMORY = {}

def get_arrangements(cond_rec, damaged_groups, cur_cond=0, cur_group=0, cur_group_len=0):
    if (cur_cond, cur_group, cur_group_len) in STATE_MEMORY:
        return STATE_MEMORY[(cur_cond, cur_group, cur_group_len)]

    if cur_cond == len(cond_rec):
        # end of cond_rec
        if cur_group == len(damaged_groups) and cur_group_len == 0:
            # all groups done
            return 1
        elif cur_group == len(damaged_groups) - 1 and damaged_groups[cur_group] == cur_group_len:
            # all groups done, but cond_rec ends with group
            return 1
        else:
            # invalid
            return 0
    
    cur_valid_arrangements = 0
    
    for spring_state in ['.', '#']:
        if cond_rec[cur_cond] in [spring_state, '?']:
            if spring_state == '.' and cur_group_len == 0:
                # no current group
                cur_valid_arrangements += get_arrangements(cond_rec, damaged_groups, cur_cond+1, cur_group, cur_group_len)
            elif spring_state == '.' and cur_group_len > 0 and cur_group < len(damaged_groups) and damaged_groups[cur_group] == cur_group_len:
                # end of current group
                cur_valid_arrangements += get_arrangements(cond_rec, damaged_groups, cur_cond+1, cur_group+1, 0)
            elif spring_state == '#':
                # continue current group
                cur_valid_arrangements += get_arrangements(cond_rec, damaged_groups, cur_cond+1, cur_group, cur_group_len+1)
    
    STATE_MEMORY[(cur_cond, cur_group, cur_group_len)] = cur_valid_arrangements
    
    return cur_valid_arrangements

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        # condition records and damaged string groups
        # ex: list of ('???.###', (1,1,3))
        cr_dsg = [(line.strip().split()[0], tuple(map(int, line.strip().split()[1].split(',')))) for line in file.readlines()]

        valid_arrangements = 0
        
        for cr, dsg in cr_dsg:
            valid_arrangements += get_arrangements(cr, dsg)
            STATE_MEMORY.clear()
        
        print("Part 1:", valid_arrangements)

    # part two 
    with open(FILE) as file:
        # condition records and damaged string groups
        # ex: list of ('???.###', (1,1,3))
        cr_dsg = [(line.strip().split()[0], tuple(map(int, line.strip().split()[1].split(',')))) for line in file.readlines()]
        
        valid_arrangements = 0
        
        for cr, dsg in cr_dsg:
            valid_arrangements += get_arrangements('?'.join([cr]*5), dsg*5)
            STATE_MEMORY.clear()
        
        print("Part 2:", valid_arrangements)