'''
Created on 21.05.2017

@author: jasch
'''
import matplotlib.pyplot as matPlot
import matplotlib.patches as mpatches
import Elements



class matplotCanvas():
    def __init__(self, lines=[], rectangles=[]):
        self.lines = lines;
        self.rectangles = rectangles;
        self.nullX = 0;
        self.nullY = 0;
        self.maxpower = 0;
        self.maxfreq= 0;
        self.maxspeed = 0;
        self.laserLineColors = [];
        self.patches = [];
    
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
        if isinstance(group, Elements.Utils.LineGroup) == False:
            raise ValueError('Group must be of type Elements.Utils.LineGroup');
        for line in group.lines:
            self.addLine(line);
            
            

    def plot(self):
        self._createPlot();
        matPlot.show();
        
    def _createPlot(self):
        self._destoyPlot();
        
        for line in self.lines:
            if isinstance(line, Elements.Shapes.LaserLine) == True:
                self._processLaserLine(line);
        
        matPlot.legend(handles=self.patches, loc=1);
        
        
    def _destoyPlot(self):
        matPlot.close();
        self.maxfreq = 0;
        self.maxpower = 0;
        self.maxspeed = 0;
        self.laserLineColors = [];
        
    def savePlot(self, filename):
        self._createPlot();
        matPlot.axis('off')
        matPlot.savefig(filename, dpi=2540)
        
    
    
    def _processLaserLine(self, line):
    
        for line in self.lines:
            if self.maxpower < line.power:
                self.maxpower = line.power;
            if self.maxfreq < line.frequency:
                self.maxfreq = line.frequency;
            if self.maxspeed < line.speed:
                self.maxspeed = line.speed;
        
        for line in self.lines:
            red = "%0.2X" % (line.power / float(self.maxpower) * 255)
            green = "%0.2X" % (line.frequency / float(self.maxfreq) * 255)
            blue = "%0.2X" % (line.speed / float(self.maxspeed) * 255)
            if red + green + blue not in self.laserLineColors:
                self.laserLineColors.append(red + green + blue)
                self.patches.append(mpatches.Patch(color='#' + red + green+ blue, label='Laser ' + str(line.power)))
            
            matPlot.plot([line.start[0], line.end[0]], [line.start[1], line.end[1]], color="#" + red + green + blue);

    

