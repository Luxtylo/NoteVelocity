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

		# Ttk Notebook code:
		"""self.tabList = []

		self.noteBook = ttk.Notebook(master, height = 20)
		self.noteBook.enable_traversal()

		fileName = "blob.txt"
		self.nextTab = "Tab(master, \"" + fileName + "\")"
		self.tabList.append(eval(self.nextTab))

		fileName = "Test.note"
		self.nextTab = "Tab(master, \"" + fileName + "\")"
		self.tabList.append(eval(self.nextTab))

		self.counter = range(len(self.tabList))
		for i in self.counter:
			self.noteBook.add(self.tabList[i], text = self.tabList[i].name)

		self.noteBook.pack(side = TOP, expand = 1, fill = BOTH)"""

		self.upperBox = Frame(master, bg = "#FFFF00")
		self.upperBox.pack(expand = 1, fill = BOTH)

		self.tabBar = TabBar(master)

		self.tabBar.add("PlaceNameDoodymajig.py")
		self.tabBar.add("Thingy.py")
		
		self.tabBar.show()


# TabContents class for adding to Tab
class TabContents(Text):

	# Constructor
	def __init__(self, master):

		# Initialise text area
		Text.__init__(self, master, bg = '#FFFFFF', fg = '#404040', padx = 10, pady = 10, wrap = 'word')

# Tab class for adding to TabBar
class Tab(Frame):

	# Constructor
	def __init__(self, master, title):

		# Initialise frame and internal frame
		Frame.__init__(self, master, bg = "#00FF00", width = "200", height = 24)
		self.subFrame = Frame()
		self.subFrame.pack(side = LEFT, padx = 5)

		# Set location and title
		self.location = title
		splitName = title.split("/")
		self.title = splitName[-1]

		# If title is longer than 15 chars, shorten it. Otherwise do nothing
		if len(self.title) > 15:
			self.title = self.title[:15]

		# Create instance of TabContents
		self.textBox = TabContents(master)

		# Create tab's widgets, overlaying them using the place manager
		# Tab Label
		self.Label = Label(self.subFrame, text = self.title)
		self.Label.pack(side = LEFT, expand = 0, fill = X)

		# Tab close button
		self.CloseButton = ttk.Button(self.subFrame, text = "X", width = 0)
		self.CloseButton.pack(side = RIGHT, expand = 0)

		# Tab unsaved indicator
		self.tabSaved = Frame(self.subFrame, width = 8, height = 8, bg = "#0000FF")
		self.tabSaved.pack(side = RIGHT, padx = 5)

# TabBar Class
class TabBar(Frame):

	# Constructor
	def __init__(self, master):

		# Initialise frame
		Frame.__init__(self, master, bg = '#FF0000')

		# Initialise tab list
		# want to set it so that when you put in the tab number, you get the tab out
		# eg self.tabList[0] = tab
		self.tabList = []

		# Initialise other variables
		self.currentTab = 0

	def show(self):
		# Pack to bottom. For integration in actual thing, fill should be change to XY.
		self.pack(side = BOTTOM, expand = 0, fill = X)

	def add(self, tabLocation):
		# Initialise variable newTab as added Tab instance
		newTab = Tab(self, tabLocation)

		# Set currentTab to be the last one
		# New tab will always be at the end
		self.currentTab = len(self.tabList)

		# Append tabList with new tab
		self.tabList.append(newTab)


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
