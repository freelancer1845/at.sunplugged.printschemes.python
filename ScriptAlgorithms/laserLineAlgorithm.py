'''
Created on 29.04.2017

@author: jasch
'''

import Elements.Shapes
from operator import attrgetter


def intialCommands():
    return '6;LACT\n3;ALLIGN;1500;-0.215\n0;NULL;16000;117000\n'

    
def startingPointExplicit(nullX, nullY):
    startingPointText = []
    startingPointText.append('*-----Starting Point-----*\n')
    startingPointText.append('0;NULL;' + str(nullX) + ';' + str(nullY) + '\n')
    return ''.join(startingPointText)

def groupLaserLinesByPower(sortedLaserLines):
    iterator = iter(sortedLaserLines)
    currentPower = 0
    currentFrequency = 0
    groupList = []
    try:
        currentLine = iterator.next()
        currentPower = currentLine.power
        currentFrequency = currentLine.frequency
        group = [currentLine]
        while(True):
            try:
                currentLine = iterator.next()
                if currentLine.power == currentPower and currentLine.frequency == currentFrequency:
                    group.append(currentLine)
                else:
                    groupList.append(group)
                    group = [currentLine]
                    currentPower = currentLine.power
                    currentFrequency = currentLine.frequency
            except StopIteration:
                if len(group) > 0:
                    groupList.append(group)
                break
    except StopIteration:
        raise ValueError('No laser line to sort...')
    
    return groupList
                        
    

def createPowerHeader(group):
    laserLine = group[0]
    return '*-----Setting new power-----Power:' + str(laserLine.power) + '---Frequency:' + str(laserLine.frequency) + '-----*\n6;LPAR;' + str(laserLine.power) + ';' + str(laserLine.frequency) + '\n'


def createLaseringScript(group):
    script = []
    sortedByYStart = sorted(group, key=_getYStartFromLaserLine)
    previousX = 0
    for line in sortedByYStart:
        distanceXStart = abs(line.start[0] - previousX)
        distanceXEnd = abs(line.end[0] - previousX)
        if (distanceXEnd < distanceXStart):
            script.append('0;LASERNXY;{};{};{};{};{}\n'.format(str(int(line.end[0])), str(int(line.start[1])), str(int(line.start[0])), str(int(line.end[1])), str(int(line.speed))))
            previousX = int(line.start[0])
        else:
            script.append('0;LASERNXY;{};{};{};{};{}\n'.format(str(int(line.start[0])), str(int(line.start[1])), str(int(line.end[0])), str(int(line.end[1])), str(int(line.speed))))
            previousX = int(line.end[0])
    
    return ''.join(script)

def _getYStartFromLaserLine(laserLine):
    return laserLine.start[1]

def createFinish():
    script = []
    script.append('*----- Finish -----*\n')
    script.append('*---Coming Home---*\n')
    script.append('0;PAY;100000;100000\n')
    script.append('0;ERR\n')
    return ''.join(script)
    


def createScriptForLaserLineGroup(group):
    script = []
    script.append(createPowerHeader(group))
    script.append(createLaseringScript(group))
    
    return "".join(script)

def createLaserScriptFromLaserLines(laserLines):
    script = []
    laserLines = sorted(laserLines, key=attrgetter('power', 'frequency'), reverse=True)
    groupedLines = groupLaserLinesByPower(laserLines)
    for group in groupedLines:
        script.append(createScriptForLaserLineGroup(group))
    return ''.join(script)

def createScriptFromLaserLinesWithExplicitNullPoint(laserLines, nullX, nullY):
    if isinstance(laserLines, list) == False:
        raise ValueError('laserLines must be list like structure!')
    for line in laserLines:
        if isinstance(line, Elements.Shapes.LaserLine) == False:
            raise ValueError('All lines must be LaserLines!')
            
    script = []
    
    '''Creates the header of the script'''
    script.append('*---------------Python created script for lasering sunplugged.at. Created by Jascha Riedel---------*\n')
    script.append(intialCommands())
    
    ''' Create starting point (null point)'''
    script.append(startingPointExplicit(nullX, nullY))
    
    ''' Create the laser lines. This is the actual complex alogirthm'''
    script.append(createLaserScriptFromLaserLines(laserLines))
    
    script.append(createFinish())
    
    return "".join(script)

    
    
