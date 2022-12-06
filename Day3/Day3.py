import numpy as np

def get_letter_val(letter):
    if letter.isupper():
        # 38 is magic number to convert uppercase letter to 27 through 52
        return ord(letter) - 38
    else:
        # 96 is magic number to convert lowercase letter to 1 through 26
        return ord(letter) - 96

def runPart1(file_input):
    total = 0

    for compartment in file_input:
        midway_i = len(compartment)//2
        compartment1 = compartment[:midway_i]
        compartment2 = compartment[midway_i:]

        for c in compartment1:
            if c in compartment2:
                total += get_letter_val(c)
                break
    print(total)

def runPart2(file_input):
    total = 0
    for i in range(len(file_input)//3):
        modifier = 3 * i
        rucksack_1 = file_input[modifier + 0]
        rucksack_2 = file_input[modifier + 1]
        rucksack_3 = file_input[modifier + 2]

        for c in rucksack_1:
            if c in rucksack_2 and c in rucksack_3:
                total += get_letter_val(c)
                break

    print(total)

    

if __name__ == '__main__':
    file = open('input.txt')
    file_input = file.read().split('\n')

    runPart1(file_input)
    runPart2(file_input)



