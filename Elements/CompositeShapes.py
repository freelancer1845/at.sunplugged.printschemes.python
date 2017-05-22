'''
Created on 22.05.2017


Here all composite Shapes are found.
These should be descendants of their respective groups (for now only LineGroup).

For now thats only the LaseredFiducial. A group of LaserLines.


@author: Jascha Riedel
'''
from Utils import _checkIfIntFloatOrLong;
import Utils
import Shapes


class LaseredFiducial(Utils.LineGroup):
    ''' LaseredFiducial with default size. The center point will be the center of the cross '''
    def __init__(self, center=(0, 0), width = 5000, height = 5000, power = 45, freq = 20, speed = 25000):
        super(LaseredFiducial, self).__init__();
        if isinstance(center, tuple) == False:
            raise ValueError('parameter center must be a tuple of x and y position!');
        if _checkIfIntFloatOrLong(center[0]) == False or _checkIfIntFloatOrLong(center[1]) == False:
            raise ValueError('x and y of center must be long or int!')
        xstart = center[0] - width / 2.0;
        xend = center[0] + width / 2.0;
        ystart = center[0] - height / 2.0;
        yend = center[0] + height / 2.0;
        self.addLine(Shapes.LaserLine((xstart, center[1]), (xend, center[1]), power, freq, speed));
        self.addLine(Shapes.LaserLine((center[0], ystart), (center[0] , yend), power, freq, speed));
        