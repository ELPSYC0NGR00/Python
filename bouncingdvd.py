"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
 A bouncing DVD logo animation. You have to be "of a certain age" to
 appreciate this. Press Ctrl-C to stop.

 NOTE: Do not resize the terminal window while this program is running.
 View this code at https://nostarch.com/big-book-small-python-projects
 Tags: short, artistic, bext"""

import sys, random, time 

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
 # We can't print to the last column on Windows without it adding a
 # newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (!) Try changing this to 1 or 100.
PAUSE_AMOUNT = 0.2   # (!) Try changing this to 1.0 or 0.0.
# (!) Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main ():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      y: random.randint(1, HEIGHT -4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1