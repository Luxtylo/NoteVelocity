"""The main UI file of my note-taking program"""

## Imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import os
import datetime

## Initialise NoteApp class
class NoteApp:

	## Constructor
	def __init__ (self, master):
		self.tabList = []

		self.noteBook = ttk.Notebook(master, height = 20)
		self.noteBook.enable_traversal()

		fileName = "blob.txt"
		nextTab = "Tab(master, \"" + fileName + "\")"
		self.tabList.append(eval(nextTab))

		fileName = "Test.note"
		nextTab = "Tab(master, \"" + fileName + "\")"
		self.tabList.append(eval(nextTab))

		self.counter = range(len(self.tabList))
		for i in self.counter:
			self.noteBook.add(self.tabList[i])

		self.noteBook.pack(side = TOP, expand = 1, fill = BOTH)

# Tab class for adding to notebook
class Tab(Text):
	def __init__(self, master, title):
		Text.__init__(self, master, bg = '#FFFFFF', fg = '#404040', padx = 10, pady = 10, wrap = 'word')
		self.name = title


## STARTING

# Root widget
root = Tk()

# Root widget properties
root.title("New Note - NoteVelocity") # Title in window title bar
root.minsize(640,400) # Minimum size of window
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(2, weight = 0)

# Set initial size to take up 3/4 of the screen for resolutions up to 1024x768
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

if screenWidth <= 1024 and screenHeight <= 768:
	windowWidth = 3 * screenWidth / 4
	windowHeight = 3 * screenHeight / 4
	# windowSizeString = str(windowWidth) + "x" + str(windowHeight)
	root.geometry("+%d+%d" % (windowWidth, windowHeight))

# Otherwise window size is 800x600
else:
	root.geometry("800x600")

# New instance of NoteApp
app = NoteApp(root)

# Call root widget's main loop
root.mainloop()
