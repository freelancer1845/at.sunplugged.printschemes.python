'''
Created on 16.05.2017
Defining all available shapes.


@author: Jascha Riedel
'''

import operator
from Utils import LineGroup

class Line:
    ''' Representing a basic line '''
    def __init__(self, start=(0, 0), end=(0, 0)):
        if isinstance(start, tuple) == False:
            if _checkIfIntFloatOrLong(start[0]) == False or _checkIfIntFloatOrLong(start[1]):
                raise ValueError('xstart and ystart must be numbers!')
            raise ValueError('start must be a tupel! (xStart,yStart)')
        if isinstance(end, tuple) == False:
            if _checkIfIntFloatOrLong(end[0]) == False or _checkIfIntFloatOrLong(end[1]) == False:
                raise ValueError('xEnd and yEnd must be numbers!')
            raise ValueError('end must be a tupel! (xEnd,yEnd)')
        
        self.start = start
        self.end = end
        
    def translate(self, translationVector = (0, 0)):
        if isinstance(translationVector, tuple) == False:
            raise ValueError('translationVetor must be a tuple')
        if _checkIfIntFloatOrLong(translationVector[0]) == False or _checkIfIntFloatOrLong(translationVector[1]) == False:
            raise ValueError('translationVector must be a tuple of numbers!')
        self.start = tuple(map(operator.add, self.start, translationVector));
        self.end = tuple(map(operator.add, self.end, translationVector));
        return self
    
  
class LaserLine(Line):
    ''' Representing a Laser line. Normal line with power frequency and speed associated.'''
    def __init__(self, start=(0, 0), end=(0, 0), power=0, frequency=0, speed=0):
        Line.__init__(self, start, end)
        if isinstance(power, (int, long)) == False:
            raise ValueError('power must be a integer!')
        if isinstance(frequency, (int, long)) == False:
            raise ValueError('frequency must be a integer!')
        if isinstance(speed, (int, long)) == False:
            raise ValueError('speed must be a integer!')
        self.power = power
        self.frequency = frequency
        self.speed = speed
    
    def createCopy(self, translationVector):
        ''' Creates a copy of the the laserline and if provided translates the copy by the translationvector'''
        newLine = LaserLine(self.start,self.end,self.power,self.frequency,self.speed).translate(translationVector)
        
        return newLine
    
class LaseredFiducial(LineGroup):
    ''' LaseredFiducial with default size. The center point will be the center of the cross '''
    def __init__(self, center=(0, 0), width = 5, height = 5, power = 45, freq = 20, speed = 25000):
        if isinstance(center, tuple) == False:
            raise ValueError('parameter center must be a tuple of x and y position!');
        if _checkIfIntFloatOrLong(center[0]) == False or _checkIfIntFloatOrLong(center[1]):
            raise ValueError('x and y of center must be long or int!')
        xstart = center[0] - width / 2.0;
        xend = center[0] + width / 2.0;
        ystart = center[0] - height / 2.0;
        yend = center[0] + height / 2.0;
        self.addLine(LaserLine((xstart, center[1]), (xend, center[1]), power, freq, speed));
        self.addLine(LaserLine((center[0], ystart), (center[0] , yend), power, freq, speed));
        
        

class Rectangle:
    '''Representing a simple rectangle'''
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        if _checkIfIntFloatOrLong(x) == False:
            raise ValueError('x must be a number!')
        if _checkIfIntFloatOrLong(y) == False:
            raise ValueError('y must be a number!')
        if _checkIfIntFloatOrLong(width) == False:
            raise ValueError('width must be a number!')
        if _checkIfIntFloatOrLong(height) == False:
            raise ValueError('height must be a number!')
        
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
    
def _checkIfIntFloatOrLong( x ):
    return isinstance(x, (float, long, int))