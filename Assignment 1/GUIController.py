# Copyright 2013, 2014 Gary Baumgartner, Dustin Wehr
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
GUIController: GUI window for manually solving Anne Hoy's problems.
"""


from TOAHModel import TOAHModel, IllegalMoveError
from GUIViewables import CheeseView, PlatformView, StoolView
import tkinter as TI
import time
import sys


class GUIController:
    
    def __init__(self: 'GUIController', 
                 number_of_cheeses: int, number_of_stools: int,
                 content_width: float, content_height: float,
                 cheese_scale: float):
        """
        Initialize a new GUIView.

        number_of_cheeses - number of cheese to tower on the first stool
        number_of_stools - number of stools
        content_width - width in pixels of the working area
        content_height - height in pixels of the working area
        cheese_scale - height in pixels for showing cheese thicknesses,
                       and to scale cheese diameters
        """

        self._model = TOAHModel(number_of_stools)
        self._stools = []
        self._cheese_to_move = None
        self._blinking = False
        self._number_of_stools = number_of_stools
        self.cheese_scale = cheese_scale
 
        self.root = TI.Tk()
        canvas = TI.Canvas(self.root,
                           background="blue",
                           width=content_width, height=content_height)
        canvas.pack(expand=True, fill=TI.BOTH)
 
        self.moves_label = TI.Label(self.root)
        self.show_number_of_moves()
        self.moves_label.pack()
        
        # the dimensions of a stool are the same as a cheese that's
        # one size bigger than the biggest of the number_of_cheeses cheeses.
        for stool_ind in range(number_of_stools):
            width = self.cheese_scale * (number_of_cheeses + 1)
            x_cent = content_width * (stool_ind + 1) / (number_of_stools + 1.0)
            y_cent = content_height - cheese_scale / 2
            stool = StoolView(width, 
                              lambda s: self.stoolClicked(s),
                              canvas,
                              self.cheese_scale,         
                              x_cent,
                              y_cent)            
            self._stools.append(stool)
 
        # Can't use self._model.fill_first_stool because we need to 
        # use CheeseView objects instead of just Cheese objects.         
        total_size = self.cheese_scale  
        for sizeparam in range(1, number_of_cheeses + 1):        
            size = (number_of_cheeses + 1 - sizeparam)
            width = self.cheese_scale * size
            x_cent = content_width / (number_of_stools + 1.0)
            y_cent = content_height - cheese_scale / 2 - total_size
            cheese = CheeseView(size,
                                width,
                                lambda c: self.cheeseClicked(c),
                                canvas,
                                self.cheese_scale,
                                x_cent,
                                y_cent)
            self._model.add(0, cheese)
            total_size += self.cheese_scale       

    def cheeseClicked(self: 'GUIController', cheese: 'CheeseView'):
        """React to cheese being clicked: if not in the middle of blinking
           then select cheese for moving, or for moving onto.

           cheese - clicked cheese
        """        
        if not self._blinking:
            self.select_cheese(cheese)
            
    def stoolClicked(self: 'GUIController', stool: 'StoolView'):
        """React to cheese being clicked: if not in the middle of blinking
        then select cheese for moving, or for moving onto.
        
        cheese - clicked cheese
        """        
        if not self._blinking:
            self.select_stool(stool)    

    def select_cheese(self: 'GUIController', cheese: CheeseView):
        """
        Called by cheeseClicked.
        If no cheese is selected to move, then select the cheese at 
        top of clicked_cheese's stool (which may be clicked_cheese 
        itself) and highlight it.
        If selected_cheese is already highlighted, then unhighlight it.
        Otherwise try to move self._cheese_to_move onto the stool that 
        clicked_cheese is on.
        """
        
        stool = self._stools[self._model.cheese_location(cheese)]
        stool_index = self.stool_index(stool)
        cheese = self._model.top_cheese(stool_index)            
        #print(stool, stool_index, cheese)
        if self._cheese_to_move is None:
            self._cheese_to_move = cheese
            self._cheese_to_move.highlight(True)
            self.root.update()
        elif self._cheese_to_move is cheese:
            self._cheese_to_move.highlight(False)
            self._cheese_to_move = None
            self.root.update()
        else:
            self.select_platform_for_move(cheese, stool_index)
            
    def select_stool(self: 'GUIController', dest_stool: StoolView):
        """
        Called by stoolClicked. Initiate a move if there is already some
        cheese highlighted (i.e. self._cheese_to_move is not None), unless
        self._cheese_to_move is on dest_stool, in which case do nothing. 
        """        
        if self._cheese_to_move is not None:
            origin_stool = self._stools[
                self._model.cheese_location(self._cheese_to_move)]
            dest_stool_index = self.stool_index(dest_stool)
            origin_stool_index = self.stool_index(origin_stool)
            if origin_stool_index != dest_stool_index:
                top_cheese = self._model.top_cheese(dest_stool_index)
                if top_cheese is None:
                    self.select_platform_for_move(dest_stool, dest_stool_index)
                else:
                    self.select_platform_for_move(top_cheese, dest_stool_index)
            
    def select_platform_for_move(self: 'GUIController', 
                                 platform: PlatformView, stool_index: int): 
        """
        Actually responsible for showing the cheese move on the screen, and 
        for telling the model to update itself.
        Change self._cheese_to_move's coordinates so that it's on top of 
        platform.
        
        platform - the StoolView or CheeseView that we want to move
        self._cheese_to_move onto. 
        stool_index - if platform is a stool, then this is its index, and
        if platform is a cheese then this is the index of the stool that
        it is on.
        """      
        
        if self._cheese_to_move is not None:
            try:
                from_stool = self._model.cheese_location(
                    self._cheese_to_move)
                self._model.move(from_stool, stool_index)                
                self._cheese_to_move.place(platform.x_center,
                                           platform.y_center 
                                           - self.cheese_scale)
                self.show_number_of_moves()
            except IllegalMoveError as e:
                print(e)
                self._blinking = True
                for i in range(10):
                    self._cheese_to_move.highlight(i % 2 != 0)
                    self.root.update()
                    time.sleep(0.1)
                self._blinking = False      
            self._cheese_to_move.highlight(False)
            self._cheese_to_move = None    
            
    def stool_index(self: 'GUIView', stool: 'StoolView') -> int:
        return self._stools.index(stool)
    
    def show_number_of_moves(self: 'GUIView'):
        """Show the number of moves so far."""
        self.moves_label.config(text='Number of moves: ' +
                                str(self._model.number_of_moves()))
    
    def get_stool(self: 'GUIController', i: int) -> 'StoolView':
        return self._stools[i]
    
    def top_cheese(self: 'GUIController', i: int) -> 'CheeseView':
        return self._model.top_cheese(i)

if __name__ == '__main__':
    gui = GUIController(5, 4, 1024, 320, 20)    
    TI.mainloop()
