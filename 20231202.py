# https://adventofcode.com/2023/day/2

import pandas as pd
import re

f = open(r"20231202_aoc_input.txt", "r")

Lines = f.readlines()

##########
# part 1 #
##########

total = 0
game_number = 0

for element in Lines:
    max_red = 0
    max_green = 0
    max_blue = 0

    game_number = game_number + 1
    game = element.split(':')[1].split(';')
    for game_round in game:
        cube_set = game_round.split(',')
        for color in cube_set:
            count = int(re.search('\d+', color).group())
            if ('red' in color) & (count>=max_red):
                max_red = count
            if ('green' in color) & (count>=max_green):
                max_green = count
            if ('blue' in color) & (count>=max_blue):
                max_blue = count
    if (max_red<=12) & (max_green<=13) & (max_blue<=14):
        total = total + game_number
        # print(f"{game_number=} {max_red=} {max_green=} {max_blue=}")

print(f"Part 1 answer: {total}")

##########
# part 2 #
##########

total = 0
game_number = 0

for element in Lines:
    max_red = 0
    max_green = 0
    max_blue = 0

    game_number = game_number + 1
    game = element.split(':')[1].split(';')
    for game_round in game:
        cube_set = game_round.split(',')
        for color in cube_set:
            count = int(re.search('\d+', color).group())
            if ('red' in color) & (count>=max_red):
                max_red = count
            if ('green' in color) & (count>=max_green):
                max_green = count
            if ('blue' in color) & (count>=max_blue):
                max_blue = count
    power = max_red * max_green * max_blue
    total = total + power
    # print(f"{game_number=} {max_red=} {max_green=} {max_blue=} {power=}")

print(f"Part 2 answer: {total}")
