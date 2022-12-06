#!/usr/bin/python3

from itertools import groupby

def parse_containers(unparsed_string: str) -> list:
    """
    Returns a list of lists with all the containers including a temporal one in index 0
    This function could parse any number of containers.
    """
    # Initialize the list with an empty container to be used later as temporal storage
    containers = [[]]
    # for each number in the last line create a container
    for f in range(len(containers_unparsed[-1].replace(' ',''))):
        containers.append([])
    # Iterate over all the container but the index 
    for line in reversed(containers_unparsed[:-1]):
        # Iterates over all the line characters
        for idx,char in enumerate(line):
            # Ignore non alphabetic characters
            if char.isalpha():
                # Appends the character to the proper container
                # (Char index in the string) // 4 +1 is the target container
                containers[(idx//4)+1].append(char)
    return containers

def parse_movement(movement: str) -> list:
    """
    Small function to debloat challenge functions.
    Parses movement string and return the needed ints to perform the movements
    """
    cranes = int(movement.split()[1])
    source_idx = int(movement.split()[3])
    target_idx = int(movement.split()[5])
    return cranes,source_idx,target_idx
    

def challenge1(containers_unparsed: str, movements:list) -> str:
    """
    Return the last item of all containers but 0
    """
    containers = parse_containers(containers_unparsed)
    for movement in movements:
        cranes,source_idx,target_idx = parse_movement(movement)
        for crane in range(cranes):
            containers[target_idx].append(containers[source_idx].pop())
    solution = ''.join([container[-1] for container in containers[1:]])
    return solution

def challenge2(containers_unparsed: str, movements:list) -> str:
    """
    Return the last item of all containers but 0
    """
    containers = parse_containers(containers_unparsed)
    for movement in movements:
        cranes,source_idx,target_idx = parse_movement(movement)
        # Uses container 0 as a temporal storage to pop and "depop"
        # This double pop sorts the cranes as expected but I'm sure there are better ways to do this
        for crane in range(cranes):
            containers[0].append(containers[source_idx].pop())
        for crane in range(cranes):
            containers[target_idx].append(containers[0].pop())
    solution = ''.join([container[-1] for container in containers[1:]])
    return solution
    
if __name__ == "__main__":
    # Read file into input_file
    file_name = 'input'
    input_file = [line.rstrip() for line in open(file_name)]
    # Variables added for readibility
    containers_unparsed = [list(group) for k, group in groupby(input_file, bool) if k][0]
    # List of movements
    movements_unparsed = [list(group) for k, group in groupby(input_file, bool) if k][1]
    print(f'Challenge 1 solution: {challenge1(containers_unparsed,movements_unparsed)}')
    print(f'Challenge 2 solution: {challenge2(containers_unparsed,movements_unparsed)}')
