'''
Created on 16.05.2017

This allows for showing Element.Shapes on a canvas

@author: Jascha Riedel
'''

from Tkinter import *

def showLines(lines):
    
    pixelsPerUm = 0.03
    
    root = Tk();
    
    canvas = Canvas(root, width = 1200, height = 1000)
    canvas.pack()
    for line in lines:
        red = "%0.2X" % (line.power * 182 % 255)
        green = "%0.2X" % (line.frequency *531  % 255)
        blue = "%0.2X" % (line.speed  % 255)
        canvas.create_line(line.start[0] * pixelsPerUm, line.start[1] * pixelsPerUm, line.end[0] * pixelsPerUm, line.end[1] * pixelsPerUm, fill="#" + red + green + blue)
        
    mainloop()
    
    
    
    
    
    
    
    
    

