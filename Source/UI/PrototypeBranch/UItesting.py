"""The main UI file of my note-taking program"""

## Imports
from Tkinter import *

## Initialise NoteApp class
class NoteApp:

	## Constructor
	def __init__ (self, master):

		# Initialise variables
		self.showFormFrame = True
		self.showMenuBar = True

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

		# Create text box in textFrame
		self.textBox = Text(self.textFrame, bg = "#000000", fg = "#FFFFFF", padx = 5, pady = 5)
		self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)

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
			self.exampleButton = Button(self.fileOpsFrame, text = "Example", font = ("DejaVu Sans", "8", "normal"))
			self.exampleButton.pack(side = LEFT)

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