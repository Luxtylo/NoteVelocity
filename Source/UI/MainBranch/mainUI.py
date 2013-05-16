"""The main UI file of my note-taking program"""

## Imports
from Tkinter import *
from tkFileDialog import askopenfilename
import makeThe

## Initialise NoteApp class
class NoteApp:

	# Constructor
	def __init__(self, master):

		# Create textbox frame and contents
		self.makeTextboxFrame(master)

		# Create button frame and contents by calling makeButtonFrame
		self.makeButtonFrame(master)

		# Initialise things as None
		self.openLocation = None
		self.inputFile = None
		self.outputFile = None

	# Create textbox frame and contents
	def makeTextboxFrame(self, master):
		textFrame = makeThe.tkFrame(master, 1)

		# Make textbox
		self.textBox = Text(textFrame)
		self.textBox.pack(fill = BOTH, expand = "yes")

	# Create button frame and contents
	def makeButtonFrame(self, master):
		buttonFrame = makeThe.tkFrame(master, 2)

		# Make self.openLoc, a button widget which runs self.askLocation
		self.openButton = Button(buttonFrame, text = "Open", command = self.askLocation)
		self.openButton.pack(side=LEFT)

		# Make a button widget which runs self.printContents
		self.saveButton = Button(buttonFrame, text = "Save", command = self.saveFile)
		self.saveButton.pack(side = LEFT)

		# Make self.quitButton, which is a button widget - runs frame.quit
		self.quitButton = Button(buttonFrame, text = "Quit", fg = "red", command = buttonFrame.quit)
		self.quitButton.pack(side=LEFT)

	# Ask for location and open file
	def askLocation(self):
		# Run open dialog box to get filename
		self.openLocation = askopenfilename(filetypes = [("Note files","*.note"),("Text files","*.txt")])

		# If the filename is a blank string
		if self.openLocation == "":
			# Return exception here - new window saying "No file selected"
			print ("Open Location Empty")
		else:
			# Open inputFile
			self.inputFile = open (self.openLocation, "r")

	def saveFile(self):
		pass

## STARTING

# Root widget
root = Tk()

# Root widget properties
root.title("Note") # Title in window title bar
root.minsize(640,480) # Minimum size of window
root.geometry("800x600") # Initial size of window

# New instance of NoteApp
app = NoteApp(root)

# Call root widget's main loop
root.mainloop()