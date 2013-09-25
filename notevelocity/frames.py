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

		self.title = Label(self.Frame, text = "NoteVelocity")
		self.title.pack(expand = 1, fill = BOTH, side = LEFT)

		self.close = Button(self.Frame, text = "X", command = self.master.quit)
		self.close.pack(expand = 0, side = RIGHT)

		self.max = Button(self.Frame, text = "+")
		self.max.pack(expand = 0, side = RIGHT)

		self.min = Button(self.Frame, text = "_")
		self.min.pack(expand = 0, side = RIGHT)

		self.dragBindings()

	def buttonAChange(self, changeTo):
		if changeTo == 0:
			self.buttonA.config(text = "Save")

		elif changeTo == 1:
			self.buttonA.config(text = "Save As")

		elif changeTo == 2:
			self.buttonA.config(text = "Rename")

		else:
			print("buttonAChange was given an index which was out of range")

	def dragBindings(self):

		self.title.bind("<ButtonPress-1>", self.startMove)
		self.title.bind("<ButtonRelease-1>", self.stopMove)
		self.title.bind("<B1-Motion>", self.onMotion)

	def startMove(self, event):
		self.root.x = event.x
		self.root.y = event.y

	def stopMove(self, event):
		self.root.x = None
		self.root.y = None

	def onMotion(self, event):
		deltax = event.x - self.root.x
		deltay = event.y - self.root.y
		x = self.root.winfo_x() + deltax
		y = self.root.winfo_y() + deltay
		self.root.geometry("+%s+%s" % (x, y))

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