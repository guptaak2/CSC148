"""
# Copyright 2013 Nick Cheng, Brian Harrington, Danny Heap, Akhil Gupta 2013,2014
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
# along with this file.  If not, see .
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, Leaf, StarTree, DotTree, BarTree

# Do not change any of the class declarations above this comment
# Student code below this comment.

def is_regex(s):
    '''
    (str) -> bool
    Return True if 's' is a valid regular expression, False otherwise.

    >>> is_regex('0')
    True
    >>> is_regex('0*')
    True
    >>> is_regex('(0.1)')
    True
    >>> is_regex('(0*|2*)')
    True
    >>> is_regex('((0.1).2)')
    True
    >>> is_regex('((1.(0|2)*).2)')
    True
    '''
    lst_i = []
    symbols = ['.', '|']
    if s.count('(') != s.count(')'):
        return False
    if s in ['0', '1', '2', 'e']:
        return True
    if "*" in s:
        if s[-1] == '*':
            return is_regex(s[:-1])
    if s.startswith('('):
        if '.' in s:
            for i in range(len(s)):
                if s[i] in symbols:
                    lst_i.append(i)
                    i = max(lst_i)
                    r1 = is_regex(s[1:i])
                    r2 = is_regex(s[i + 1:s.find(')', i)])
            return (r1 and r2)
    return False
        

def regex_perms(s):
    '''
    (str) -> list
    Return the list of permutations of s.
    # Code provided by Dan(lecture)
    '''
    if len(s) == 0:
        return [""]
    regex_lst = []
    lst = []
    for i in range(len(s)):
        shorter = s[0:i] + s[i+1:]
        short_perms = regex_perms(shorter)
        for p in short_perms:
            new_perm = s[i] + p
            if new_perm not in regex_lst:
                regex_lst.append(new_perm)
    return regex_lst

def all_regex_permutations(s):
    '''
    (list) -> set
    Return the set of permutations of s that are valid regex expressions
    '''
    regex_lst = []
    lst = regex_perms(s)
    for element in lst:
        if is_regex(element):
            if element.count('(') == element.count(')'):
                regex_lst.append(element)
    return set(regex_lst)
            

def build_regex_tree(regex):
    '''
    (regex) -> tree
    Return the root of the corresponding regular expression tree.
    '''
    lst_i = []
    if regex in ['0', '1', '2', 'e']:
            return Leaf(regex)
    if "*" in regex:
        if regex[-1] == "*":
            return StarTree(build_regex_tree(regex[:-1]))
    if regex.startswith('('):
        if '.' in regex:
            for i in range(len(regex)):
                if regex[i] is '.':
                    lst_i.append(i)
                    i = max(lst_i)
                    r1 = regex[1:i]
                    r2 = regex[i + 1:regex.find(')', i)]
            return DotTree(build_regex_tree(r1), build_regex_tree(r2))
        elif '|' in regex:
            for i in range(len(regex)):
                if regex[i] is '|':
                    lst_i.append(i)
                    i = max(lst_i)
                    r1 = regex[1:i]
                    r2 = regex[i + 1:regex.find(')', i)]
            return BarTree(build_regex_tree(r1), build_regex_tree(r2))
    return False
        
def regex_match(r,s):
    '''
    (RegexTree, str) -> bool
    Return True iff s matches RegexTree.
    '''
    if r.symbol == '0':
        return s == '0'
    if r.symbol == '1':
        return s == '1'
    if r.symbol == '2':
        return s == '2'
    if r.symbol == 'e':
        return s == ''
      
    if isinstance(r, StarTree):
        if s == '':
            return True
        else:
            for i in range(len(s)):
                if s[i] == r.children[0].symbol and s[i] * len(s) == s:
                    return regex_match(r.children[0], s[i])
                return False
              
    elif isinstance(r, BarTree):
        return regex_match(r.children[0], s) or regex_match(r.children[1], s)
        
    elif isinstance(r, DotTree):
        if s == '':
            return True  
        else:
            for i in range(len(s)):
                s1 = s[:i]
                s2 = s[i:]
            return (regex_match(r.children[0], s1) and \
                   regex_match(r.children[1], s2))

    


        
    
    
