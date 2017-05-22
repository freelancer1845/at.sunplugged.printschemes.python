'''
Created on 16.05.2017

@author: Jascha Riedel

This should suit as an example for using python ways to create a script for creating a printscheme.
'''
from Elements.Shapes import LaserLine
from Elements.Shapes import LaseredFiducial
import Elements.Utils
import ScriptAlgorithms.laserLineAlgorithm
import GraphicalRepresentations.matplotlibRepresentation
import GraphicalRepresentations.Gui
import Utils

if __name__ == '__main__':
    
    
    ''' This creates n cells and adds a n + 1 incomplete cell plus a cut off line. '''
    ''' We first define a dictonary containing all necessary parameters. These are the default values. A GUI will be opened where the values may be changed.
        Currently only INTEGER values are supported!
     '''
    parameters = {'xStart': 0,
                  'xEnd': 40000,
                  'powerP1': 45,
                  'freqP1': 20,
                  'speedP1': 25000,
                  'yStartP1': 2500,
                  'powerP2': 30,
                  'freqP2': 150,
                  'speedP2': 50000,
                  'yStartP2': 2800,
                  'distanceBetweenP2Lines': 20,
                  'powerP3': 8,
                  'freqP3': 20,
                  'speedP3': 50000,
                  'yStartP3': 2430,
                  'distanceBetweenFirstAndSecondP3Line': 2570 - 2430,
                  'distanceBetweenSecondAndThirdP3Line': 3300- 2570,
                  'yCutOff': -2500,
                  'powerCutOff': 8,
                  'freqCutOff': 20,
                  'speedCutOff': 50000,
                  'distanceBetweenCells': 5000,
                  'numberOfCells': 5,
                  'fiducialX': -5000,
                  'fiducialY': -5000}

    #Graphical representation of a value input form. Not finished.
    inputForm = GraphicalRepresentations.Gui.InputForm(parameters)
    
    if inputForm.open() == True:
        parameters = inputForm.getDictonary();
        for key in parameters:
            print(key, parameters[key]);
    else:
        quit()
    
    
    ''' First create one cell and store all the lines in one list.'''
    singleCellLines = []
    
    ''' Create P1 Line and immediately append it to the singleCellLines... For instance the first parameter is a tuple of xStart and yStart (0, 2500)'''
    singleCellLines.append(LaserLine((parameters['xStart'], parameters['yStartP1']),
                                      (parameters['xEnd'], parameters['yStartP1']),
                                       parameters['powerP1'], parameters['freqP1'], parameters['speedP1']));
    
    ''' Create P2 Lines '''
    for i in range(0, 5):
        singleCellLines.append(LaserLine((parameters['xStart'], parameters['yStartP2'] + i * parameters['distanceBetweenP2Lines']),
                                          (parameters['xEnd'], parameters['yStartP2'] + i * parameters['distanceBetweenP2Lines']),
                                           parameters['powerP2'], parameters['freqP2'], parameters['freqP2']));
        
    ''' Alternative
    startLine = LaserLine((xStart, yStartP1), (xEnd, yEnd), powerP2, freqP2, speedP2)
    singleCellLines.append(startLine)
    for i in range(1, 5):
        nextLine = startLine.createCopy((0, i * distancenBetweenP2Lines))
        singleCellLines.append(nextLine)
    '''
        

    ''' Create P3 Lines '''
    firstLineP3 = LaserLine((parameters['xStart'], parameters['yStartP3']),
                             (parameters['xEnd'], parameters['yStartP3']),
                              parameters['powerP3'], parameters['freqP3'], parameters['speedP3'])
    ''' Alternative
    firstLineP3 = LaserLine()
    firstLineP3.start = (xStart, yStartP3)
    firstLineP3.end = (xEnd, yStartP3)
    firstLineP3.power = powerP3
    firstLineP3.frequency = freqP3
    firstLineP3.speed = speedP3
    '''
    
    secondLineP3 = firstLineP3.createCopy((0, parameters['distanceBetweenFirstAndSecondP3Line']))
    thridLineP3 = secondLineP3.createCopy((0, parameters['distanceBetweenSecondAndThirdP3Line']))
    singleCellLines.append(firstLineP3)
    singleCellLines.append(secondLineP3)
    singleCellLines.append(thridLineP3)
    
    
    ''' Create an array that contains all lines that should be lasered. '''
    allLaserLines = []
    
    ''' There are better ways, but this not just adds the first cell
        and then all others but creates 5 new cells from the single cell and adds them'''
    for i in range(0, parameters['numberOfCells']):
        ''' this duplicates the single cell with a translation vector provided as parameter.
            The first cell has no translation and thus is just the untranslated single cell (i = 0) '''
        currentCell = Elements.Utils.duplicateLineArray(singleCellLines, (0, i * parameters['distanceBetweenCells']))
        
        ''' now add every line of the new cell to allLaserLines'''
        for line in currentCell:
            allLaserLines.append(line)

    ''' Add the n + 1 part cell '''
    ''' Don't forget that there is also a p1 line that belongs to this cell'''
    allLaserLines.append(LaserLine((parameters['xStart'], (parameters['distanceBetweenCells'] * parameters['numberOfCells']) + parameters['yStartP1']),
                                    (parameters['xEnd'], (parameters['distanceBetweenCells'] * parameters['numberOfCells']) + parameters['yStartP1']),
                                     parameters['yStartP1'], parameters['freqP1'], parameters['speedP1']));
    ''' we can reuse the p3 lines '''
    allLaserLines.append(firstLineP3.createCopy((0, parameters['distanceBetweenCells'] * parameters['numberOfCells'])))
    allLaserLines.append(secondLineP3.createCopy((0, parameters['distanceBetweenCells'] * parameters['numberOfCells'])))
                         
    
    ''' Now add the lower cut off p3 line '''
    allLaserLines.append(LaserLine((parameters['xStart'], parameters['yCutOff']),
                                   (parameters['xEnd'], parameters['yCutOff']) ,
                                   parameters['powerCutOff'], parameters['freqCutOff'], parameters['speedCutOff']));
    
    ''' Add a fiducial '''
    fiducial = LaseredFiducial((parameters['fiducialX'], parameters['fiducialY']));
    
    for line in fiducial.lines:
        print(line.start, line.end)
        allLaserLines.append(line);

    
   
    ''' All lines that should be lasered are added now. To make changes just change the parameters. For Example distance between cells'''
    
    ''' This uses the ScriptAlgorithm to create the laserlinesscript '''
    nullX = 15000
    nullY = -15000
    laserScript = ScriptAlgorithms.laserLineAlgorithm.createScriptFromLaserLinesWithExplicitNullPoint(allLaserLines, nullX, nullY)
    print (laserScript)
    
    
    ''' this creates a simple matplotlib representation '''
    canvas = GraphicalRepresentations.matplotlibRepresentation.matplotCanvas();
    
    canvas.lines = allLaserLines;
    
    canvas.plot();
    

    
    ''' save the file if you want '''
    filename = raw_input("If you want to save the file, provide a filename:\n")
    if filename != '':
        Utils.saveScript(laserScript,filename)
    

                                                                                                
