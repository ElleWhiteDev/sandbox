import os
import random
import time

SNOW_DENSTITY = 10
DELAY = .5

snowflakes = ['❄️', '❅', '❆','❉','❊']

term = os.get_terminal_size()

w = term.columns
h = term.lines

grid = []

for _ in range(h):
    # can sub letter for space to check if working
    grid.append([' ' * w])


def draw_grid():
    """
    _summary_: Draws the grid
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\033[?25l')

    output = ''

    for row in grid:
        output += ''.join(row) + '\n'

    output = output.strip('\n')

    print(output, end='')


while True:
    # add snowflakes to grid
    row = []

    for _ in range(w):
        if random.random() < SNOW_DENSTITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')

    grid.insert(0, row)
    grid.pop()

    draw_grid()

    time.sleep(DELAY)
