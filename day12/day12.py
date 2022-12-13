#!/usr/bin/python3
import sys
import time

# Using deque for performance. Kinda overkill to be honest since pop(0) would have worked well for a small map but I wanted to try it
# dequeue VS pop -> https://realpython.com/python-deque/
from collections import deque

def parse_map_value(map_unparsed: list) -> list:
    """
    Returns a numeric map with the value of each cell.
    We could use the characters because each character values is ord(character) anyway but this way we already manage S and E exceptions
    """
    # Create a temporary list to insert all parsed values
    outcome = [[None for _ in range(map_cols)] for _ in range(map_rows)]
    # Fill the new list with int values
    for row in range(map_rows):
        # Using offset so [a-z] => [1-25] S => 0 E => 26
        for col in range(map_cols):
            # Setting Start to 0 so it's different of A and we can parse it but also <= 1
            if map_unparsed[row][col]=='S':
                outcome[row][col] = 0
            # Setting END point value to 26 so we can parse it and it's also >= 1
            elif map_unparsed[row][col] == 'E':
                outcome[row][col] = 26
            else:
            # All other characters are normalized to [1-25]
                outcome[row][col] = ord(map_unparsed[row][col]) - ord('a') + 1
    return outcome

def challenge(mapf: list,challenge: int) -> int:
    """
    Solves the map using BFS algorythm. So much comments because it's my first time with BFS, sorry.
    Really good explanations about BFS here -> https://www.youtube.com/watch?v=oDqjPvD54Ss and https://www.youtube.com/watch?v=KiCBXu4P-2Y
    """
    # Intialize FIFO Queue with starting position(s) and also visited positions set
    bfs_q = deque()
    visited = set()
    # Iterate over map to find starting points.
    for row in range(map_rows):
        for col in range(map_cols):
            # For challenge 1 we use 0 as the starting point
            # For challenge 2 we <= 1 so all a and also the old starting point are added as starting positions.
            if (challenge==1 and mapf[row][col] == 0) or (challenge==2 and mapf[row][col] <=1 ):
                bfs_q.append(((row,col), 0))
    # Until we find the ending point we keep iterating over the queue
    while bfs_q:
        # Pop first item of queue
        (row,col),steps = bfs_q.popleft()
        # Ignore it if has already been visited to avoid backtracking
        if (row,col) in visited:
            continue
        # Add node to the visited set
        visited.add((row,col))
        # We got to the ending ! Return steps of current node
        if mapf[row][col] == 26:
            return steps
        # Else add check all the children nodes
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = row+dr
            cc = col+dc
            # For each coordinate if candidate positions is inside the map and is climbable
            # Append the new nodes to the queue and update distance
            if 0<=rr<map_rows and 0<=cc<map_cols and mapf[rr][cc]<=1+mapf[row][col]:
                bfs_q.append(((rr,cc),steps+1))

if __name__ == "__main__":
    start_time = time.time()
    # Read file into a list of lists. Each sublist is a row
    file_name = sys.argv[1] if len(sys.argv)>1 else 'input'
    unparsed_map = [line.rstrip() for line in open(file_name)]
    map_rows = len(unparsed_map)
    map_cols = len(unparsed_map[0])
    parsed_map = parse_map_value(unparsed_map)
    print(f'Challenge 1 solution: {challenge(parsed_map,1)}')
    print(f'Challenge 2 solution: {challenge(parsed_map,2)}')
    print(f'Completed in {(time.time() - start_time)} seconds')
