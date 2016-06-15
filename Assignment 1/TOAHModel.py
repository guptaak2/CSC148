# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
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
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will 
need to return MoveSequence object after solving an instance of the 4-stool 
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


class TOAHModel:
    """Model a game of Towers Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.

    fill_first_stool - put an existing model in the standard starting config
    move - move cheese from one stool to another
    add - add a cheese to a stool        
    top_cheese - top cheese on a non-empty stool    
    cheese_location - index of the stool that the given cheese is on
    number_of_cheeses - number of cheeses in this game
    number_of_moves - number of moves so far
    number_of_stools - number of stools in this game
    get_move_seq - MoveSequence object that records the moves used so far
     
    """

    def __init__(self: 'TOAHModel', number_of_stools:int):
        '''
        Initializes the TOAHModel with a number of stools.
        '''
        self._move = MoveSequence([])
        self._number_of_stools = number_of_stools
        self.stool_lst = []
        for stool in range(number_of_stools):
            self.stool_lst.append([])
    
    def fill_first_stool(self: 'TOAHModel', number_of_cheeses: int):
        """
        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order 
        of size, with a cheese of size == number_of_cheeses on bottom and 
        a cheese of size == 1 on top.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        """
        self._number_of_cheeses = number_of_cheeses
        first_stool = self.stool_lst[0]
        for cheese in range(1, number_of_cheeses+1):
            first_stool.append(Cheese(cheese))
        first_stool.sort(key = lambda cheese:cheese.size, reverse=True)
        self.end_game_stool = first_stool.copy()
                    
    def move(self: 'TOAHModel', origin_stool: int, dest_stool:int): 
        '''
        Move cheese from one stool to another.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0,1)
        '''
        self._origin_stool = origin_stool
        self._dest_stool = dest_stool

        if self.top_cheese(origin_stool) is None:
            raise IllegalMoveError

        elif self.stool_lst[origin_stool] == self.stool_lst[dest_stool]:
            raise IllegalMoveError
        
        elif self.top_cheese(dest_stool) is None:
            self._move.add_move(origin_stool, dest_stool)
            cheese_to_move = self.top_cheese(origin_stool)
            self.add(dest_stool, cheese_to_move)
            self.stool_lst[origin_stool].remove(cheese_to_move)
            self.stool_lst[origin_stool].sort(key = lambda cheese:cheese.size,
                                              reverse=True)
            
        elif self.top_cheese(origin_stool).size > \
        self.top_cheese(dest_stool).size:
            raise IllegalMoveError
        
        else:
            self._move.add_move(origin_stool, dest_stool)
            cheese_to_move = self.top_cheese(origin_stool)
            self.add(dest_stool, cheese_to_move)
            self.stool_lst[origin_stool].remove(cheese_to_move)
            self.stool_lst[origin_stool].sort(key = lambda cheese:cheese.size,
                                              reverse=True)
      
    def add(self: 'TOAHModel', stool_index:int, cheese):
        '''
        Add a cheese to a stool.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.add(0, Cheese(0))
        '''
        self._stool_index = stool_index
        self.stool_lst[stool_index].append(cheese)

    def top_cheese(self: 'TOAHModel', stool_index:int) -> 'Cheese':
        '''
        Top cheese on a non-empty stool.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.top_cheese(0)
        Cheese(1)
        >>> M.move(0,1)
        >>> M.top_cheese(1)
        Cheese(1)
        '''
        self._stool_index = stool_index
        if self.stool_lst[stool_index] != []:
            return self.stool_lst[stool_index][-1]
        
    def cheese_location(self: 'TOAHModel', cheese) -> int:
        '''
        Index of the stool that the given cheese is on.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.cheese_location(Cheese(5))
        0
        >>> M.move(0,1)
        >>> M.cheese_location(Cheese(1))
        1
        '''
        for item in range(len(self.stool_lst)):
            if cheese in self.stool_lst[item]:
                return item

    def number_of_cheeses(self: 'TOAHModel') -> int:
        '''
        Number of cheeses in this game.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.number_of_cheeses()
        5
        '''
        return self._number_of_cheeses

    def number_of_moves(self: 'TOAHModel') -> int:
        '''
        Number of moves so far.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0,1)
        >>> M.move(0,2)
        >>> M.number_of_moves()
        2
        '''
        return self._move.length()

    def number_of_stools(self: 'TOAHModel') -> int:
        '''
        Number of stools in this game.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.number_of_stools()
        4
        '''
        return self._number_of_stools
    
    def _cheese_at(self: 'TOAHModel', stool_index, 
                   stool_height: int) -> 'Cheese':
        """
        If there are at least stool_height+1 cheeses 
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if len(self.stool_lst[stool_index]) >= stool_height+1:
            self._stool_index = stool_index
            self._stool_height = stool_height
            return self.stool_lst[stool_index][stool_height]
        else:
            return None

    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':        
        return self._move    
                
    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current 
        configurations of cheeses on stools look the same. 
        More precisely, for all h,s, the h-th cheese on the s-th 
        stool of self should be equivalent the h-th cheese on the s-th 
        stool of other
        
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        return self.stool_lst == other.stool_lst
        
    def __str__(self: 'TOAHModel') -> str:       
        """
        Depicts only the current state of the stools and cheese.
        """
        # This is the new __str__. Don't modify this.
        all_cheeses = []
        for height in range(self.number_of_cheeses()):
            for stool in range(self.number_of_stools()):   
                if self._cheese_at(stool,height) is not None:
                    all_cheeses.append(self._cheese_at(stool,height))        
        max_cheese_size = max([c.size for c in all_cheeses]) \
                            if len(all_cheeses) > 0 else 0
        stool_str = "="*(2*max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()
        
        def cheese_str(size: int):            
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler
        
        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str
        
        return lines

class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same 
        size."""
        return isinstance(other, Cheese) and self.size == other.size
    
       
class IllegalMoveError(Exception):
    pass
       
class MoveSequence(object):
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves
            
    def get_move(self: 'MoveSequence', i: int):
        if not (0 <= i < self.length()):
            raise IllegalMoveError
        else:
            return self._moves[i]
        
    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))
        
    def length(self: 'MoveSequence') -> int:
        return len(self._moves)
    
    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int, 
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in move_seq.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model
        
    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
