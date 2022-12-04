#!/usr/bin/python3

file_name = 'input'
input_file = [line.rstrip() for line in open(file_name)]

def full_overlap(range1:range, range2:range) -> bool:
    """
    Return true if one range is fully contained in the other.
    """
    range1_in_range2 = range1.start in range2 and range1[-1] in range2
    range2_in_range1 = range2.start in range1 and range2[-1] in range1
    return range1_in_range2 or range2_in_range1

def partial_overlap(range1:range, range2:range) -> bool:
    """
    Return true if any element of one range is in the other Using set.intersection
    """
    r1 = {r for r in range1}
    r2 = {r for r in range2}
    return bool(r1.intersection(r2))

def str_to_range(range_str: str) -> range:
    """
    Convert an string in the format Start-Stop to a range(Start,stop) object
    The range has to be modified to get the end correctly
    ie: string_to_range('2-4') returns a range(2,5) object
    """
    r_start,r_end = [int(n) for n in range_str.split('-')]
    return range(r_start,r_end+1)

def challenge1():
    solution = 0
    for elf in input_file:
    # Each line is a str like this: 14-50,14-50
        r1 = str_to_range(elf.split(',')[0])
        r2 = str_to_range(elf.split(',')[1])
        if full_overlap(r1,r2):
            solution +=1
    return solution

def challenge2():
    solution = 0
    for elf in input_file:
    # Each line is a str like this: 14-50,14-50
        r1 = str_to_range(elf.split(',')[0])
        r2 = str_to_range(elf.split(',')[1])
        if partial_overlap(r1,r2):
            solution +=1
    return solution

if __name__ == "__main__":
    print(f'Challenge 1 solution: {challenge1()}')
    print(f'Challenge 2 solution: {challenge2()}')