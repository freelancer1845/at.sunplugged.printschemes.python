'''

OpenCV interface for detecting fiducials in camera shots.

Created on 20.06.2017

@author: Jascha Riedel

'''
import numpy as np
import cv2


def loadImageFromFile(png):
    return cv2.imread(png, 0)


if __name__ == '__main__':
    img = loadImageFromFile('test.png')
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

