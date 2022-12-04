import numpy as np

if __name__ == '__main__':
    file = open('Day1-input.txt')
    content = file.read().split('\n\n')
    max = 0
    top_3 = [0, 0, 0]

    for i, elf in enumerate(content):
        totals = elf.split('\n')
        totals = np.asarray(totals).astype(np.int64)
        sum_elf = np.sum(totals)

        # Problem 1A
        if sum_elf > max:
            max = sum_elf
            max_arg = i

        # Iterated to this for problem 1B
        if sum_elf > min(top_3):
            # rearrange top 3, drop the lowest
            arg_min = np.argmin(top_3)
            top_3[arg_min] = sum_elf

    print(max)
    print(top_3)
    print(np.sum(top_3))
        

