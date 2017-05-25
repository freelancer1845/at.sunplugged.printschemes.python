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


class Group(object):
    ''' A general Group of objects. Functions like translate are immediately passed to the constituents.
        The Parameter 'metaData' may be used in various ways. For example ('color': 'red') will draw all elements in 'red' in the scheme.
    '''
    def __init__(self, elements = None, metaData = None):
        if elements is None:
            self.elements = [];
        elif isinstance(elements, list) == True:
            self.elements = elements;
        else:
            raise ValueError('Elements must be of type list');
        if metaData is None:
            self.metaData = {};
        elif isinstance(metaData, dict) == True:
            self.metaData = metaData;
        else:
            raise ValueError('MetaData must be of type dict');
        
    
    def translate(self, translationVector):
        
        ''' This translates each element of the group if it has a method named 'translate'.'''
        for element in self.elements:
            
            ''' Checks if that method exists '''
            if getattr(element, 'translate', None) is not None:
                element.translate(translationVector);
    
    def addElement(self, element):
        self.elements.append(element);
    
    def createCopy(self, translationVector = (0, 0)):
        newGroup = copy.deepcopy(self);
        newGroup.translate(translationVector);
        return newGroup;
    
    def addMetaData(self, metaData):
        if isinstance(metaData, dict) == True:
            self.metaData.update(metaData);
        else:
            raise ValueError('Meta Data must be provided as dictionary or key value pair');
        
        
    def getAllElementsOfType(self, typeOfElments):
        returnElements = [];
        for element in self.elements:
            if isinstance(element, Group):
                for subElement in element.getAllElementsOfType(typeOfElments):
                    returnElements.append(subElement);
            elif isinstance(element, typeOfElments):
                returnElements.append(element);
        
        return returnElements;


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
