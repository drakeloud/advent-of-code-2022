import numpy as np

def runPart1(file_input):
    total = 0
    for pair in file_input:
        pair_1, pair_2 = pair.split(',')
        low_pair_1, high_pair_1 = pair_1.split('-')
        low_pair_2, high_pair_2 = pair_2.split('-')

        low_pair_1 = int(low_pair_1)
        low_pair_2 = int(low_pair_2)
        high_pair_1 = int(high_pair_1)
        high_pair_2 = int(high_pair_2)

        if low_pair_1 <= low_pair_2 and high_pair_1 >= high_pair_2:
            total += 1
        elif low_pair_2 <= low_pair_1 and high_pair_2 >= high_pair_1:
            total += 1

    print(total)

def runPart2(file_input):
    total = 0
    for pair in file_input:
        pair_1, pair_2 = pair.split(',')
        low_pair_1, high_pair_1 = pair_1.split('-')
        low_pair_2, high_pair_2 = pair_2.split('-')

        low_pair_1 = int(low_pair_1)
        low_pair_2 = int(low_pair_2)
        high_pair_1 = int(high_pair_1)
        high_pair_2 = int(high_pair_2)

        if low_pair_1 <= low_pair_2 and high_pair_1 >= low_pair_2:
            total += 1
        elif low_pair_2 <= low_pair_1 and high_pair_2 >= low_pair_1:
            total += 1

    print(total)

if __name__ == '__main__':
    file = open('input.txt')
    file_input = file.read().split('\n')

    runPart1(file_input)
    runPart2(file_input)

