import numpy as np

def part_one(cycles):
    notable_cycles = [20, 60, 100, 140, 180, 220]
    sum_cycles = [cycles[x - 1] * x for x in notable_cycles]

    # 16020
    print(sum(sum_cycles))

def part_two(cycles):
    screen = []
    for _ in range(6):
        screen.append(list("." * 40))

    for i in range(len(cycles)): 
        row = i // 40 
        col = i - (row * 40)
        if abs(col - cycles[i]) <= 1:
            screen[row][col] = "#"
    
    for row in screen:
        print(''.join(row))



if __name__ == '__main__':
    with open('input.txt') as file:
        file_input = file.read().split('\n')

        X = 1
        cycles = [1]
        for signal in file_input:
            if signal.startswith('noop'):
                cycles.append(X)
            else:
                addx, n = signal.split(' ')
                n = int(n)
                cycles.append(X)
                X += n
                cycles.append(X)

        part_one(cycles)
        part_two(cycles)
