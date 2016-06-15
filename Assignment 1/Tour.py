# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
from ConsoleController import ConsoleController
from GUIController import GUIController
from TOAHModel import TOAHModel
import math 
import time


def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5, 
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to use ConsoleController to animate the tour       
       delay_btw_moves - time delay between moves in seconds IF 
                         console_animate == True
                         no effect if console_animate == False
    """    
    n = four_stools.number_of_cheeses()
    origin = 0
    helper_one = 1
    helper_two = 2
    dest = 3
    four_stool_hanoi(n, origin, helper_one, helper_two, dest)

# Description of solution:
# I have created two helper functions: three_stool_hanoi, four_stool_hanoi
# The four_stool_hanoi uses three_stool_hanoi recursively to compute a solution

# The heart of the solution lies in this line:
# i = int(math.ceil(((math.sqrt(8 * n + 1) - 1)/2)))
# It represents the number of cheeses to move from the stool depending on the
# number of cheeses on that stool. (n = number_of_cheeses)
# After it computes that, the code follows the same procedure as described
# in the Assignment #1 handout.
# It moves (n-i) cheese rounds to an intermediate stool using four_stool_hanoi
# i.e. it moves (n-i) from origin to helper_one using dest and helper_two
# Then it moves (i) cheeses from origin to helper_two using three_stool_hanoi
# Then it moves (n-i) cheeses from helper_one to dest using origin and
# helper_two via four_stool_hanoi.

# The code follows the same procedure described in Assignment #1 handout,
# but with a slightly different approach.

# In three_stool_hanoi, it receives parameters from four_stool_hanoi
# It receives (i, origin, dest, helper_two)
# three_stool_hanoi moves (n-1) cheeses from origin to dest using helper_one

# three_stool_hanoi is used to solve the smaller cheese stack from
# four_stool_hanoi

def three_stool_hanoi(n, origin, dest, helper_one):
    if n != 0:
        if CONSOLE_ANIMATE == True:
            print (four_stools)
            time.sleep(DELAY_BETWEEN_MOVES)
        three_stool_hanoi(n-1, origin, helper_one, dest)
        four_stools.move(origin, dest)
        three_stool_hanoi(n-1, helper_one, dest, origin)

def four_stool_hanoi(n, origin, helper_one, helper_two, dest):
    i = 0
    if n == 1:
        four_stools.move(origin, dest)
        if CONSOLE_ANIMATE == True:
            print (four_stools)
            time.sleep(DELAY_BETWEEN_MOVES)
    elif n == 2:
        four_stools.move(origin, helper_one)
        if CONSOLE_ANIMATE == True:
            print (four_stools)
            time.sleep(DELAY_BETWEEN_MOVES)
        four_stools.move(origin, dest)
        if CONSOLE_ANIMATE == True:
            print (four_stools)
            time.sleep(DELAY_BETWEEN_MOVES)
        four_stools.move(helper_one, dest)
        if CONSOLE_ANIMATE == True:
            print (four_stools)
            time.sleep(DELAY_BETWEEN_MOVES)
    else:
        i = int(math.ceil(((math.sqrt(8 * n + 1) - 1)/2)))
        four_stool_hanoi(n-i, origin, helper_two, dest, helper_one)
        three_stool_hanoi(i, origin, dest, helper_two)
        four_stool_hanoi(n-i, helper_one, origin, helper_two, dest)
    
# The above code uses a solution provided by my high school teacher.
# It is a derivation of the original solution by Ted Roth.
# However, I have explained how the solution works.

# High School Teacher info:
# Mrs. Ouellette,
# 5555 Creditview Rd,St. Joseph Secondary School,
# Mississauga, ON - L5V 2B9
# (905) - 812 - 1376

if __name__ == '__main__':
    NUM_CHEESES = 8
    DELAY_BETWEEN_MOVES = 0.5
    CONSOLE_ANIMATE = True
    
    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)    
    four_stools.fill_first_stool(number_of_cheeses=NUM_CHEESES)
    
    tour_of_four_stools(four_stools, 
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)
    
    print(four_stools.number_of_moves())
