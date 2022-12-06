import numpy as np

def runPart1(initial_stacks, instructions):
    stacks = [[i for i in row] for row in initial_stacks]

    for order in instructions:
        order_array = order.split()
        move_num = int(order_array[1])
        # subtracting one because orders are 1 based
        from_i = int(order_array[3]) - 1
        to_i = int(order_array[5]) - 1 

        for _ in range(move_num):
            stacks[to_i].append(stacks[from_i].pop())

    print(''.join([s[-1] for s in stacks]))

def runPart2(initial_stacks, instructions):
    stacks = [[i for i in row] for row in initial_stacks]
    for order in instructions:
        order_array = order.split()
        move_num = int(order_array[1])
        # subtracting one because orders are 1 based
        from_i = int(order_array[3]) - 1
        to_i = int(order_array[5]) - 1 

        n_last_items = stacks[from_i][-move_num:]
        del stacks[from_i][-move_num:]
        stacks[to_i] += n_last_items

    print(''.join([s[-1] for s in stacks]))

if __name__ == '__main__':
    file = open('input.txt')
    starting_input, instructions = file.read().split('\n\n')
    # Time is money so i'm not going to try and parse the starting input :)

    # [T]     [D]         [L]            
    # [R]     [S] [G]     [P]         [H]
    # [G]     [H] [W]     [R] [L]     [P]
    # [W]     [G] [F] [H] [S] [M]     [L]
    # [Q]     [V] [B] [J] [H] [N] [R] [N]
    # [M] [R] [R] [P] [M] [T] [H] [Q] [C]
    # [F] [F] [Z] [H] [S] [Z] [T] [D] [S]
    # [P] [H] [P] [Q] [P] [M] [P] [F] [D]
    # 1   2   3   4   5   6   7   8   9 
    starting_input = [
        ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
        ['H', 'F', 'R'],
        ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
        ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
        ['P', 'S', 'M', 'J', 'H'],
        ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
        ['P', 'T', 'H', 'N', 'M', 'L'],
        ['F', 'D', 'Q', 'R'],
        ['D', 'S', 'C', 'N', 'L', 'P', 'H'],
    ]

    instructions = instructions.split('\n')
    runPart1(starting_input, instructions)
    runPart2(starting_input, instructions)

