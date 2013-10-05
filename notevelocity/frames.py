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
import bindings

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
	def __init__(self, master, root):

		self.master = master
		self.root = root

		self.testMessage = "textFrame is initialised"

		self.Frame = Frame()
		self.Frame.pack(fill = BOTH, expand = 1, side = LEFT)

		self.scrollbar = Scrollbar(self.Frame)
		self.scrollbar.pack(expand = 0, fill = Y, side = RIGHT)

		self.textBox = Text(self.Frame)
		self.textBox.pack(expand = 1, fill = BOTH, side = LEFT)
		self.textBox.config(tabs = ("0.5c", "0.75c", "0.825c"))

		# Link self.textBox and self.scrollbar
		self.textBox.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.config(command = self.textBox.yview)

		# Bind Enter to newLine
		self.textBox.bind("<Return>", lambda event: self.newLine())

		self.textBox.bind(bindings.increaseIndent, self.increaseIndent)
		self.textBox.bind(bindings.decreaseIndent, self.decreaseIndent)

		self.configureTags()

		self.startUpdate()

	# Make new lines keep the same indentation
	def newLine(self):
		self.tabbed = 0

		# Get current line
		lineNum, columnNum = self.textBox.index("insert").split(".")
		line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

		for char in line:
			if char == "\t":
				self.tabbed += 1

			else:
				break

		if self.tabbed != 0:
			insertIndex = str(int(lineNum) + 1) + ".0"
			insertTabs = "\n" + "\t" * self.tabbed
			self.textBox.insert(insertIndex, insertTabs)

		else:
			insertIndex = str(int(lineNum) + 1) + ".0"
			self.textBox.insert(insertIndex, "\n")

		return "break"

	def decreaseIndent(self, event):
		self.tabbed = 0

		# Get current line
		lineNum, columnNum = self.textBox.index("insert").split(".")
		line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

		for char in line:
			if char == "\t":
				self.tabbed += 1

			else:
				break

		if self.tabbed != 0:
			deleteStart = lineNum + ".0"
			deleteEnd = lineNum + ".1"
			self.textBox.delete(deleteStart, deleteEnd)

		return "break"

	def increaseIndent(self, event):
		lineNum, columnNum = self.textBox.index("insert").split(".")

		insertIndex = lineNum + ".0"

		self.textBox.insert(insertIndex, "\t")

	def configureTags(self):
		self.tags = ["title", "subtitle", "text"]

		self.textBox.tag_add(self.tags[0], "1.0", "end")
		self.textBox.tag_add(self.tags[1], "1.0", "end")
		self.textBox.tag_add(self.tags[2], "1.0", "end")

	def startUpdate(self):
		self.updateTagFlag = True
		self.updateTags()

	def stopUpdate(self):
		self.updateTagFlag = False

	# Run every second or so (do testing to find how often is necessary)
	def updateTags(self):

		if self.updateTagFlag:

			lineNum = 0

			for line in self.textBox.get("1.0", "end"):

				self.tabbed = 0

				for char in line:
					if char == "\t":
						self.tabbed += 1

					else:
						break

				lineStart = str(lineNum) + ".0"
				lineEnd = str(lineNum) + ".end"

				# Remove tags
				self.textBox.tag_remove(self.tags[0], lineStart, lineEnd)
				self.textBox.tag_remove(self.tags[1], lineStart, lineEnd)
				self.textBox.tag_remove(self.tags[2], lineStart, lineEnd)

				if self.tabbed == 0:
					self.textBox.tag_add(self.tags[0], lineStart, lineEnd)
					#print("Title")

				elif self.tabbed == 1:
					self.textBox.tag_add(self.tags[1], lineStart, lineEnd)
					#print("Subtitle")

				elif self.tabbed == 2:
					self.textBox.tag_add(self.tags[2], lineStart, lineEnd)
					#print("Text")

				lineNum += 1

			self.root.after(1000, self.updateTags)

		else:
			print("Tag updating disabled")