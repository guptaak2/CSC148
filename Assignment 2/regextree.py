"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, 2013, 2014
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014
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

# Do not change any of the declarations of RegexTree class and its
# subclasses!  This module provides the various RegexTree subclasses
# you need to complete regex_functions.py

class RegexTree:
    """Root of a regular expression tree"""
    def __init__(self: 'RegexTree', symbol: str, children: list) -> None:
        """A new RegexTree with regex symbol and subtrees children.

        symbol must be one of "0", "1", "2", "e", "|", ".", "*"

        >>> print(RegexTree("0", []))
        RegexTree('0', [])
        >>> print(RegexTree("1", []))
        RegexTree('1', [])
        """
        self.symbol, self.children = symbol, children[:]

    def __repr__(self: 'RegexTree') -> str:
        """Return string representation of this RegexTree."""
        return 'RegexTree({}, {})'.format(
            repr(self.symbol), repr(self.children))

    def __eq__(self: 'RegexTree', other: object) -> bool:
        """Return whether RegexTree self is equivalent to other

        >>> RegexTree("1", []).__eq__(RegexTree("2", []))
        False
        >>> RegexTree("2", []).__eq__(RegexTree("2", []))
        True
        """
        return (isinstance(other, RegexTree) and
                self.symbol == other.symbol and
                self.children == other.children)


class Leaf(RegexTree):
    """RegexTree with symbol in '012e' and no children"""
    def __init__(self: 'Leaf', symbol: str) -> None:
        """Create a Leaf with symbol and no children"""
        RegexTree.__init__(self, symbol, [])

    def __repr__(self: 'Leaf') -> str:
        """Return string representation of Leaf self"""
        return 'Leaf({})'.format(repr(self.symbol))


class UnaryTree(RegexTree):
    """RegexTree with a single child, so far used only for star nodes."""
    def __init__(self: 'RegexTree', symbol: str, child: 'RegexTree') -> None:
        """A new UnaryTree with regex symbol and (only) child"""
        RegexTree.__init__(self, symbol, [child])

    def __repr__(self: 'UnaryTree') -> str:
        """Return string representation of this UnaryTree"""
        return 'UnaryTree({}, {})'.format(
            repr(self.symbol), repr(self.children[0]))


class BinaryTree(RegexTree):
    """RegexTree with two children.  so far, it's only used for bar
    and dot nodes.
    """
    def __init__(self: 'BinaryTree', symbol: str,
                 left: 'RegexTree', right: 'RegexTree') -> None:
        """A new BinaryTree with regex symbol and left and right children.
        """
        RegexTree.__init__(self, symbol, [left, right])

    def __repr__(self: 'BinaryTree') -> str:
        """Return string representation of this BinaryTree"""
        return 'BinaryTree({}, {}, {})'.format(repr(self.symbol), 
                                               repr(self.children[0]), 
                                               repr(self.children[1]))


class StarTree(UnaryTree):
    """A UnaryTree rooted at a star ("*")

    >>> rtn0 = RegexTree("0", [])
    >>> rtn1 = RegexTree("1", [])
    >>> rtdot = DotTree(rtn1, rtn1)
    >>> rtbar = BarTree(rtn0, rtdot)
    >>> StarTree(rtbar).__eq__(\
StarTree(BarTree(RegexTree('0', []), DotTree(RegexTree('1', []), RegexTree('1', [])))))
    True
    """
    def __init__(self: 'StarTree', child: 'RegexTree') -> None:
        """New StarTree with (only) child"""
        UnaryTree.__init__(self, '*', child)

    def __repr__(self: 'StarTree') -> str:
        """Return string representation of this StarTree"""
        return 'StarTree({})'.format(repr(self.children[0]))


class BarTree(BinaryTree):
    """A UnaryTree rooted at a bar ("|")

    >>> rtn0 = RegexTree("0", [])
    >>> rtn1 = RegexTree("1", [])
    >>> BarTree(rtn0, rtn1) == BarTree(RegexTree('0', []), \
RegexTree('1', []))
    True
    """

    def __init__(self: 'BarTree', left: 'RegexTree', 
                 right: 'RegexTree') -> None:
        BinaryTree.__init__(self, "|", left, right)

    def __repr__(self: 'BarTree') -> str:
        """Return string representation of this BarTree"""
        return 'BarTree({}, {})'.format(repr(self.children[0]), 
                                        repr(self.children[1]))


class DotTree(BinaryTree):
    """BinaryTree for a dot ('.')"""
    def __init__(self: 'DotTree', left: 'RegexTree',
                 right: 'RegexTree') -> None:
        """New DotTree with left and right children

        >>> rtn0 = RegexTree("0", [])
        >>> rtn1 = RegexTree("1", [])
        >>> DotTree(rtn0, rtn1) == DotTree(RegexTree('0', []), \
RegexTree('1', []))
        True
        """
        BinaryTree.__init__(self, ".", left, right)

    def __repr__(self: 'DotTree') -> str:
        """Return string representation of this DotTree"""
        return 'DotTree({}, {})'.format(repr(self.children[0]), 
                                        repr(self.children[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
