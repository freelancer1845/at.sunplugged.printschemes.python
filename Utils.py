'''
Created on 16.05.2017
Some utils a that may be used in different scripts.

@author: Jascha Riedel
'''


def saveScript(script, filename):
    try:
        with open(filename, 'w') as fileHandle:
            fileHandle.write(script)
    except IOError:
        print('Error while saving script', IOError)