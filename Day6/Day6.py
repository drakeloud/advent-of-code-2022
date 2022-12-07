import numpy as np

def runPart1(signal):
    for i in range(4, len(signal)):
        temp_set = set(signal[i - 4:i])
        if len(temp_set) == 4:
            print(i)
            break


def runPart2(signal):
    for i in range(14, len(signal)):
        temp_set = set(signal[i - 14:i])
        if len(temp_set) == 14:
            print(i)
            break

if __name__ == '__main__':
    with open('input.txt') as file:
        file_input = file.read()

        runPart1(file_input)
        runPart2(file_input)

