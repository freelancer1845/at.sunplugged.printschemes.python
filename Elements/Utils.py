'''
Created on 16.05.2017

This module contains some Utility classes and functions that can be used to save time.

@author: Jascha Riedel
'''
import Shapes
import copy


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
    


class LineGroup:
    def __init__(self, lines):
        if isinstance(lines, list) == False:
            raise ValueError('lines must be an list like structure!')
        for line in lines:
            if isinstance(line, Shapes.Line) == False:
                raise ValueError('lines contains at least one element that is not a line!')
        
        self.lines = lines
    
    def translateLines(self, translationVector=(0, 0)):
        if isinstance(translationVector, tuple) == False:
            raise ValueError('translationVector must be a tuple!')
        if _checkIfIntFloatOrLong(translationVector[0]) == False or _checkIfIntFloatOrLong(translationVector[1]) == False:
            raise ValueError('translationVector must be a tuple of numbers!')
        
        for line in self.lines:
            line.start = line.start + translationVector;
            line.end = line.end + translationVector;
            
    def createCopy(self, translationVector=(0, 0)):
        return copy.deepcopy(self).translateLines(translationVector)
        

def _checkIfIntFloatOrLong(x):
    return isinstance(x, (float, long, int))
