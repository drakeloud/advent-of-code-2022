import numpy as np

def populate_totals(totals, instructions):
    working_dir = ['/']
    # Populate all directories with values from ls
    for instruction in instructions:
        cmd = instruction[0]
        if cmd.startswith('cd'):
            dir = cmd.split(' ')[-1]
            if dir == '/':
                working_dir = ['/']
            elif dir == '..':
                working_dir.pop()
            else:
                working_dir.append(dir + '/')
        elif cmd.startswith('ls'):
            for res in instruction[1:]:
                key = ''.join(working_dir)
                if res.startswith('dir'):
                    pass
                elif key in totals:
                    totals[key] += int(res.split(' ')[0])
                else:
                    totals[key] = int(res.split(' ')[0])

def resolve_directory_totals(totals):
    keys = list(totals.keys())
    while len(keys) > 0:
        keys.sort(key=lambda x: len(x.split('/')))
        temp_key = keys.pop()
        temp_key = temp_key[:-1] # Remove the trailing slash
        if temp_key.rfind('/') >= 0:
            parent_total = totals[temp_key + '/']
            temp_key = temp_key[:temp_key.rfind('/')]

            if temp_key + '/' in totals:
                totals[temp_key + '/'] += parent_total
            else:
                totals[temp_key + '/'] = parent_total
                keys.append(temp_key + '/')

def part_one(totals):
    sum_totals = 0
    for k in totals:
        if totals[k] < 100_000:
            sum_totals += totals[k]
    
    print(sum_totals)

def part_two(totals):
    current_space = 70_000_000 - totals['/']
    all_candidates = filter(lambda x: x >= 30_000_000 - current_space, totals.values())
    print(min(all_candidates))

if __name__ == '__main__':
    with open('input.txt') as file:
        file_input = file.read().split('$')
        instructions = []
        for f in file_input:
            temp = f.split('\n')
            temp[0] = temp[0].lstrip()

            if temp[-1] == '':
                del temp[-1]

            instructions.append(temp)
        
        totals = {}
        # from the $ split, the first element is not needed
        del instructions[0]
        populate_totals(totals, instructions)
        resolve_directory_totals(totals)
        part_one(totals)
        part_two(totals)
