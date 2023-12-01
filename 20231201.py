# https://adventofcode.com/2023/day/1

import re

def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: replacements[mo.group()], text) 

##############################################################################

if __name__ == "__main__":
    f = open(r"20231201_aoc_input.txt", "r")

    Lines = f.readlines()

    ##########
    # part 1 #
    ##########

    total = 0

    for element in Lines:
        a = re.findall(r'\d', element)
        value = int(a[0] + a[-1])
        total = total + value

    print(total)

    ##########
    # part 2 #
    ##########
    d = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    d2 = {
        'oneight': '18',
        'twone': '21',
        'threeight': '38',
        'nineight': '98',
        'eightwo': '82',
        'eighthree': '83',
    }

    d3 = {'twoneight': '218'}

    total = 0

    for element in Lines:
        element = multiple_replace(d3, element)
        element = multiple_replace(d2, element)
        element = multiple_replace(d, element)
        a = re.findall(r'\d', element)
        value = int(a[0] + a[-1])
        total = total + value

    print(total)

    
