'''
Created on 21.05.2017

@author: jasch
'''
import matplotlib.pyplot as matPlot
import matplotlib.patches as mpatches
import Elements



class matplotCanvas(Elements.Utils.Group):
    '''
        The matplotCanvas is a descendant of Elements.Utils.Group since it consists out of Elements.
    '''
    def __init__(self, elements = None):
        super(matplotCanvas, self).__init__(elements);
        
        self.nullX = 0;
        self.nullY = 0;
        
        ''' Variables for finding colors of laserLines '''
        self.maxpower = 0;
        self.maxfreq= 0;
        self.maxspeed = 0;
        self.laserLineColors = [];
        self.patches = [];

    def plot(self):
        self._createPlot();
        matPlot.show();
        


    
    def _createPlot(self):
        self._destoyPlot();
        
        self._processLaserLines();
        
        for line in self.getAllElementsOfType(Elements.Shapes.LaserLine):
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
    
    
    def _processLaserLines(self):
        laserLines = self.getAllElementsOfType(Elements.Shapes.LaserLine);
        ''' find max values for color generation '''
        for line in laserLines:
            if self.maxpower < line.power:
                self.maxpower = line.power;
            if self.maxfreq < line.frequency:
                self.maxfreq = line.frequency;
            if self.maxspeed < line.speed:
                self.maxspeed = line.speed;
    
        ''' Now process each line'''
        for line in laserLines:
            self._processLaserLine(line);
            
        
    
    def _processLaserLine(self, line):
        red = "%0.2X" % (line.power / float(self.maxpower) * 255)
        green = "%0.2X" % (line.frequency / float(self.maxfreq) * 255)
        blue = "%0.2X" % (line.speed / float(self.maxspeed) * 255)
        if red + green + blue not in self.laserLineColors:
            self.laserLineColors.append(red + green + blue)
            self.patches.append(mpatches.Patch(color='#' + red + green+ blue, label='Laser ' + str(line.power) + ";" + str(line.frequency) + ";" + str(line.speed)))
        
        matPlot.plot([line.start[0], line.end[0]], [line.start[1], line.end[1]], color="#" + red + green + blue);

    

