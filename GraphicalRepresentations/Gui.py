'''
Created on 21.05.2017

@author: jasch
'''
from Tkinter import *
from tkinter.tix import *

class InputForm(object):
    '''
    Creates a basic TKinter gui with specified input fields. The answers are saved in an array ordered the way the fields are provided.
    '''


    def __init__(self, *fields): 
        '''
        Constructor
        '''
        self.root = Tk();
        '''self.frame = Frame(width="500",height="800")
        self.frame.pack()
        self.swin = ScrolledWindow(self.frame, width=500, height=800)
        self.swin.pack()'''
        self.swin = self.root;
        
        
        self.rows = 0;
        self.entryFields = [];
        self.fieldValues = [];
        self.defaultValues = [];
        self.isOk = False;
        for field in fields:
            self._createInputForm(field);
        
        Button(self.swin, text="Cancel", command=self._cancelCall).grid(row=self.rows, column=1, padx=20, pady=50, columnspan = 1, sticky='WE');
        Button(self.swin, text="Ok", command=self._okCall).grid(row=self.rows, column=2, padx=20, pady=50, columnspan = 1, sticky='WE');
        
        
    def open(self):
        mainloop();
        return self.isOk;
    
    def setDefaultValues(self, values):
        index = 0;
        for value in values:
            self.entryFields[index].insert(0, str(value));
            index += 1;
    
    def _createInputForm(self, field):
        Label(self.swin, text=field).grid(row=self.rows, column=1, padx=20, pady=0);
        entryField = Entry(self.swin);
        entryField.grid(row=self.rows, column=2, padx=20, pady=0);
        self.entryFields.append(entryField);
        self.rows += 1
        
    def _okCall(self):
        
        self._saveFields();
        self.root.destroy();
        self.isOk = True;
    
    def _cancelCall(self):
        self.root.destroy();
        self.isOk = False;
    
    def _saveFields(self):
        for entry in self.entryFields:
            self.fieldValues.append(entry.get());