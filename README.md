# at.sunplugged.printschemes.python


# Overview

## Structure

The project may be seen as a framework providing different functions and classes to create python scripts that in turn create scripts to operate machines.

**The used unit is micrometer if not explicitly specified.**


### Elements.Shapes

This package contains shapes that should be used. Currently there exists *Line* and *Rectangle* as basic shapes and all other shapes should be decendendts of that basic shapes *(i. e. LaserLine extends Line)*. See the classes for short explanations.

### Elements.Utils

Contains utility functions that are useful in combination with Elements.Shapes

### ScriptAlgorithms.laserLineAlgorithm

Contains a useful function **createScriptFromLaserLinesWithExplicitNullPoint(laserLines, nullX, nullY)** that may be used to generate a script for lasering. The first parameter should be **list** of **LaserLines**. The function returns a String that is the script.

### GraphicalRepresentations

This packages contains all modules that should be used for graphical representations.

#### matplotlibRepresentation

To use this module you need to install matplotlib. If you are on windows and python is in your PATH variable use: 
* python -m pip install setuptools
* python -m pip install matplotlib

and you are good to go.

Currently the module contains one class **matplotCanvas(lines, rectangles)** and only draws the **lines** (actually currently only **LaserLines**!). You can add lines or **LineGroups** later via *addLine(line)* and *addLineGroup(group)*.
Use the function *plot* to draw the lines. A window is openend containing the plot.

#### Gui

This is a simple Tkinter graphical user interface that allows the input of different parameters. 
The module contains a single class **InputForm**. On creation you provide as parameter a dictionary in the form {"Value Name 1": defaultValue1, ... , "Value Name N": defaultValueN}

*i. e. parameters = {"powerP1": 45, "freqP1": 35, ...}*

The Gui will contain an inputfield for every entry in the dictionary. With the function *open()* the gui is openend and when closed the function will return either **True(ok clicked)** or **False(cancel clicked or Red X)**.
You can now get your dictonary back by calling *getDictonary()*.

