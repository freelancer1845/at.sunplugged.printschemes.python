'''
Created on 16.05.2017
Defining all available shapes as classes.

The classes Line and Rectangle are the current base classes. Every Shape should be a descendant of those classes.
One might argue that the Fiducial is also a shape, but it consists out of LaserLines and thus is not a descendant of Line
but a collection of line (i. e. a group of shapes). 


@author: Jascha Riedel
'''

import operator

class Line(object):
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
        if isinstance(power, (int, long, float)) == False:
            raise ValueError('power must be a integer!')
        if isinstance(frequency, (int, long, float)) == False:
            raise ValueError('frequency must be a integer!')
        if isinstance(speed, (int, long, float)) == False:
            raise ValueError('speed must be a integer!')
        self.power = int(power)
        self.frequency = int(frequency)
        self.speed = int(speed)
    
    def createCopy(self, translationVector):
        ''' Creates a copy of the the laserline and if provided translates the copy by the translationvector'''
        newLine = LaserLine(self.start,self.end,self.power,self.frequency,self.speed).translate(translationVector)
        
        return newLine
    

class Rectangle(object):
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
        
    def translate(self, translationVector=(0, 0)):
        if isinstance(translationVector, tuple) == False:
            raise ValueError('translationVetor must be a tuple')
        if _checkIfIntFloatOrLong(translationVector[0]) == False or _checkIfIntFloatOrLong(translationVector[1]) == False:
            raise ValueError('translationVector must be a tuple of numbers!')
        self.x += translationVector[0];
        self.y += translationVector[1];
        
        
class PrintRectangle(Rectangle):
    ''' Representing a rectangle that will be printed later.
        Use metaData to specify 'color' and 'alpha' in the plot. {'color': 'black'; 'alpha': 0.3} ...
    '''
    def __init__(self, x = 0, y = 0, width = 0, height = 0, metaData = None):
        Rectangle.__init__(self, x, y, width, height);
        if metaData is None:
            self.metaData = {};
        else:
            self.metaData = metaData;
        
def _checkIfIntFloatOrLong( x ):
    return isinstance(x, (float, long, int))