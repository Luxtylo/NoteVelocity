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
		self.showTabBar = False

		# Initialise styles
		self.initStyles()

		# Initialise tab stuff
		tabs = list()

		# Initialise key bindings
		self.keyBindings(master)

		self.Log.write("\tInitialised variables, styles and keybindings")		

		# Create upper level 2 frame (Text + Formatting)
		self.textFormFrame = Frame()
		self.textFormFrame.pack(fill = BOTH, side = TOP, expand = 1)

		# Create left level 3 frame (Text)
		self.textFrame = Frame(self.textFormFrame)
		self.textFrame.pack(fill = BOTH, expand = 1, side = LEFT)

		if self.showFormFrame == True:
			# Create right level 3 frame (Formatting)
			self.formFrame = Frame(self.textFormFrame)
			self.formFrame.pack(fill = Y, side = RIGHT)

		# Create lower level 2 frame (File ops)
		if self.showMenuBar == True:
			self.fileOpsFrame = Frame()
			self.fileOpsFrame.pack(fill = X, side = BOTTOM)

			if self.showTabBar == True:		
				# Create tabs frame to go inside level 2 frame
				self.tabFrame = Frame(self.fileOpsFrame)
				self.tabFrame.pack(fill = X, side = LEFT, expand = 1)

		# Create text box in textFrame
		self.textBox = Text(self.textFrame, bg = "#FFFFFF", fg = "#404040", padx = 5, pady = 5, wrap = "word")
		self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)
		self.textBox.focus_set()

		# Create scrollbar in textFrame
		self.textScrollBar = Scrollbar(self.textFrame, width = 16)
		self.textScrollBar.pack(fill = Y, side = RIGHT)

		# Link scrollbar and text box
		self.textBox.config(yscrollcommand = self.textScrollBar.set)
		self.textScrollBar.config(command = self.textBox.yview)

		if self.showFormFrame == True:
			# Create formatting buttons in formFrame
			self.boldButton = ttk.Button(self.formFrame, text = "<B>", width = 4, style = "FB.TButton")
			self.boldButton.pack(side = TOP, expand = 0, fill = X)
			self.boldButton.bind("<Enter>", lambda event: self.boldButton.configure(style = "FOB.TButton"))
			self.boldButton.bind("<Leave>", lambda event: self.boldButton.configure(style = "FB.TButton"))

			self.italicButton = ttk.Button(self.formFrame, text = "*I*", width = 4, style = "FB.TButton")
			self.italicButton.pack(side = TOP, expand = 0, fill = X)

			self.underlineButton = ttk.Button(self.formFrame, text = "_U_", width = 4, style = "FB.TButton")
			self.underlineButton.pack(side = TOP, expand = 0, fill = X)

		if self.showMenuBar == True:
			# Create file operation buttons in fileOpsFrame

			self.quitButton = ttk.Button(self.fileOpsFrame, text = "Quit", width = 6, command = self.Quit, style = "FOB.TButton")
			self.quitButton.pack(side = RIGHT)

			self.openButton = ttk.Button(self.fileOpsFrame, text = "Open", width = 6, command = self.askLocation, style = "FOB.TButton")
			self.openButton.pack(side = RIGHT)
			self.openButton.bind("<Shift-Enter>", lambda event: self.openButton.configure(text = "New", command = self.New))
			self.openButton.bind("<Shift-Leave>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))
			self.openButton.bind("<Enter>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))
			self.openButton.bind("<Leave>", lambda event: self.openButton.configure(text = "Open", command = self.askLocation))

			self.saveButton = ttk.Button(self.fileOpsFrame, text = "Save", width = 6, command = self.saveFile, style = "FOB.TButton")
			self.saveButton.pack(side = RIGHT)
			self.saveButton.bind("<Shift-Enter>", lambda event: self.saveButton.configure(text = "Save As", command = self.saveAsFile))
			self.saveButton.bind("<Shift-Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Alt-Enter>", lambda event: self.saveButton.configure(text = "Rename", command = self.renameFile))
			self.saveButton.bind("<Alt-Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Enter>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))
			self.saveButton.bind("<Leave>", lambda event: self.saveButton.configure(text = "Save", command = self.saveFile))

			if self.showTabBar == True:
				# Tabs
				self.tabLeftButton = ttk.Button(self.tabFrame, text = "<", width = 0)
				self.tabLeftButton.pack(side = LEFT)

				## TABS GO HERE

				self.tabRightButton = ttk.Button(self.tabFrame, text = ">", width = 0)
				self.tabRightButton.pack(side = RIGHT)#

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
			self.Log.write("\tFile saved at " + self.outputFilename)
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
			self.tabFrame = Frame(self.fileOpsFrame)
			self.tabFrame.pack(fill = X, side = LEFT, expand = 1)

			# Tabs
			self.tabLeftButton = Button(self.tabFrame, text = "<", width = 0, font = ("DejaVu Sans", "8", "normal"))
			self.tabLeftButton.pack(side = LEFT)

			## TABS GO HERE

			self.tabRightButton = Button(self.tabFrame, text = ">", width = 0, font = ("DejaVu Sans", "8", "normal"))
			self.tabRightButton.pack(side = RIGHT)
		else:
			# Remove/hide self.tabFrame
			self.tabFrame.destroy()

	# Initialise styles
	def initStyles(self):
		
		# Formatting buttons
		self.formButtonFont = Font(family = "DejaVu Sans", size = 8)
		self.formatButtonStyle = ttk.Style()
		self.formatButtonStyle.configure("FB.TButton", font = self.formButtonFont, foreground = "#202020", background = "#EEEEEE")

		# FileOps buttons
		self.fileButtonFont = Font(family = "DejaVu Sans", size = 8)
		self.fileOpsButtonStyle = ttk.Style()
		self.fileOpsButtonStyle.configure("FOB.TButton", font = self.fileButtonFont, foreground = "#202020", background = "#EEEEEE")

	# Initialise keybindings
	def keyBindings(self, master):
		# Bind Control-O to Open
		master.bind("<Control-o>", lambda event: self.askLocation())

		# Bind Control-Shift-O and Control-N to New
		master.bind("<Control-O>", lambda event: self.New())
		master.bind("<Control-N>", lambda event: self.New())

		# Bind Control-S to Save
		master.bind("<Control-s>", lambda event: self.SaveFile())

		# Bind Control-Shift-S to Save As
		master.bind("<Control-S>", lambda event: self.SaveAsFile())

		# Bind Control-Alt-S to Rename
		master.bind("<Control-Alt-s>", lambda event: self.renameFile())

		# Bind Control-Alt-T to TabHideShow
		master.bind("<Control-Alt-t>", lambda event: self.tabHideShow())

		# Bind Control-w and Control-q to root.quit
		master.bind("<Control-w>", lambda event: self.Quit())
		master.bind("<Control-q>", lambda event: self.Quit())

	# Quit
	def Quit(self):
		self.Log.close()
		Quit(self)

## Log function
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
