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

		# Initialise log at log.txt
		self.logLocation = "log.txt"
		self.Log = logFile(self.logLocation)

		# Initialise variables
		self.openLocation = None
		self.inputFile = None
		self.outputFilename = None

		# Initialise show variables
		self.showFormFrame = True
		self.showMenuBar = True
		self.showTabBar = True

		# Initialise styles
		self.styleMode = 0
		self.initStyles()

		# Initialise tab stuff
		tabs = list()

		# Initialise key bindings
		self.keyBindings(master)

		self.Log.write("\tInitialised variables, styles and keybindings")		

		# Create upper level 2 frame (Text + Formatting)
		self.textFormFrame = ttk.Frame(root, name = "textFormFrame")
		self.textFormFrame.pack(fill = BOTH, side = TOP, expand = 1)

		# Create left level 3 frame (Text)
		self.textFrame = ttk.Frame(self.textFormFrame, name = "textFrame")
		self.textFrame.pack(fill = BOTH, expand = 1, side = LEFT)

		if self.showFormFrame == True:
			# Create right level 3 frame (Formatting)
			self.formFrame = ttk.Frame(self.textFormFrame, style = "FS.TFrame")
			self.formFrame.pack(fill = Y, side = RIGHT)

		# Create lower level 2 frame (File ops)
		if self.showMenuBar == True:
			self.fileOpsFrame = ttk.Frame(root, style = "FS.TFrame", name = "fileOpsFrame")
			self.fileOpsFrame.pack(fill = X, side = BOTTOM)

			if self.showTabBar == True:		
				# Create tabFrame to go inside level 2 frame
				self.tabFrame = Frame(self.fileOpsFrame, name = "tabFrame")
				self.tabBar = TabBar(self.tabFrame)

		"""# Create text box in textFrame
		if self.styleMode == 0:
			self.textBox = Text(self.textFrame, bg = "#FFFFFF", fg = "#404040", padx = 10, pady = 10, wrap = "word")
			self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)
			self.textBox.focus_set()
		elif self.styleMode == 1:
			self.textBox = Text(self.textFrame, bg = "#404040", fg = "#FFFFFF", insertbackground = "#DDDDDD", padx = 10, pady = 10, wrap = "word")
			self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)
			self.textBox.focus_set()"""

		"""# Create scrollbar in textFrame
		self.textScrollBar = ttk.Scrollbar(self.textFrame, style = "SB.Vertical.TScrollbar")
		self.textScrollBar.pack(fill = Y, side = RIGHT)

		# Link scrollbar and text box
		self.textBox.config(yscrollcommand = self.textScrollBar.set)
		self.textScrollBar.config(command = self.textBox.yview)"""

		if self.showFormFrame == True:
			# Create formatting buttons in formFrame
			self.boldButton = ttk.Button(self.formFrame, text = "<B>", width = 4, style = "FB.TButton", takefocus = 0)
			self.boldButton.pack(side = TOP, expand = 0, fill = X)
			self.boldButton.bind("<Enter>", lambda event: self.boldButton.configure(style = "FOB.TButton"))
			self.boldButton.bind("<Leave>", lambda event: self.boldButton.configure(style = "FB.TButton"))

			self.italicButton = ttk.Button(self.formFrame, text = "*I*", width = 4, style = "FB.TButton", takefocus = 0)
			self.italicButton.pack(side = TOP, expand = 0, fill = X)

			self.underlineButton = ttk.Button(self.formFrame, text = "_U_", width = 4, style = "FB.TButton", takefocus = 0)
			self.underlineButton.pack(side = TOP, expand = 0, fill = X)

		if self.showMenuBar == True:
			# Create file operation buttons in fileOpsFrame

			self.quitButton = ttk.Button(self.fileOpsFrame, text = "Quit", width = 6, command = self.Quit, style = "FOB.TButton", takefocus = 0)
			self.quitButton.pack(side = RIGHT)

			self.openButton = ttk.Button(self.fileOpsFrame, text = "Open", width = 6, command = self.askLocation, style = "FOB.TButton", takefocus = 0)
			self.openButton.pack(side = RIGHT)
			self.openButton.bind("<Shift-Enter>", lambda event: self.openButton.configure(text = "New", command = self.New))
			self.openButton.bind("<Shift-Leave>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))
			self.openButton.bind("<Enter>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))
			self.openButton.bind("<Leave>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))

			self.saveButton = ttk.Button(self.fileOpsFrame, text = "Save", width = 6, command = self.saveFile, style = "FOB.TButton", takefocus = 0)
			self.saveButton.pack(side = RIGHT)
			self.saveButton.bind("<Shift-Enter>", lambda event: self.saveButton.configure(text = "Save As", command = self.saveAsFile))
			self.saveButton.bind("<Shift-Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Alt-Enter>", lambda event: self.saveButton.configure(text = "Rename", command = self.renameFile))
			self.saveButton.bind("<Alt-Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Enter>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))

			if self.showTabBar == True:
				# Tab left button
				"""self.tabLeftButton = ttk.Button(self.tabFrame, text = "<", width = 0, style = "FOB.TButton")
				self.tabLeftButton.pack(side = LEFT)"""

				self.tabBar.add("PlaceNameDoodymajig.py")
				self.tabBar.add("Thingy.py")
				self.tabBar.add("Boop.nom")

				# Tab right button
				"""self.tabRightButton = ttk.Button(self.tabFrame, text = ">", width = 0, style = "FOB.TButton")
				self.tabRightButton.pack(side = RIGHT)#"""

	# Ask for location and open file
	def askLocation(self):

		# Function to write contents of input file to textBox
		def openFile(self):

			# Run open dialog box to get filename
			self.openLocation = filedialog.askopenfilename(filetypes = (("Note files","*.note"),("Text files","*.txt")))

			# If the filename is a blank string
			if self.openLocation == "" or str(self.openLocation) == "()":
				# Return exception here - new window saying "No file selected"
				self.Log.write("\tNo location selected to open")

			else:
				# Open inputFile
				self.inputFile = open (self.openLocation, "r")
				root.title(self.openLocation + " - NoteVelocity")

				logString = "\tOpening " + self.openLocation
				self.Log.write(logString)

				# Clear self.textBox
				self.textBox.delete(1.0,END)

				# Set self.outputFilename to openLocation
				self.outputFilename = self.openLocation

				# Initialise lineNumber
				lineNumber = 1

				# Reset logString
				logString = ""

				# Iterate through self.inputFile, adding to self.textBox
				for line in self.inputFile:

					# Create lineBuffer and lineBufferLen
					lineBuffer = list(line)
					lineBufferLen = range(len(lineBuffer))

					for n in lineBufferLen:
						index = str(lineNumber) + "." + str(lineBufferLen[n])
						self.textBox.insert(index,lineBuffer[n])

					lineNumber += 1

				# Log insertions
				logString = "\tWrote lines 1-" + str(lineNumber-1) + " to self.textBox"
				self.Log.write(logString)
				logString = "\tCompleted writing contents of " + self.openLocation + " to self.textBox"
				self.Log.writeNoTimestamp(logString)

		# Check to see whether contents of self.textBox are "\n" - ie empty
		textBoxContents = self.textBox.get(1.0,END)
		if textBoxContents == "\n" or textBoxContents == "" or textBoxContents == "\n\n" or textBoxContents == "\n\n":

			openFile(self)

		else:
			print(textBoxContents)
			saveyn = messagebox.askyesno("File Open","There is text entered.\nWould you like to save it before opening another?")

			if saveyn == True:

				# Run self.saveFile, then open file
				self.saveFile()
				openFile(self)

			else:
				# Open file
				openFile(self)

	# Save current file
	def saveFile(self):
		# Will probably need elaboration after replacements have been added
		# If outputFilename hasn't been set, use saveAsFile instead, and log
		if self.outputFilename is None or self.outputFilename == "" or str(self.outputFilename) == "()":
			self.saveAsFile()
			self.Log.write("\tNo output file set. Using save as instead.")

		# Otherwise get textBox contents, open outputFile, write, close and log
		else:
			textToSave = self.textBox.get(1.0, END)
			outputFile = open(self.outputFilename, "w+")
			outputFile.write(textToSave)
			outputFile.close()
			self.Log.write("\tWrote contents of self.textBox to " + self.outputFilename)

	# Save current file as
	def saveAsFile(self):
		# Get save filename
		self.outputFilename = filedialog.asksaveasfilename(defaultextension = "*.note", filetypes = (("Note File","*.note"), ("Text File", "*.txt")))

		# Catch empty outputFilenames
		if self.outputFilename == "" or str(self.outputFilename) == "()":
			self.Log.write("\tNo save location selected")

		# Otherwise save textbox
		else:
			# Get textbox contents
			textToSave = self.textBox.get(1.0, END)

			# Open outputfile, write, close and log
			outputFile = open(self.outputFilename, "w+")
			outputFile.write(textToSave)
			outputFile.close()
			self.Log.write("\tFile saved at " + self.outputFilename)

	# Rename current file
	def renameFile(self):
		# Get save filename
		self.outputFilename = filedialog.asksaveasfilename(defaultextension = "*.note", filetypes = (("Note File","*.note"), ("Text File", "*.txt")))

		# Catch empty outputFilenames
		if self.outputFilename == "" or str(self.outputFilename) == "()":
			self.Log.write("\tNo save location selected")

		# Otherwise rename file
		else:
			# Get textbox contents
			textToSave = self.textBox.get(1.0, END)

			# Open outputfile, write, close and log
			outputFile = open(self.outputFilename, "w+")
			outputFile.write(textToSave)
			outputFile.close()
			self.Log.write("\tFile renamed to " + self.outputFilename)
			root.title(self.outputFilename + " - NoteVelocity")
			os.remove(self.openLocation)

	# Create new note
	def New(self):

		def newFile(self):
			# Set new window title
			root.title("New Note - NoteVelocity")

			# Delete contents of self.textbox, and write new note to log
			self.textBox.delete(1.0, END)
			self.Log.write("\tNew note")

			# Reset input and output files
			self.inputFile = None
			self.outputFilename = None

		# Check to see whether contents of self.textBox are "\n" - ie empty
		if self.textBox.get(1.0, END) == "\n":

			newFile(self)

		else:
			saveyn = messagebox.askyesno("File Open","There is text entered.\nWould you like to save it before opening another?")

			if saveyn == True:

				# Run self.saveFile, then make a new file
				self.saveFile(self)
				newFile(self)

			else:
				# Open file
				newFile(self)

	# Hide and show tab bar
	def tabHideShow(self):
		if self.showTabBar == True:
			self.showTabBar = False
		elif self.showTabBar == False:
			self.showTabBar = True
		else:
			logString = "\tself.showTabBar was not True or False."
			self.Log.write(logString)

		if self.showTabBar == True:

			# Create tabs frame to go inside level 2 frame
			#self.tabFrame = Frame(self.fileOpsFrame)
			self.tabFrame.pack(fill = X, side = LEFT, expand = 1)

			"""# Tabs
			self.tabLeftButton = Button(self.tabFrame, text = "<", width = 0, font = ("DejaVu Sans", "8", "normal"))
			self.tabLeftButton.pack(side = LEFT)

			## TABS GO HERE

			self.tabRightButton = Button(self.tabFrame, text = ">", width = 0, font = ("DejaVu Sans", "8", "normal"))
			self.tabRightButton.pack(side = RIGHT)"""
		else:
			# Remove/hide self.tabFrame
			self.tabFrame.pack_forget()

	# Initialise styles
	def initStyles(self):
		
		if self.styleMode == 0:
			# Formatting buttons
			self.formButtonFont = Font(family = "DejaVu Sans", size = 8)
			self.formatButtonStyle = ttk.Style()
			self.formatButtonStyle.configure("FB.TButton", font = self.formButtonFont, foreground = "#202020", background = "#EEEEEE")

			# FileOps buttons
			self.fileButtonFont = Font(family = "DejaVu Sans", size = 8)
			self.fileOpsButtonStyle = ttk.Style()
			self.fileOpsButtonStyle.configure("FOB.TButton", font = self.fileButtonFont, foreground = "#202020", background = "#EEEEEE")

			# Frames
			self.frameStyle = ttk.Style()
			self.frameStyle.configure("FS.TFrame", background = "#DDDDDD")

			# ScrollBar
			self.scrollBarStyle = ttk.Style()
			self.scrollBarStyle.configure("SB.Vertical.TScrollbar", background = "#DDDDDD", arrowsize = 12)

		elif self.styleMode == 1:
			# Formatting buttons
			self.formButtonFont = Font(family = "DejaVu Sans", size = 8)
			self.formatButtonStyle = ttk.Style()
			self.formatButtonStyle.configure("FB.TButton", font = self.formButtonFont, foreground = "#EEEEEE", background = "#202020")

			# FileOps buttons
			self.fileButtonFont = Font(family = "DejaVu Sans", size = 8)
			self.fileOpsButtonStyle = ttk.Style()
			self.fileOpsButtonStyle.configure("FOB.TButton", font = self.fileButtonFont, foreground = "#EEEEEE", background = "#202020")

			# Frames
			self.frameStyle = ttk.Style()
			self.frameStyle.configure("FS.TFrame", background = "#101010")

			# ScrollBar
			self.scrollBarStyle = ttk.Style()
			self.scrollBarStyle.configure("SB.Vertical.TScrollbar", background = "#151515", arrowsize = 12)

		else:
			self.Log.write("Style initialisation mode out of expected range")

	# Initialise keybindings
	def keyBindings(self, master):

		# Unbind Control-Tab from cycling focus
		root.bind("<Control-Tab>", lambda event: self.doNothing())
		root.bind("<Control-Shift-Tab>", lambda event: self.doNothing())

		# Bind Control-O to Open
		master.bind("<Control-o>", lambda event: self.askLocation())

		# Bind Control-Shift-O and Control-N to New
		master.bind("<Control-O>", lambda event: self.New())
		master.bind("<Control-N>", lambda event: self.New())

		# Bind Control-S to Save
		master.bind("<Control-s>", lambda event: self.saveFile())

		# Bind Control-Shift-S to Save As
		master.bind("<Control-S>", lambda event: self.saveAsFile())

		# Bind Control-Alt-S to Rename
		master.bind("<Control-Alt-s>", lambda event: self.renameFile())

		# Bind Control-Alt-T to TabHideShow
		master.bind("<Control-Alt-t>", lambda event: self.tabHideShow())

		# Bind Control-w and Control-q to root.quit
		master.bind("<Control-q>", lambda event: self.Quit())

	# Quit
	def Quit(self):
		self.Log.close()
		Quit(self)

	def doNothing(self):
		pass

## Log class
class logFile:

	# Initialise function
	def __init__(self, logLocation):
		self.logFileFile = open(logLocation, "w+")
		now = datetime.datetime.now()
		self.logFileFile.write("Time of log creation: " + str(now))
		self.logFileFile.close()
		self.location = logLocation

	# Write function
	def write(self, string):
		self.logFileFile = open(self.location, "a")
		now = datetime.datetime.now()
		self.logFileFile.write("\n\nAt " + str(now) + ":\n" + string)
		self.logFileFile.close()

	# WriteNoTimestamp function
	def writeNoTimestamp(self, string):
		self.logFileFile = open(self.location, "a")
		self.logFileFile.write("\n\n" + string)
		self.logFileFile.close()

	# Close function
	def close(self):
		self.logFileFile = open(self.location, "a")
		now = datetime.datetime.now()
		self.logFileFile.write("\n\nAt " + str(now) + ":\n\t" + "Closing log file and exiting")
		self.logFileFile.close()

## Quit function - does anything needed before quitting
def Quit(self):
	root.quit()


## TABS

# TabContents class for adding to Tab
class TabContents(Text):

	# Constructor
	def __init__(self, master):

		lastCharacters = None

		# Initialise text area
		Text.__init__(self, master, bg = '#FFFFFF', fg = '#404040', padx = 10, pady = 10, wrap = 'word')
		"""for k in master.configure().keys():
			print(k, ":", master.cget(k))"""
		masterStack = master
		print(str(masterStack))

# Tab class for adding to TabBar
class Tab(Frame):

	# Constructor
	def __init__(self, master, title, number):

		# Initialise frame and internal frame
		Frame.__init__(self, master, bg = "#000000", width = "200", height = 24, name = "tab")
		self.subFrame = Frame(self, name = "tab subframe")
		self.subFrame.pack(side = LEFT, padx = 5, ipadx = 0, ipady = 2)
		self.subSubFrame = Frame(self.subFrame, name = "tab sub-subframe")
		self.subSubFrame.pack(side = LEFT, padx = 2)
		self.subSubFrame.bind("<Button-1>", lambda event: master.switchToTab(self.Num))

		# Set tab number
		self.Num = number

		# Set location and title
		self.location = title
		splitName = title.split("/")
		self.longTitle = splitName[-1]
		self.title = self.longTitle

		# If title is longer than 15 chars, shorten it. Otherwise do nothing
		if len(self.title) > 15:
			self.title = self.title[:12] + "..."

		# Create instance of TabContents
		self.textBox = TabContents(master)
		

		# Create tab's widgets, overlaying them using the place manager
		# Tab Label
		self.Label = Label(self.subSubFrame, text = self.title)
		self.Label.pack(side = LEFT, expand = 0, fill = X, padx = 5)
		self.Label.bind("<Button-1>", lambda event: master.switchToTab(self.Num))

		# Tab close button
		self.CloseButton = ttk.Button(self.subSubFrame, text = "X", width = 0, takefocus = 0)
		self.CloseButton.pack(side = RIGHT, expand = 0)
		self.CloseButton.bind("<Button-1>", lambda event: app.tabBar.close(self.Num))

		# Tab unsaved indicator
		self.tabSaved = Frame(self.subSubFrame, width = 8, height = 8, bg = "#00FF00")
		self.tabSaved.pack(side = RIGHT, padx = 5)

# TabBar Class
class TabBar(Frame):

	# Constructor
	def __init__(self, master):

		# Initialise frame
		Frame.__init__(self, master, name = "tab bar")

		# Initialise tab list
		# want to set it so that when you put in the tab number, you get the tab out
		# eg self.tabList[0] = tab
		self.tabList = []

		# Initialise other variables
		self.currentTab = 0
		self.previousTab = 0

		# Initialise keybindings
		self.keyBindings()

	def show(self):
		# Pack to bottom. For integration in actual thing, fill should be change to XY.
		self.pack(side = LEFT, expand = 0, fill = X)

		self.currentTab = 0
		self.switchToTab(0)

	def add(self, tabLocation):

		# Set currentTab to be the last one
		# New tab will always be at the end
		self.previousTab = self.currentTab
		"""self.currentTab = len(self.tabList)"""
		newTabNum = len(self.tabList)

		# Initialise variable newTab as added Tab instance
		newTab = Tab(self, tabLocation, newTabNum)

		# Append tabList with new tab
		self.tabList.append(newTab)

		self.switchToTab(-1)

	def switchBy(self, number):
		if number != 1 and number != -1:
			# Throw error here - this should not happen
			pass
		else:

			if number == 1 and self.currentTab == len(self.tabList) - 1:
				currentTab = 0
			elif number == -1 and self.currentTab == 0:
				currentTab = len(self.tabList) - 1
			else:
				currentTab = self.currentTab + number
 
			self.switchToTab(currentTab)

		return "break"

	def switchToTab(self, index):
		# Set old tab to previous tab and new to index
		self.previousTab = self.currentTab
		if index == -1:
			self.currentTab = len(self.tabList) - 1
		else:
			self.currentTab = index

		# Make aesthetic changes to show selectedness
		self.tabList[self.previousTab].subFrame.config(bg = "#FFFFFF")
		self.tabList[self.currentTab].subFrame.config(bg = "#FF0000")

		# Update root.title
		root.title(self.tabList[self.currentTab].longTitle)

		# Update text box showing
		self.updateTextBoxes()

		return "break"

	def close(self, index):

		print("Closing tab " + str(index))
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
			self.add("New Note")
			self.tabList[index].pack_forget()
			self.tabList[index].textBox.pack_forget()

	def updateTextBoxes(self):
		self.tabList[self.previousTab].textBox.pack_forget()
		#self.tabList[self.currentTab].textBox.pack(side = TOP, expand = 1, fill = X)

		# Change focus back to tab's textBox
		#self.tabList[self.currentTab].textBox.focus()
		

	def keyBindings(self):

		root.bind("<Control-t>", lambda event: self.switchBy(1))
		root.bind("<Control-T>", lambda event: self.switchBy(-1))

		root.bind("<Control-1>", lambda event: self.switchToTab(0))
		root.bind("<Control-2>", lambda event: self.switchToTab(1))
		root.bind("<Control-3>", lambda event: self.switchToTab(2))
		root.bind("<Control-4>", lambda event: self.switchToTab(3))
		root.bind("<Control-5>", lambda event: self.switchToTab(4))
		root.bind("<Control-6>", lambda event: self.switchToTab(5))
		root.bind("<Control-7>", lambda event: self.switchToTab(6))
		root.bind("<Control-8>", lambda event: self.switchToTab(7))
		root.bind("<Control-9>", lambda event: self.switchToTab(8))

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