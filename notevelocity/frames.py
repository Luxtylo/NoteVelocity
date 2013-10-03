"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *
from tkinter.ttk import *

## Main
# Title bar
class titleBar(Frame):
	def __init__(self, master, root):

		self.master = master
		self.root = root

		self.testMessage = "titleBar is initialised"

		self.Frame = Frame()
		self.Frame.pack(fill = X, side = TOP, expand = 0, ipadx = 2, ipady = 2)

		self.icon = Frame(self.Frame)
		self.icon.pack(expand = 0, side = LEFT)

		self.buttonA = Button(self.Frame, text = "Save")
		self.buttonA.pack(expand = 0, side = LEFT)

		self.buttonB = Button(self.Frame, text = "Open")
		self.buttonB.pack(expand = 0, side = LEFT)

		self.title = Label(self.Frame, text = "New note                            ", anchor = CENTER)
		self.title.pack(expand = 1, fill = BOTH, side = LEFT)

		self.Bindings()

	def Bindings(self):
		self.buttonA.bind("<Enter>", lambda event: self.buttonASave())
		self.buttonA.bind("<Leave>", lambda event: self.buttonASave())

		self.buttonA.bind("<Shift-Enter>", lambda event: self.buttonASaveAs())
		self.buttonA.bind("<Shift-Leave>", lambda event: self.buttonASave())

		self.buttonA.bind("<Control-Enter>", lambda event: self.buttonARename())
		self.buttonA.bind("<Control-Leave>", lambda event: self.buttonASave())

	def buttonASave(self):
		self.buttonA.config(text = "Save", command = lambda: self.master.saveFile(1))

	def buttonASaveAs(self):
		self.buttonA.config(text = "Save As", command = lambda: self.master.saveFile(2))

	def buttonARename(self):
		self.buttonA.config(text = "Rename", command = lambda: self.master.saveFile(3))

# Formatting bar
class formatBar(Frame):
	def __init__(self, master):

		self.master = master

		self.testMessage = "formatBar is initialised"

		self.Frame = Frame()
		self.Frame.pack(fill = Y, side = LEFT, expand = 0, ipadx = 2, ipady = 2)

		self.bold = Button(self.Frame, text = "B")
		self.bold.pack(expand = 0, side = TOP)

		self.italic = Button(self.Frame, text = "I")
		self.italic.pack(expand = 0, side = TOP)

		self.settings = Button(self.Frame, text = "S")
		self.settings.pack(expand = 0, side = BOTTOM)

# Text Frame
class text(Frame):
	def __init__(self, master):

		self.master = master

		self.testMessage = "textFrame is initialised"

		self.Frame = Frame()
		self.Frame.pack(fill = BOTH, expand = 1, side = LEFT)

		self.scrollbar = Scrollbar(self.Frame)
		self.scrollbar.pack(expand = 0, fill = Y, side = RIGHT)

		self.textBox = Text(self.Frame)
		self.textBox.pack(expand = 1, fill = BOTH, side = LEFT)

		# Link self.textBox and self.scrollbar
		self.textBox.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.config(command = self.textBox.yview)