import numpy as np

if __name__ == '__main__':
    file = open('input.txt')
    compartments = file.read().split('\n')
    total = 0

    for compartment in compartments:
        midway_i = len(compartment)//2
        compartment1 = compartment[:midway_i]
        compartment2 = compartment[midway_i:]

        for c in compartment1:
            if c in compartment2:
                if c.isupper():
                    # 38 is magic number to convert uppercase letter to 27 through 52
                    total += ord(c) - 38
                else:
                    # 96 is magic number to convert lowercase letter to 1 through 26
                    total += ord(c) - 96
                break

    print(total)
    # part 1
    # for letter in compartments:
    #     print()


