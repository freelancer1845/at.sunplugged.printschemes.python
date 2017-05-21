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
import Utils

if __name__ == '__main__':
    
    
    ''' This creates n cells and adds an n + 1 incomplete cell plus a cut off line. '''

    xStart = 0
    xEnd = 40000
    
    ''' Parameters For P1 '''
    powerP1 = 45
    freqP1 = 20
    speedP1 = 25000
    yStartP1 = 2500
    
    ''' Parameters For P2 '''
    powerP2 = 30
    freqP2 = 150
    speedP2 = 50000
    yStartP2 = 2800
    distanceBetweenP2Lines = 20
    
    ''' Paramters For P3 '''
    powerP3 = 8
    freqP3 = 20
    speedP3 = 50000
    yStartP3 = 2430
    distanceBetweenFirstAndSecondP3Line = 2570 - 2430
    distanceBetweenSecondAndThirdP3Line = 3300 - 2570
    
    ''' Paramters For P3 CutOffLine'''
    startCutOff = (xStart, -2500)
    endCutOff = (xEnd, -2500)
    powerCutOff = powerP3
    freqCutOff = freqP3
    speedCutOff = speedP3
    
    ''' Cell duplication parameters '''
    distanceBetweenCells = 5000
    numberOfCells = 5
    
    ''' First create one cell and store all the lines in one array '''
    singleCellLines = []
    
    ''' Create P1 Line '''
    singleCellLines.append(LaserLine((xStart, yStartP1), (xEnd, yStartP1), powerP1, freqP1, speedP1))
    
    ''' Create P2 Lines '''
    for i in range(0, 5):
        singleCellLines.append(LaserLine((xStart, yStartP2 + i * distanceBetweenP2Lines), (xEnd, yStartP2 + i * distanceBetweenP2Lines), powerP2, freqP2, speedP2))
        
    ''' Alternative
    startLine = LaserLine((xStart, yStartP1), (xEnd, yEnd), powerP2, freqP2, speedP2)
    singleCellLines.append(startLine)
    for i in range(1, 5):
        nextLine = startLine.createCopy((0, i * distancenBetweenP2Lines))
        singleCellLines.append(nextLine)
    '''
        

    ''' Create P3 Lines '''
    firstLineP3 = LaserLine((xStart, yStartP3), (xEnd, yStartP3), powerP3, freqP3, speedP3)
    ''' Alternative
    firstLineP3 = LaserLine()
    firstLineP3.start = (xStart, yStartP3)
    firstLineP3.end = (xEnd, yStartP3)
    firstLineP3.power = powerP3
    firstLineP3.frequency = freqP3
    firstLineP3.speed = speedP3
    '''
    
    secondLineP3 = firstLineP3.createCopy((0, distanceBetweenFirstAndSecondP3Line))
    thridLineP3 = secondLineP3.createCopy((0, distanceBetweenSecondAndThirdP3Line))
    singleCellLines.append(firstLineP3)
    singleCellLines.append(secondLineP3)
    singleCellLines.append(thridLineP3)
    
    
    ''' Create an array that contains all lines that should be lasered. '''
    allLaserLines = []
    
    ''' There are better ways, but this not just adds the first cell
        and then all others but creates 5 new cells from the single cell and adds them'''
    for i in range(0, numberOfCells):
        ''' this duplicates the single cell with a translation vector provided as parameter.
            The first cell has no translation and thus is just the untranslated single cell (i = 0) '''
        currentCell = Elements.Utils.duplicateLineArray(singleCellLines, (0, i * distanceBetweenCells))
        
        ''' now add every line of the new cell to allLaserLines'''
        for line in currentCell:
            allLaserLines.append(line)

    ''' Add the n + 1 part cell '''
    ''' Don't forget that there is also a p1 line that belongs to this cell'''
    allLaserLines.append(LaserLine((xStart, (distanceBetweenCells * numberOfCells) + yStartP1), (xEnd, (distanceBetweenCells * numberOfCells) + yStartP1), powerP1, freqP1, speedP1))
    ''' we can reuse the p3 lines '''
    allLaserLines.append(firstLineP3.createCopy((0, distanceBetweenCells * numberOfCells)))
    allLaserLines.append(secondLineP3.createCopy((0, distanceBetweenCells * numberOfCells)))
                         
    
    ''' Now add the lower cut off p3 line '''
    allLaserLines.append(LaserLine(startCutOff, endCutOff, powerCutOff, freqCutOff, speedCutOff))
    
    ''' Add a fiducial '''
    fiducial = LaseredFiducial((-5000, -5000));
    
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
    
    
    
    ''' show a very rudimantary graphical represenation ( will be moved to a matplotlib plot... )'''
    #GraphicalRepresentations.Canvas.showLines(allLaserLines)
    
    ''' save the file if you want '''
    filename = raw_input("If you want to save the file, provide a filename:\n")
    if filename != '':
        Utils.saveScript(laserScript,filename)
    

                                                                                                
