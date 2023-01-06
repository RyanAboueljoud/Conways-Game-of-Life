'''
Python implementation of Conway's Game of Life

Accepts command line arguments to alter board size and random seed
run with -h for more info

References:
    https://beltoforion.de/en/game_of_life/
    https://beltoforion.de/en/recreational_mathematics/game_of_life.php
    https://github.com/beltoforion/recreational_mathematics_with_python
    https://www.pygame.org/docs/
    https://www.geeksforgeeks.org/command-line-arguments-in-python/
    https://github.com/dwyl/english-words
'''

import random
import pygame
import numpy as np
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("-s", "--seed", help="Set manual seed")
parser.add_argument("-x", "--xaxis", help="Set game board width")
parser.add_argument("-y", "--yaxis", help="Set game board height")
parser.add_argument("-c", "--cell", help="Set grid cell size")

# Read arguments from command line
args = parser.parse_args()

col_grid = (30, 30, 60)     # Grid color
col_about_to_die = (185, 0, 0)
col_alive = (255, 213, 0)
col_background = (10, 10, 40)


def init(dimx, dimy):
    seed = ''

    # Set random seed using command line argument
    # or using three random words
    if args.seed:
        seed = args.seed
    else:
        with open('words.txt') as word_file:
            words = word_file.readlines()
        for n in range(3):
            index = random.randint(0, len(words))
            seed += f'{words[index]}'.replace("\n", "").capitalize()
            if n < 2:
                seed += '-'
    print(seed)
    random.seed(seed)      # Set random seed

    cells = np.zeros((dimy, dimx))

    # Randomly set the game board
    for row, col in np.ndindex(cells.shape):
        cells[row, col] = random.randint(0, 1)

    return cells, seed


def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r - 1:r + 2, c - 1:c + 2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c * sz, r * sz, sz - 1, sz - 1))

    return nxt


def main(dimx, dimy, cellsize):
    # Initialize game board size
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))

    # Initialize game board cells
    cells, rand_seed = init(dimx, dimy)

    # Set window title
    title = "John Conway's Game of Life"
    title += ' - Random Seed = ' + rand_seed
    pygame.display.set_caption(title)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    if args.xaxis:  # Game surface length
        x = int(args.xaxis)
    else:
        x = 120

    if args.yaxis:  # Game surface height
        y = int(args.yaxis)
    else:
        y = 90

    if args.cell:   # Random seed
        c = int(args.cell)
    else:
        c = 8

    main(x, y, c)    # 120, 90, 8
