"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *

## Main
# Title bar
class titleBar(Frame):
	def __init__(self, master):

		self.master = master

		self.testMessage = "titleBar is initialised"

		self.Frame = Frame()
		self.Frame.pack(fill = X, side = TOP, expand = 1, ipadx = 2, ipady = 2)

		self.icon = Frame(self.Frame)
		self.icon.pack(expand = 0, side = LEFT)

		self.buttonA = Button(self.Frame, text = "Save")
		self.buttonA.pack(expand = 0, side = LEFT)

		self.buttonB = Button(self.Frame, text = "Open")
		self.buttonB.pack(expand = 0, side = LEFT)

		self.title = Label(self.Frame, text = "NoteVelocity")
		self.title.pack(expand = 1, fill = BOTH, side = LEFT)

		self.close = Button(self.Frame, text = "X")
		self.close.pack(expand = 0, side = RIGHT)

		self.max = Button(self.Frame, text = "+")
		self.max.pack(expand = 0, side = RIGHT)

		self.min = Button(self.Frame, text = "_")
		self.min.pack(expand = 0, side = RIGHT)

	def buttonAChange(self, changeTo):
		if changeTo == 0:
			self.buttonA.config(text = "Save")

		elif changeTo == 1:
			self.buttonA.config(text = "Save As")

		elif changeTo == 2:
			self.buttonA.config(text = "Rename")

		else:
			print("buttonAChange was given an index which was out of range")