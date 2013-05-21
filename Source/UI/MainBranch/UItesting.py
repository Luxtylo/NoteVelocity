"""The main UI file of my note-taking program"""

## Imports
from tkinter import *
from tkinter import filedialog
import datetime

## Initialise NoteApp class
class NoteApp:

	## Constructor
	def __init__ (self, master):

		# Initialise log
		Log.init(self)

		# Initialise variables
		self.openLocation = None
		self.inputFile = None
		self.outputFile = None

		# Initialise show variables
		self.showFormFrame = True
		self.showMenuBar = True

		Log.write(self,"\tInitialised variables")

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

			# Create tabs frame to go inside level 2 frame
			self.tabFrame = Frame(self.fileOpsFrame)
			self.tabFrame.pack(fill = X, side = LEFT, expand = 1)

		# Create text box in textFrame
		self.textBox = Text(self.textFrame, bg = "#FFFFFF", fg = "#404040", padx = 5, pady = 5)
		self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)

		# Run function to initialise text tags
		#initialiseTags()

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

			self.openButton = Button(self.fileOpsFrame, text = "Open", font = ("DejaVu Sans", "8", "normal"), command = self.askLocation)
			self.openButton.pack(side = RIGHT)

			self.saveButton = Button(self.fileOpsFrame, text = "Save", font = ("DejaVu Sans", "8", "normal"), command = self.saveFile)
			self.saveButton.pack(side = RIGHT)

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
				Log.write(self, "\tNo location selected to open")

			else:
				# Open inputFile
				self.inputFile = open (openLocation, "r")

				logString = "\tOpening " + openLocation
				Log.write(self, logString)

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

					logString = logString + "\n\tWrote line " + str(lineNumber) + " to self.textBox"

					lineNumber += 1

				Log.write(self, logString)
				logString = "\tCompleted writing contents of " + openLocation + " to self.textBox"
				Log.write(self, logString)

		# Check to see whether contents of self.textBox are "\n" - ie empty
		if self.textBox.get(1.0,END) == "\n":

			openFile(self)

		else:
			saveyn = askyesno("File Open","There is text entered.\nWould you like to save it before opening another?")

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
	
	# Initialise textBox's tage
	def initialiseTags(self):
		#textBox.tag_config()
		pass

	def Quit(self):
		Quit(self)

## Log function
def Log():
	# Initialise function
	def init(self):
		self.logFile = open("log.txt", "w+")
		now = datetime.datetime.now()
		self.logFile.write("Time of log creation: " + str(now))

	# Write function
	def write(self, string):
		now = datetime.datetime.now()
		self.logFile.write("\n\nAt " + str(now) + ":\n" + string)

	# Close function
	def close(self):
		now = datetime.datetime.now()
		self.logFile.write("\n\nAt " + str(now) + ":\n\t" + "Closing log file")

	# Return stuff
	Log.init = init
	Log.write = write
	Log.close = close
	return Log

Log = Log()

## Quit function - does anything needed before quitting
def Quit(self):
	Log.close(self)
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
