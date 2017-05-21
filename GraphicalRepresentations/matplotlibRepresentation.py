'''
Created on 21.05.2017

@author: jasch
'''
import matplotlib.pyplot as matPlot
import Elements


class matplotCanvas():
    def __init__(self, lines=[], rectangles=[]):
        self.lines = lines;
        self.rectangles = rectangles;
        self.nullX = 0;
        self.nullY = 0;
    
    @property
    def lines(self):
        return self.lines;
    
    @lines.setter
    def lines(self, lines):
        if any([isinstance(line, Elements.Shapes.Line) for line in lines]) == False:
            raise ValueError('Lines must be of type Elements.Shapes.Line');
        self.lines = lines
        
    @property
    def rectangles(self):
        return self.rectangles;
     
    @rectangles.setter
    def rectangles(self, rectangles):
        if any([isinstance(rectangle, Elements.Shapes.Rectangle) for rectangle in rectangles]) == False:
            raise ValueError('Rectangles must be of type Elements.Shapes.Rectangle!');
        self.rectangles = rectangles;
    
    def addLine(self, line):
        if isinstance(line, Elements.Shapes.Line) == False:
            raise ValueError('Line must be of type Elements.Shapes.Line');
        self.lines.append(line);
    
    def removeLine(self, line):
        self.lines.remove(line);
        
    def addLineGroup(self, group):
        if isinstance(group, Elements.Shapes.LineGroup) == False:
            raise ValueError('Group must be of type Elements.Utils.LineGroup');
        for line in group.lines:
            self.addLine(line);
            
            

    def plot(self):
        self._createPlot();
        matPlot.show();
        
    def _createPlot(self):
        matPlot.close();
        maxpower = 0
        maxfreq = 0
        maxspeed = 0
        for line in self.lines:
            if maxpower < line.power:
                maxpower = line.power;
            if maxfreq < line.frequency:
                maxfreq = line.frequency;
            if maxspeed < line.speed:
                maxspeed = line.speed;
        print(maxpower, maxfreq, maxspeed)
        
        for line in self.lines:
            red = "%0.2X" % (line.power / float(maxpower) * 255)
            green = "%0.2X" % (line.frequency / float(maxfreq) * 255)
            blue = "%0.2X" % (line.speed / float(maxspeed) * 255)
        
            matPlot.plot([line.start[0], line.end[0]], [line.start[1], line.end[1]], color="#" + red + green + blue);
        
        
    def savePlot(self, filename):
        self._createPlot();
        matPlot.axis('off')
        matPlot.savefig(filename, dpi=2540)
        
        
    

