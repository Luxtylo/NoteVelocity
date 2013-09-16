"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *

## Main loop
class AppFrame(Frame):
	def __init__(self, master):
		self.master = master

		self.initVars()
		self.initUI()

	def initVars(self):
		pass

	def initUI(self):
		print("Initialising UI...")

		# Custom title bar
		self.titleBar = Frame(self.master)
		self.titleBar.pack(side = TOP, expand = True, fill = Y)
		self.titleBar.pack(ipadx = 2, ipady = 2)

		# Main text box and scrollbar
		self.textBoxContainer = Frame(self.master)
		self.textBoxContainer.pack(side = LEFT, expand = True, fill = BOTH)

		self.mainTextBox = Text(self.textBoxContainer)
		self.mainTextBox.pack(side=LEFT, expand = True, fill = BOTH)

		self.scrollBar = Scrollbar(self.textBoxContainer)
		self.scrollBar.pack(side = LEFT, expand = False, fill = Y)

		# Attach scrollbar to text box
		self.mainTextBox.config(yscrollcommand = self.scrollBar.set)
		self.scrollBar.config(command=self.mainTextBox.yview)

	def saveFile(self, rename):
		if rename == True:
			pass
		else:
			pass

	def open(self):
		pass

	def quit(self):
		pass

	def log(mode):
		if mode == 0:
			pass
		elif mode == 1:
			pass

# Set root window properties
root = Tk()

root.title("NoteVelocity - New Note")
root.minsize(640,480)

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

if screenWidth <=1024 or screenHeight <= 768:
	windowWidth = int(screenWidth * 3 / 4)
	windowHeight = int(screenHeight * 3 / 4)
	root.geometry(str(windowWidth) + "x" + str(windowHeight))
	print(str(windowWidth) + "x" + str(windowHeight))
else:
	root.geometry("800x600")

## Start main loop
app = AppFrame(root)
root.mainloop()
