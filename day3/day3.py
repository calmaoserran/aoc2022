#!/usr/bin/python3

file_name = 'input'
input_parsed = [line.rstrip() for line in open(file_name)]

# Tried to do it without external libraries and might be a little overkill but practiced list comprehension and list merge
lower_priorities = dict(zip([chr(f) for f in range(97,123)],range(1,27)))
upper_priorites = dict(zip([chr(f) for f in range(65,91)],range(27,53)))
priorities = {**lower_priorities, **upper_priorites}

def char_priority(char: chr) -> int:
    """
    returns character priority value
    """
    return priorities[char]

def find_duplicates(rugsack: str) -> str:
    """
    Find duplicated characters in first and second half of a word
    """
    first_half = {char for char in rugsack[:len(rugsack)//2]}
    second_half = {char for char in rugsack[len(rugsack)//2:]}
    duplicate = first_half.intersection(second_half).pop()
    return duplicate

def find_badge(rugsack1: str,rugsack2: str,rugsack3: str) -> str:
    """
    finds common character in three words
    assumes only one common character will be found
    """
    r1 = set(rugsack1)
    r2 = set(rugsack2)
    r3 = set(rugsack3)
    badge = r1.intersection(r2,r3).pop()
    return badge

def test_find_duplicates():
    tests = [['vJrwpWtwJgWrhcsFMMfFFhFp','p'],
             ['jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','L'],
             ['PmmdzqPrVvPwwTWBwg','P'],
             ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','v'],
             ['ttgJtRGJQctTZtZT','t'],
             ['CrZsJsPPZsGzwwsLwLmpwMDw','s']]
    for test in tests:
        print(f'{test} OK') if find_duplicates(test[0]) == test[1] else print (f'{test} ERROR. Expected {test[1]} got {find_duplicates(test[0])}')

def test_char_priority():
    tests = [[16,'p'],
             [38,'L'],
             [42,'P'],
             [22,'v'],
             [20,'t'],
             [19,'s']]
    for test in tests:
        print(f'{test} OK') if char_priority(test[1]) == test[0] else print (f'{test} ERROR. Expected {test[0]} got {char_priority(test[1])}')

def challenge1() -> int:
    solution = 0
    # for each Rugsrack
    for line in input_parsed:
        # Calculate the value of the duplicated character and add it to the solution
        solution += char_priority(find_duplicates(line))
    return solution

def challenge2() -> int:
    solution = 0
    # Read three lines of file. I'm not so keen of this solution, tho
    for i in range(0,len(input_parsed),3):
        # Find the badge and adds the value to the solution
        solution += char_priority(find_badge(input_parsed[i],input_parsed[i+1],input_parsed[i+2]))
    return solution

if __name__ == "__main__":
    print(f'Challenge 1 solution: {challenge1()}')
    print(f'Challenge 2 solution: {challenge2()}')