# Copyright 2014 Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014.
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
"""
ConsoleController: User interface for manually solving Anne Hoy's problems      
from the console.

move: Apply one move to the given model, and print any error message 
to the console. 
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError

def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console. 
    
    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want 
             to move
    dest - the stool number that you want to move the top cheese 
            on stool origin onto.        
    '''
    try:
        model.move(origin, dest)
    except IllegalMoveError:
        print ("***Can't perform move***")
    except IndexError:
        print ("***Stool does not exist***")
    except AttributeError:
        print ("***Move not possible***")
    else:
        pass

class ConsoleController:
    
    def __init__(self: 'ConsoleController', 
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool                            
        number_of_stools - number of stools
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools
        self.model = TOAHModel(number_of_stools)
        self.cheeses = self.model.fill_first_stool(number_of_cheeses)
        self.play_loop()
                
    def play_loop(self: 'ConsoleController'):
        '''    
        Console-based game. 
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've 
        provided to print a representation of the current state of the game.
        '''
        print ("Welcome to Towers Of Anne Hoy!")
        print ("Instructions: The stool numbers start from 0.")
        print ("Please enter the source stool when prompted.")
        print ("Source stool is the stool number to move the cheese from.")
        print ("Please enter the destination stool when prompted.")
        print ("Destination stool is the stool number to move the cheese to.")
        print ("Enter 'e' to exit.")
        print (" ")
        print (self.model)
        print (" ")
        print ("Let's start!")
        print (" ")

        while True: 
            try:
                if self.model.end_game_stool == self.model.stool_lst[-1]:
                    print ("GAME OVER!")
                    raise SystemExit
                self.play_loop
                origin_stool = input("Please enter the source stool: ")
                if origin_stool == 'e':
                    print ("***Thanks for playing!***")
                    raise SystemExit    
                dest_stool = input("Please enter the destination stool: ")
                if dest_stool == 'e':
                    print ("***Thanks for playing!***")
                    raise SystemExit 
                move(self.model, int(origin_stool), int(dest_stool))
                print (self.model)
                print ("Number of moves so far: "
                       +str(self.model.number_of_moves()))
                print (" ")
            except ValueError:
                print ("***Bad input***")

if __name__ == '__main__':
    # TODO: 
    # You should initiate game play here. Your game should be playable by
    # running this file.    
    game = ConsoleController(5, 4)
    
