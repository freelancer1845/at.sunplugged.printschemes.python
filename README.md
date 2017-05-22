# at.sunplugged.printschemes.python


# Overview

## Structure

The project may be seen as a framework providing different functions and classes to create python scripts that in turn create scripts to operate machines.

** The used unit is micrometer if not explicitly specified. **


### Elements.Shapes

This package contains shapes that should be used. Currently there exists *Line* and *Rectangle* as basic shapes and all other shapes should be decendendts of that basic shapes *(i. e. LaserLine extends Line)*. See the classes for short explanations.

### Elements.Utils

Contains utility functions that are useful in combination with Elements.Shapes

### ScriptAlgorithms.laserLineAlgorithm

Contains a useful function **createScriptFromLaserLinesWithExplicitNullPoint(laserLines, nullX, nullY)** that may be used to generate a script for lasering. The first parameter should be **list** of **LaserLines**. The function returns a String that is the script.
