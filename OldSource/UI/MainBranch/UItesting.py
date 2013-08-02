"""The main UI file of my note-taking program"""

## Imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
		self.outputFile = None

		# Initialise show variables
		self.showFormFrame = True
		self.showMenuBar = True
		self.showTabBar = False

		self.Log.write(self.logLocation, "\tInitialised variables")

		# Initialise tab stuff
		tabs = list()

		# Create upper level 2 frame (Text + Formatting)
		self.textFormFrame = Frame(bg = "#FF0000")
		self.textFormFrame.pack(fill = BOTH, side = TOP, expand = 1)

		# Create left level 3 frame (Text)
		self.textFrame = Frame(self.textFormFrame, bg = "#FF8800")
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
			self.boldButton = Button(self.formFrame, text = "<B>", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.boldButton.pack(side = TOP)
			self.boldButton.bind('<Enter>', lambda event: self.boldButton.configure(text = "B", font = ("DejaVu Sans", "8", "bold")))
			self.boldButton.bind('<Leave>', lambda event: self.boldButton.configure(text = "<B>", font = ("DejaVu Sans", "8", "normal")))

			self.italicButton = Button(self.formFrame, text = "*I*", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.italicButton.pack(side = TOP)
			self.italicButton.bind('<Enter>', lambda event: self.italicButton.configure(text = "I", font = ("DejaVu Sans", "8", "italic")))
			self.italicButton.bind('<Leave>', lambda event: self.italicButton.configure(text = "*I*", font = ("DejaVu Sans", "8", "normal")))

			self.underlineButton = Button(self.formFrame, text = "_U_", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.underlineButton.pack(side = TOP)
			self.underlineButton.bind('<Enter>', lambda event: self.underlineButton.configure(text = "U", font = ("DejaVu Sans", "8", "underline")))
			self.underlineButton.bind('<Leave>', lambda event: self.underlineButton.configure(text = "_U_", font = ("DejaVu Sans", "8", "normal")))

		if self.showMenuBar == True:
			# Create file operation buttons in fileOpsFrame

			self.quitButton = Button(self.fileOpsFrame, text = "Quit", font = ("DejaVu Sans", "8", "normal"), command = self.Quit)
			self.quitButton.pack(side = RIGHT)

			self.newButton = Button(self.fileOpsFrame, text = "New", font = ("DejaVu Sans", "8", "normal"), command = self.New)
			self.newButton.pack(side = RIGHT)

			self.openButton = Button(self.fileOpsFrame, text = "Open", font = ("DejaVu Sans", "8", "normal"), command = self.askLocation)
			self.openButton.pack(side = RIGHT)

			self.saveButton = Button(self.fileOpsFrame, text = "Save", font = ("DejaVu Sans", "8", "normal"), command = self.saveFile)
			self.saveButton.pack(side = RIGHT)

			if self.showTabBar == True:
				# Tabs
				self.tabLeftButton = Button(self.tabFrame, text = "<", width = 0, font = ("DejaVu Sans", "8", "normal"))
				self.tabLeftButton.pack(side = LEFT)

				## TABS GO HERE

				self.tabRightButton = Button(self.tabFrame, text = ">", width = 0, font = ("DejaVu Sans", "8", "normal"))
				self.tabRightButton.pack(side = RIGHT)

	# Ask for location and open file
	def askLocation(self):

		# Function to write contents of input file to textBox
		def openFile(self):

			# Run open dialog box to get filename
			openLocation = filedialog.askopenfilename(filetypes = (("Note files","*.note"),("Text files","*.txt")))

			# If the filename is a blank string
			if openLocation == "":
				# Return exception here - new window saying "No file selected"
				self.Log.write(self.logLocation, "\tNo location selected to open")

			else:
				# Open inputFile
				self.inputFile = open (openLocation, "r")

				logString = "\tOpening " + openLocation
				self.Log.write(self.logLocation, logString)

				# Clear self.textBox
				self.textBox.delete(1.0,END)

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

				logString = "\tWrote lines 1-" + str(lineNumber-1) + " to self.textBox"
				self.Log.write(self.logLocation, logString)
				logString = "\tCompleted writing contents of " + openLocation + " to self.textBox"
				self.Log.writeNoTimestamp(self.logLocation, logString)

		# Check to see whether contents of self.textBox are "\n" - ie empty
		if self.textBox.get(1.0,END) == "\n":

			openFile(self)

		else:
			saveyn = messagebox.askyesno("File Open","There is text entered.\nWould you like to save it before opening another?")

			if saveyn == True:

				# Run self.saveFile, then open file
				self.saveFile(self)
				openFile(self)

			else:
				# Open file
				openFile(self)

	# Save current file
	def saveFile(self):
		pass

	# Create new note
	def New(self):
		pass

	# Hide and show tab bar
	def tabHideShow(self):
		if self.showTabBar == True:
			self.showTabBar = False
		elif self.showTabBar == False:
			self.showTabBar = True
		else:
			logString = "\tself.showTabBar was not True or False."
			self.Log.write(self.logLocation, logString)

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


	# Quit
	def Quit(self):
		self.Log.close(self.logLocation)
		Quit(self)

## Log function
class logFile:
	# Initialise function
	def __init__(self, logLocation):
		self.logFileFile = open(logLocation, "w+")
		now = datetime.datetime.now()
		self.logFileFile.write("Time of log creation: " + str(now))
		self.logFileFile.close()

	# Write function
	def write(self, logLocation, string):
		self.logFileFile = open(logLocation, "a")
		now = datetime.datetime.now()
		self.logFileFile.write("\n\nAt " + str(now) + ":\n" + string)
		self.logFileFile.close()

	# WriteNoTimestamp function
	def writeNoTimestamp(self, logLocation, string):
		self.logFileFile = open(logLocation, "a")
		self.logFileFile.write("\n\n" + string)
		self.logFileFile.close()

	# Close function
	def close(self, logLocation):
		self.logFileFile = open(logLocation, "a")
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
root.title("New Note") # Title in window title bar
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
