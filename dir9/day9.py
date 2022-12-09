#!/usr/bin/python3

import numpy as np

def challenge1(forest: np.array) -> int:
    """
    Returns visible tree number
    """
    forest_rows, forest_cols = np.shape(forest)
     # All exterior trees are visible so we add them to the visible trees and ignore after
    visible_trees = forest_cols * 2 + (forest_rows - 2) * 2

    # Iterate over all internal trees
    for row in range(1,forest_rows-1):
        for col in range(1,forest_cols-1):
            tree = forest[row,col]
            
            # Find greatest tree in each direction
            trees_up = max(forest[:row, col])
            trees_down = max(forest[row+1:, col])
            trees_left = max(forest[row,:col])
            trees_right = max(forest[row, col+1:])

            # If tree is higher than all other trees in any direction it's visible
            if tree > trees_up or tree > trees_down or tree > trees_left or tree > trees_right:
                visible_trees +=1

    return visible_trees

def challenge2(forest: np.array) -> int:
    """
    Returns visible tree number
    """
    solution = 0
    forest_rows, forest_cols = np.shape(forest)
    # Iterate over all internal trees
    for row in range(forest_rows):
        for col in range(forest_cols):
            tree = forest[row,col]
            # Initialize variable at 1 because it's 
            tree_score = 1
            
            # Creates arrays of trees in all directions
            # up and left direction must be reversed to iterate over them later
            trees_up = reversed(forest[:row, col])
            trees_down = forest[row+1:, col]
            trees_left = reversed(forest[row,:col])
            trees_right = forest[row, col+1:]

            # Check up right and down direction
            for tree_array in [trees_right,trees_down,trees_up,trees_left]:
                score_multiplier = 0
                for t in tree_array:
                    score_multiplier +=1
                    if t >= tree: break
                tree_score *= score_multiplier
            solution = max(solution,tree_score)

    return solution
    
if __name__ == "__main__":
    # Read file into np.array
    file_name = 'input'
    forest = np.array([list(x.strip()) for x in open(file_name)],int)
    print(f'Challenge 1 solution: {challenge1(forest)}')
    print(f'Challenge 2 solution: {challenge2(forest)}')

