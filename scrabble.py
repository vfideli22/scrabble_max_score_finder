# -*- coding: utf-8 -*-
# Python 3.8
"""
Author:     Vincent Fideli
Created:    Thu Jan  5 23:04:39 2023

Description
-----------
Trying to place a given word on a Scrabble board, maximising number of points.
- Inputs word to be searched
- Outputs max score the word can get
- Outputs location 

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### Scrabble board setup
""""
0 = blank
1 = double letter
2 = triple letter
3 = double word
4 = triple word
"""
board = np.array([
    [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4],
    [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
    [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1],
    [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
    [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0],
    [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4]
    ])

# Defining the number of points each letter is worth
points_reversed = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
    }

# Creating the dictionary which has (key, value) of (letter, point), reversing above
points_reference = {letter:point for point, letters in points_reversed.items() for letter in letters}
# for point, letters in points_reversed.items():
#     for letter in letters:
#         print(point, letter)


### Defining functions 
def how_many_points(word, row, column):
    """
    Imposes a word onto a defined scrabble position (row x column). Outputs number of points. 

    Parameters
    ----------
    word : string
        Must be capitalised.
    row : int
    column : int

    Returns
    -------
    points : int
        Number of points this word wins at the specified position.

    """
    points = 0
    is_double_word = 0
    is_triple_word = 0

    for position, letter in enumerate(word):
        point = points_reference[letter]
        if board[row][column + position] == 1:
            point *= 2
        elif board[row][column + position] == 2:
            point *= 3
        elif board[row][column + position] == 3:
            is_double_word += 1
        elif board[row][column + position] == 4:
            is_triple_word += 1
        points += point

    points *= 2 ** is_double_word
    points *= 3 ** is_triple_word

    return points


def scan(word):
    """
    Scans through the whole Scrabble board, left to right (until the end is reached),
    then up to down.

    Parameters
    ----------
    word : string
        Word being scanned through the board.

    Returns
    -------
    max_score : int
        Maximum score achieved by the word.
    scores_grid : numpy array
        Grid showing score achieved by word if the first letter was placed on that square 
        and word went horizontally.

    """
    
    max_score = 0
    scores_grid = np.empty((8, 16 - len(word)), dtype=int)
    
    for row_num in range(8):
        for column_num in range(16 - len(word)):
            # print(row_num, column_num)
            score = how_many_points(word, row_num, column_num)
            
            if score > max_score:
                max_score = score
            
            scores_grid[row_num, column_num] = score

    return max_score, scores_grid

### Inputting names to test
# name = "kascorin"
# name_caps = name.upper()

# Featuring some D&D characters ;)
names = ["kascorin", "orville", "kyvir", "dorothy", "ozman"]

# Iterating through list of names, running functions, graphing
for name in names:
    name_caps = name.upper()
    point, score_map = scan(name_caps)
    print(f"{name}: {point}")
    print(score_map)    # Comment out if you don't want to see the score map :)
    
    # Filling in the heatmap completely
    zeros = np.zeros((8, len(name)-1))
    score_map_plot = np.concatenate((score_map, zeros), axis=1)
    annotated_board = board[:8, :]
    
    # Graphing the heatmaps
    ax = sns.heatmap(score_map_plot, annot=annotated_board, linewidth=0.5, cmap='Blues',\
                     cbar_kws={'label':'points'})
    ax.set_title(name)
    plt.show()
