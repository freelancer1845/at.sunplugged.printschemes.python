'''
Interface to the Scratching Machine.

Created on 20.06.2017

@author: Jascha Riedel

'''

import pyads as twin
from pyads.testserver import AdsTestServer
import TWINCatConfig
from enum import Enum
import logging

adr = twin.AmsAddr()

class Properties(Enum):
    RoationSpeed = 0
    Force = 1


def getLocationInPlane():
    '''
        Gets the X and Y position of the robot and returns it in a tuple.
    '''
    logging.debug('Getting location in plane')
    return (0.0, 0.0)
    
def moveToLocation(newLocation , speed):
    '''
        Moves the robot to the designated Location.
    '''
    if isinstance(newLocation, (tuple, list)) is False:
        raise ValueError('NewLocation must be a tuple or list!')
    if all(isinstance(x, float) for x in newLocation) is False:
        raise ValueError('NewLocation must be float like')
    if isinstance(speed, float) is False:
        raise ValueError('Speed must be a float')

    logging.debug('Moving Tip')
    # Actual moving...
    
def lowerTip():
    logging.debug('Lowering tip')
    # TODO : Implement

def raiseTip():
    logging.debug('Raising tip')
    # TODO : Implement
    
def setRotationSpeed(value):
    logging.debug('Setting RotationSpeed to value: ' + str(value))
    # TODO : Implement

def getRotationSpeed():
    logging.debug('Getting Rotation Speed')
    # TODO : Implement
    return 0

def setForce(value):
    logging.debug('Setting Force to value: ' + str(value))
    # TODO : Implement

def getForce():
    logging.debug('Getting Force')
    # TODO : Implement
    
def setProperty(key, value):
    if isinstance(key, Properties) is False:
        raise ValueError('Key must be from the Properties Enum!')
    
    if key is Properties.RoationSpeed:
        setRotationSpeed(value)
    elif key is Properties.Force:
        setForce(value)
 
def getProperty(key):
    if isinstance(key, Properties) is False:
        raise ValueError('Key must be from the Properties Enum!')
    if key is Properties.RoationSpeed:
        getRotationSpeed()
    elif key is Properties.Force:
        getForce()
    

def init():
    '''
        Connects to the TWINCat Ads
    '''
    print('Opened connection to ads server with port: ' + str(twin.open_port()))
    print(twin.get_local_address().toString())
    global adr;
    adr = twin.get_local_address()
    twin.add_route(adr, TWINCatConfig.ams_address)
    
    
def tests():
    twin.write_by_name(adr, 'testbool', True, twin.PLCTYPE_BOOL)
    twin.read_by_name(adr, 'testbool', twin.PLCTYPE_BOOL)
    
    
    
    
if __name__ == '__main__':
    '''
        test routine
    '''
    
    testServer = AdsTestServer()
    
    testServer.start();
    
    init()
    tests()
    
    raw_input('Finish...')
    testServer.stop();
    
    



