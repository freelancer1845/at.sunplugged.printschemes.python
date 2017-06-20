'''
Created on 25.05.2017

This is the current minimal code example for creating the standard laserline script.

@author: Jascha Riedel
'''

from Elements.Utils import Group
from Elements.CompositeShapes import LaseredFiducial
from Elements.Shapes import LaserLine
from ScriptAlgorithms import laserLineAlgorithm
from GraphicalRepresentations import matplotlibRepresentation
from GraphicalRepresentations.Gui import InputForm
import Utils


if __name__ == '__main__':
    ''' First we define all the parameters and get them via a simple Tkinter interface '''
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
                  'distanceBetweenSecondAndThirdP3Line': 3300 - 2570,
                  'distanceBetweenSecondAndFourthP3Line': 3200 - 2570,
                  'yCutOff':-2500,
                  'powerCutOff': 8,
                  'freqCutOff': 20,
                  'speedCutOff': 50000,
                  'distanceBetweenCells': 5000,
                  'numberOfCells': 5,
                  'fiducialX':-5000,
                  'fiducialY':-5000,
                  'NumberofP2Lines':5}
    
    inputForm = InputForm(parameters)
    
    if inputForm.open() == True:
        parameters = inputForm.getDictonary();
        for key in parameters:
            print(key, parameters[key]);
    else:
        quit()
    
    
    ''' Everything is organized in this MainGroup '''
    
    mainGroup = Group();
    
    ''' Add the fiducial '''
    mainGroup.addElement(LaseredFiducial((parameters['fiducialX'], parameters['fiducialY'])))
    
    ''' Construct singel cell '''
    singleCellGroup = Group();
    ''' Add p1 line '''
    singleCellGroup.addElement(LaserLine((parameters['xStart'], parameters['yStartP1']),
                                        (parameters['xEnd'], parameters['yStartP1']),
                                        parameters['powerP1'],
                                        parameters['freqP1'],
                                        parameters['speedP1']));
    
    ''' Add p2 Lines '''                                    
    p2Lines = Group();
    for i in range(0, parameters['NumberofP2Lines']):
        p2Lines.addElement(LaserLine((parameters['xStart'], parameters['yStartP2'] + i * parameters['distanceBetweenP2Lines']),
                                    (parameters['xEnd'], parameters['yStartP2'] + i * parameters['distanceBetweenP2Lines']),
                                    parameters['powerP2'],
                                    parameters['freqP2'],
                                    parameters['speedP2']));
    
    singleCellGroup.addElement(p2Lines);
    
    ''' Add p3 Lines '''
    
    firstLineP3 = LaserLine((parameters['xStart'], parameters['yStartP3']),
                             (parameters['xEnd'], parameters['yStartP3']),
                              parameters['powerP3'], parameters['freqP3'], parameters['speedP3'])
    secondLineP3 = firstLineP3.createCopy((0, parameters['distanceBetweenFirstAndSecondP3Line']))
    thridLineP3 = secondLineP3.createCopy((0, parameters['distanceBetweenSecondAndThirdP3Line']))
    fourthLineP3 = secondLineP3.createCopy((0, parameters['distanceBetweenSecondAndFourthP3Line']))
    singleCellGroup.addElements([firstLineP3, secondLineP3, thridLineP3,fourthLineP3]);
    
    ''' add the n cells '''
    for i in range(0, parameters['numberOfCells']):
        mainGroup.addElement(singleCellGroup.createCopy((0, i * parameters['distanceBetweenCells'])));
    
    ''' add the n + 1 part cell '''
        
    ''' Don't forget that there is also a p1 line that belongs to this cell'''
    mainGroup.addElement(LaserLine((parameters['xStart'], (parameters['distanceBetweenCells'] * parameters['numberOfCells']) + parameters['yStartP1']),
                                    (parameters['xEnd'], (parameters['distanceBetweenCells'] * parameters['numberOfCells']) + parameters['yStartP1']),
                                     parameters['powerP1'], parameters['freqP1'], parameters['speedP1']));
    ''' we can reuse the p3 lines '''
    mainGroup.addElement(firstLineP3.createCopy((0, parameters['distanceBetweenCells'] * parameters['numberOfCells'])))
    mainGroup.addElement(secondLineP3.createCopy((0, parameters['distanceBetweenCells'] * parameters['numberOfCells'])))
                         
    
    ''' Now add the lower cut off p3 line '''
    mainGroup.addElement(LaserLine((parameters['xStart'], parameters['yCutOff']),
                                   (parameters['xEnd'], parameters['yCutOff']) ,
                                   parameters['powerCutOff'], parameters['freqCutOff'], parameters['speedCutOff']));
    
    ''' All lines that should be lasered are added now. To make changes just change the parameters. For Example distance between cells'''
    
    ''' This uses the ScriptAlgorithm to create the laserlinesscript '''
    nullX = 15000
    nullY = -15000
    laserScript = laserLineAlgorithm.createScriptFromLaserLinesWithExplicitNullPoint(mainGroup.getAllElementsOfType(LaserLine), nullX, nullY)
    print (laserScript)
    
    
    ''' this creates a simple matplotlib representation '''
    canvas = matplotlibRepresentation.matplotCanvas([mainGroup]);
    
    
    canvas.plot();
    
    
    ''' save the file if you want '''
    filename = raw_input("If you want to save the script, provide a filename:\n")
    if filename != '':
        Utils.saveScript(laserScript,filename)
    
    
    
    
    
    
    
    
