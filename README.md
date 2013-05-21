Note-taking project
===================

An EPQ project for designing and making a note-taking program for university and A-level students. My aim is to have syntax like markdown and Python, but functionality like LaTeX.
Made using *Python* and *Tkinter*.

UI is currently **less than semi-functional**

Function is currently **WIP**

*Source/Functionality/Syntax.txt* describes syntax. It is also available in *Source/Functionality/Notes/Syntax.note*

*InitialStructurePlan.txt* contains my initial plan of the structure of the program. It will change as I code the program.

As of 2013/05/08, */Source/Functionality/function.py* will take the input from */Source/Functionality/Notes* and make the file specified. *.html* extension is recommended, although anything which can contain html tags and be opened by a browser will work.
Input is corrected if no file extension is given (or currently, if there's no extension less than 5 characters long. This currently stops it working with filenames of less than 5 characters.)


**Dependencies:**
* *Python* >= *3.3*, as of commit 47
* tkinter *(Included with Python on Windows and Mac)*
