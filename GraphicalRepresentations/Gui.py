'''
Created on 21.05.2017

@author: jasch
'''
from Tkinter import *

class InputForm(object):
    '''
    Creates a basic TKinter gui with specified input fields. The answers are saved in an array ordered the way the fields are provided.
    '''


    def __init__(self, dictonary): 
        '''
        Constructor
        '''
        self.root = Tk();
        '''self.frame = Frame(width="500",height="800")
        self.frame.pack()
        self.swin = ScrolledWindow(self.frame, width=500, height=800)
        self.swin.pack()'''
        self.swin = self.root;
        
        self.initialDictonary = dictonary;
        
        self.keyEntryDictonary = {};
        
        self.savedDictonary = {};
        
        self.rows = 0;
        self.entryFields = [];
        self.fieldValues = [];
        self.defaultValues = [];
        self.isOk = False;
        for key in dictonary:
            entryField = self._createInputForm(key);
            entryField.insert(0, str(dictonary[key]));
            self.keyEntryDictonary[key] = entryField;
            
        
        Button(self.swin, text="Cancel", command=self._cancelCall).grid(row=self.rows, column=1, padx=20, pady=50, columnspan = 1, sticky='WE');
        Button(self.swin, text="Ok", command=self._okCall).grid(row=self.rows, column=2, padx=20, pady=50, columnspan = 1, sticky='WE');
        
        
    def open(self):
        mainloop();
        return self.isOk;
    
    def getDictonary(self):
        return self.savedDictonary;
    
    def _createInputForm(self, field):
        Label(self.swin, text=field).grid(row=self.rows, column=1, padx=20, pady=0);
        entryField = Entry(self.swin);
        entryField.grid(row=self.rows, column=2, padx=20, pady=0);
        self.entryFields.append(entryField);
        self.rows += 1
        return entryField;
        
    def _okCall(self):
        
        self._saveFields();
        self.root.destroy();
        self.isOk = True;
    
    def _cancelCall(self):
        self.root.destroy();
        self.isOk = False;
    
    def _saveFields(self):
        for key in self.keyEntryDictonary:
            self.savedDictonary[key] = int(self.keyEntryDictonary[key].get());