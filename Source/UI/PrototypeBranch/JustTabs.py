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

		self.tabBar = TabBar(master)

		self.tabBar.add("PlaceNameDoodymajig.py")
		self.tabBar.add("Thingy.py")

		self.updateTextBoxes()
		
		self.tabBar.show()

	def updateTextBoxes(self):
		currentTab = self.tabBar.currentTab
		previousTab = self.tabBar.previousTab

		self.tabBar.tabList[previousTab].textBox.pack_forget()
		self.tabBar.tabList[currentTab].textBox.pack(side = TOP, expand = 1, fill = X)		


# TabContents class for adding to Tab
class TabContents(Text):

	# Constructor
	def __init__(self, master):

		# Initialise text area
		Text.__init__(self, master, bg = '#FFFFFF', fg = '#404040', padx = 10, pady = 10, wrap = 'word')

# Tab class for adding to TabBar
class Tab(Frame):

	# Constructor
	def __init__(self, master, title, number):

		# Initialise frame and internal frame
		Frame.__init__(self, master, bg = "#000000", width = "200", height = 24)
		self.subFrame = Frame()
		self.subFrame.pack(side = LEFT, padx = 5, ipadx = 0, ipady = 2)
		self.subSubFrame = Frame(self.subFrame)
		self.subSubFrame.pack(side = LEFT, padx = 2)
		self.subSubFrame.bind("<Button-1>", lambda event: master.switchToTab(self.Num))

		# Set tab number
		self.Num = number

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
		self.Label = Label(self.subSubFrame, text = self.title)
		self.Label.pack(side = LEFT, expand = 0, fill = X, padx = 5)
		self.Label.bind("<Button-1>", lambda event: master.switchToTab(self.Num))

		# Tab close button
		self.CloseButton = ttk.Button(self.subSubFrame, text = "X", width = 0)
		self.CloseButton.pack(side = RIGHT, expand = 0)
		self.CloseButton.bind("<Button-1>", lambda event: master.close(self.Num))

		# Tab unsaved indicator
		self.tabSaved = Frame(self.subSubFrame, width = 8, height = 8, bg = "#00FF00")
		self.tabSaved.pack(side = RIGHT, padx = 5)

# TabBar Class
class TabBar(Frame):

	# Constructor
	def __init__(self, master):

		# Initialise frame
		Frame.__init__(self, master)

		# Initialise tab list
		# want to set it so that when you put in the tab number, you get the tab out
		# eg self.tabList[0] = tab
		self.tabList = []

		# Initialise other variables
		self.currentTab = 0
		self.previousTab = 0

	def show(self):
		# Pack to bottom. For integration in actual thing, fill should be change to XY.
		self.pack(side = BOTTOM, expand = 0, fill = X)

		self.currentTab = 0
		self.switchToTab(0)

	def add(self, tabLocation):

		# Set currentTab to be the last one
		# New tab will always be at the end
		self.previousTab = self.currentTab
		self.currentTab = len(self.tabList)

		# Initialise variable newTab as added Tab instance
		newTab = Tab(self, tabLocation, self.currentTab)

		# Append tabList with new tab
		self.tabList.append(newTab)

		self.switchToTab(self.currentTab)

	def switchBy(self, number):
		check = self.currentTab + number
		if check != 1 and check != -1:
			# Throw error here - this should not happen
			pass
		else:
			currentTab = self.currentTab + number
			self.switchToTab(currentTab)

	def switchToTab(self, index):
		# Set old tab to previous tab and new to index
		self.previousTab = self.currentTab
		self.currentTab = index

		# Make aesthetic changes 
		self.tabList[self.previousTab].subFrame.config(bg = "#FFFFFF")
		self.tabList[self.currentTab].subFrame.config(bg = "#FF0000")

		# Update text box showing
		self.updateTextBoxes

	def close(self, index):
		# If it's not the current tab
		if index != self.currentTab:
			self.tabList[index].pack_forget()
			self.tabList[index].textBox.pack_forget()

		# If it is the current tab, and it's not the 0th tab
		elif len(self.tabList) > 1 and index != 0:
			self.switchToTab(index - 1)
			self.tabList[index].pack_forget()
			self.tabList[index].textBox.pack_forget()

		# If it is the current tab, and it is the 0th tab
		elif len(self.tabList) > 1 and index == 0:
			self.switchToTab(index + 1)
			self.tabList[index].pack_forget()
			self.tabList[index].textBox.pack_forget()

		# If it's the only tab
		else:
			self.add(self, "New Note")
			self.tabList[index].pack_forget()
			self.tabList[index].textBox.pack_forget()

	def updateTextBoxes(self):
		self.tabBar.tabList[self.previousTab].textBox.pack_forget()
		self.tabBar.tabList[self.currentTab].textBox.pack(side = TOP, expand = 1, fill = X)	

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
