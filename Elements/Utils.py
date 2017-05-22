'''
Created on 16.05.2017

This module contains all Classes and Functions that are useful when using Shapes.

LineGroup is useful composite shapes that consist out of lines.
 But also if you want to combine multiple Lines in a group and want to translate/duplicate them etc.

The duplicateLineArray method may be used to duplicate an list of lines and translate them (replaced by LineGroup...)

@author: Jascha Riedel
'''
import Shapes
import copy


class LineGroup(object):
    ''' Wrapper for multiple lines'''
    def __init__(self, containingLines=[]):
        for line in containingLines:
            if isinstance(line, Shapes.Line) == False:
                raise ValueError('A line group may only consist of lines!');
        self.lines = containingLines;

    def addLine(self, line):
        if isinstance(line, Shapes.Line) == False:
            raise ValueError('A line group may only consist of lines!');
        self.lines.append(line);
    
    def translate(self, translationVector=(0, 0)):
        for line in self.lines:
            line.translate(translationVector);
            
    def createCopy(self, translationVector):
        newGroupLines = []
        for line in self.lines:
            newLine = copy.deepcopy(line);
            newLine.translate(translationVector);
            newGroupLines.append(newLine);
        return newGroupLines;
  

def duplicateLineArray(lines, translationVector=(0, 0)):
    if isinstance(lines, list) == False:
        raise ValueError('lines must be an list like structure!')
    for line in lines:
        if isinstance(line, Shapes.Line) == False:
            raise ValueError('lines contains at least one element that is not a line!')
    if isinstance(translationVector, tuple) == False:
        raise ValueError('translationVetor must be a tuple')
    if _checkIfIntFloatOrLong(translationVector[0]) == False or _checkIfIntFloatOrLong(translationVector[1]) == False:
        raise ValueError('translationVector must be a tuple of numbers!')
    
    
    newLines = copy.deepcopy(lines)
    for line in newLines:
        line.translate(translationVector)
    
    return newLines
    


        

def _checkIfIntFloatOrLong(x):
    return isinstance(x, (float, long, int))
