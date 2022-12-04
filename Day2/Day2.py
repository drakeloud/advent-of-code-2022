import numpy as np

SCORE_MAP = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3  # Scissors
}

WIN_LOSS_MAP = {
    'A': { # Rock
        'X': 3, # Rock
        'Y': 6, # Paper
        'Z': 0  # Scissors
    },
    'B': { # Paper
        'X': 0, # Rock
        'Y': 3, # Paper
        'Z': 6  # Scissors
    },
    'C': { # Scissors
        'X': 6, # Rock
        'Y': 0, # Paper
        'Z': 3  # Scissors
    }
}

RESULT_MAP = {
    'A': { # Rock
        'X': 'Z', # LOSE
        'Y': 'X', # DRAW
        'Z': 'Y'  # WIN
    },
    'B': { # Paper
        'X': 'X', # LOSE
        'Y': 'Y', # DRAW
        'Z': 'Z'  # WIN
    },
    'C': { # Scissors
        'X': 'Y', # LOSE
        'Y': 'Z', # DRAW
        'Z': 'X'  # WIN
    }
}

if __name__ == '__main__':
    file = open('Day2-input.txt')
    games = file.read().split('\n')

    # part 1
    total = 0
    for game in games:
        # opponents move and your recommended move
        opponent_move, my_move = game.split(' ')
        win_loss_score = WIN_LOSS_MAP[opponent_move][my_move]
        score = win_loss_score + SCORE_MAP[my_move]
        total += score

    print(total)
    
    # part 2
    part_b_total = 0
    for game in games:
        opponent_move, strategy = game.split(' ')
        my_move = RESULT_MAP[opponent_move][strategy]
        win_loss_score = WIN_LOSS_MAP[opponent_move][my_move]
        score = win_loss_score + SCORE_MAP[my_move]
        part_b_total += score

    print(part_b_total)


