#!/usr/bin/python3

file_name = 'input'
input_parsed = [line.rstrip() for line in open(file_name)]

def cheat(game: str) -> str:
    """
    Returns the modified string after intepreting how the round should end
    """
    # Standarize input
    game = game.lower()
    # Dictionary to translate instructions to the final hand
    cheat = {
    'a x':'a z',   # Lose
    'a y':'a x',   # Draw
    'a z':'a y',   # Win
    'b x':'b x',   # Lose
    'b y':'b y',   # Draw
    'b z':'b z',   # Win
    'c x':'c y',   # Lose
    'c y':'c z',   # Draw
    'c z':'c x'}   # Win
    return cheat[game]

def calc_single_game(game: str) -> int:
    """
    Returns the value of the game outcome plus the player 2 pick
    """
    # Standarize input
    game = game.lower()
    # Dictionary used to calculate the player 2 pick points
    xyz_values = {'x': 1,'y': 2,'z': 3}
    # Player 2 pick
    player2_pick = game[-1]
    # Dictionary with all the possible combinations
    game_outcome = {
    'a x':3,'a y':6,'a z':0,
    'b x':0,'b y':3,'b z':6,
    'c x':6,'c y':0,'c z':3}
    return game_outcome[game] + xyz_values[player2_pick]

def challenge1() -> int:
    solution = 0
    for line in input_parsed:
        solution += calc_single_game(line)
    return solution

def challenge2() -> int:
    solution = 0
    for line in input_parsed:
        solution += calc_single_game(cheat(line))
    return solution

if __name__ == "__main__":
    print(f'Challenge 1 solution: {challenge1()}')
    print(f'Challenge 2 solution: {challenge2()}')