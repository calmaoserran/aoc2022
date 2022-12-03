#!/usr/bin/python3

from itertools import groupby

file_name = 'input'
file_content = [line.rstrip() for line in open(file_name)]
# Split the list using empty elements into a list of lists
# So each Elf calories will be a list
parsed_content = [list(group) for k, group in groupby(file_content, bool) if k]

def challenge(calorie_list: list, number: int) -> int:
    """
    Retuns the sum of calories of the N highest calories elfs
    """
    solution = []
    # Calculates calories for each elf 
    for elf in calorie_list:
        # Appends the sum of calories of each elf to the solution list
        solution.append(sum(int(calorie) for calorie in elf))
    return sum(sorted(solution)[number*-1:])

if __name__ == "__main__":
    print(f'Challenge 1 solution: {challenge(parsed_content,1)}')
    print(f'Challenge 2 solution: {challenge(parsed_content,3)}')