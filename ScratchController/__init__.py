'''
Interface to the Scratching Machine.

Created on 20.06.2017

@author: Jascha Riedel

'''

import pyads as twin
from pyads.testserver import AdsTestServer


adr = None;


def init():
    '''
        Connects to the TWINCat Ads
    '''
    print('Opened connection to ads server with port: ' + str(twin.open_port()))
    adr = twin.AmsAddr(twin.get_local_address())
    
    
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
    
    testServer.stop();
    
    



