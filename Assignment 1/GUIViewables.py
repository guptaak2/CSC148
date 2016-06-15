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
PlatformView: A visible Cheese or stool, which a cheese can sit on top of.
CheeseView: A visible Cheese object represented as a PlatformView.
StoolView: A visible stool.

Each PlatformView instance receives a Canvas instance. The Canvas class is a 
class in the tkinter framework. The class is used for a place in a window 
to draw shapes.

PlatformView objects draw themselves as rectangles on the canvas, to represent
side views of stools or rounds of cheese with particular sizes. 

CheeseView objects can be moved and highlighted.
Note that CheeseView inherits from both Cheese and PlatformView

PlatformView objects receive a function to call in order to report to some
UI object (e.g. GUIController) that their rectangle was clicked on.
"""

from TOAHModel import Cheese
from tkinter import Canvas
from tkinter import Event


class PlatformView:
    
    def __init__(self: 'PlatformView',
                 width: float,
                 click_handler: (lambda Event: None),
                 canvas: Canvas,
                 thickness: float,
                 x_center: float, y_center: float):
        """
        Initialize a new PlatformView.
        
        click_handler - function to react to mouse clicks
        width - width in pixels of the displayed representation
        canvas - space to draw a representation of this platform
        thickness - vertical extent of this platform
        x_center - center of this platform horizontally
        y_center - center of this platform vertically
        """

        self.canvas = canvas
        self._width = width
        self.x_center = x_center
        self.y_center = y_center
        self.thickness = thickness

        # Create a rectangle on the canvas, and record the index that tkinter
        # uses to refer to it.
        self.index = canvas.create_rectangle(0, 0, 0, 0)
        self.canvas.itemconfigure(self.index)

        # Initial placement.
        self.place(x_center, y_center)

        # Tell the canvas to report when the rectangle is clicked.
        # The report is a call to click_handler, passing it this CheeseView
        # instance so the controller knows which one was clicked.
        canvas.tag_bind(self.index,
                        '<ButtonRelease>',
                        lambda _: click_handler(self))    
        
    def place(self: 'PlatformView', x_center: float,
              y_center: float):
        """
        Place rectangular image of this cheese/stool at (x_center, y_center)
        """
        # corners are half of size or thickness away
    
        self.canvas.coords(self.index,
                           round(x_center - self._width / 2),
                           round(y_center - self.thickness / 2),
                           round(x_center + self._width / 2),
                           round(y_center + self.thickness / 2))
        # record new center
        self.x_center = x_center
        self.y_center = y_center    
        

class CheeseView(Cheese, PlatformView):
    def __init__(self: 'CheeseView',
                 size: int,
                 width: float,
                 click_handler: (lambda Event: None),
                 canvas: Canvas,
                 thickness: float,
                 x_center: float, y_center: float):
        """
        Initialize a new CheeseView.

        width - horizontal extent of this cheese, in pixels
        size - relative size of this cheese, with 1 being the smallest
        click_handler - function to react to mouse clicks
        canvas - space to draw a representation of this cheese
        thickness - vertical extent of this cheese
        x_center - center of this cheese horizontally
        y_center - center of this cheese vertically
        """

        PlatformView.__init__(self, width, click_handler, canvas, thickness, 
                              x_center, y_center)
        Cheese.__init__(self, size)

        # Initially unhighlighted.
        self.highlight(False)

    def highlight(self: 'CheeseView', highlighting: bool):
        """Set this CheeseView's colour to highlighted or not.

           highlighting - whether to highlight"""

        self.canvas.itemconfigure(self.index,
                                  fill=('red' if highlighting else 'orange'))

        
class StoolView(PlatformView):
    
    def __init__(self: 'StoolView',                 
                 width: float,
                 click_handler: (lambda Event: None),
                 canvas: Canvas,
                 thickness: float,
                 x_center: float, y_center: float):
        
        PlatformView.__init__(self, width, 
                              click_handler, canvas, thickness, 
                              x_center, y_center)
        self.canvas.itemconfigure(self.index, fill='black')        
