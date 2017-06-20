'''
Created on Jun 20, 2017

@author: Jascha Riedel
'''
from ScriptAlgorithms.laserLineAlgorithm import readBackScriptFile
from GraphicalRepresentations import matplotlibRepresentation


if __name__ == '__main__':
    laserLines = readBackScriptFile('text.txt')
    
    ''' this creates a simple matplotlib representation '''
    canvas = matplotlibRepresentation.matplotCanvas([laserLines]);
    
    
    canvas.plot();
    
