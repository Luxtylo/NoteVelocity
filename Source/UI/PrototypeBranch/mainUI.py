"""The main UI file of my note-taking program"""

## Imports
from Tkinter import *

## Initialise NoteApp class
class NoteApp:

	# Constructor
	def __init__(self, master):
		# Create frame
		frame = Frame(master)
		# Pack frame to contents
		frame.pack()

		# Make self.button, which is a button widget - runs frame.quit
		self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
		self.button.pack(side=LEFT)

		# Make self.hi_there, a button widget which runs self.say_hi
		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)

	def say_hi(self):
		print "hi there, everyone!"

## Starting

#Root widget
root = Tk()

# New instance of NoteApp
app = NoteApp(root)

# Call root widget's main loop
root.mainloop()