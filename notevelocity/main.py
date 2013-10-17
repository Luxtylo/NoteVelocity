"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os import getcwd
import frames
import bindings
import logging

## Main loop
class AppFrame(Frame):
	def __init__(self, master):
		self.master = master

		self.log = logging.Log(self)

		self.initVars()
		self.initUI()

	def initVars(self):
		self.files = list()

		self.notesDir = getcwd() + "/notes"

	def initUI(self):
		self.log.write("Initialising UI")

		## Top level frames
		try:
			self.titleBar = frames.titleBar(self, root)
			self.log.write(self.titleBar.testMessage)
		except:
			print("titleBar was not initialised properly")
			self.log.write("titleBar was not initialised properly")
			self.quit()

		try:
			self.formatBar = frames.formatBar(self)
			self.log.write(self.formatBar.testMessage)
		except:
			print("formatBar was not initialised properly")
			self.log.write("formatBar was not initialised properly")
			self.quit()

		try:
			self.textFrame = frames.text(self, root)
			self.log.write(self.textFrame.testMessage)
		except:
			print("textFrame was not initialised properly")
			self.log.write("textFrame was not initialised properly")
			self.quit()

		try:
			bindings.init(self, root)
		except:
			print("bindings were not initialised properly")
			self.log.write("bindings were not initialised properly")
			self.quit()

	def saveFile(self, mode):
		if mode == 1:
			# Save file
			print("Saving file")

			if(self.textFrame.fileName == ""):
				print("File has no name")
				self.saveFile(2)
			else:
				fileContents = self.textFrame.textBox.get("1.0", "end")

				saveLocation = filedialog.asksaveasfilename(initialdir = self.notesDir, title = "SAVING", filetypes = [("Note files", "*.note"), ("Text files", "*.txt"), ("All files", "*")])

				self.textFrame.changed = False

		elif mode == 2:
			# Save file as
			fileContents = self.textFrame.textBox.get("1.0", "end")

			saveLocation = filedialog.asksaveasfilename(initialdir = self.notesDir, title = "Save note as", filetypes = [("Note files", "*.note"), ("Text files", "*.txt"), ("All files", "*")])
			self.textFrame.fileName = saveLocation

			if saveLocation is None or saveLocation is False or saveLocation is "" or saveLocation is "\n":
				print("No save location selected")
			else:
				fileToSave = open(saveLocation, "w+").close()

				textContents = self.textFrame.textBox.get("1.0", "end")
				print(textContents)
				fileToSave.write(textContents)

				print("Saved file at " + saveLocation)

				self.textFrame.changed = False

		elif mode == 3:
			# Rename
			print("Renaming file to <filename>")
		else:
			print("saveFile index out of range")
			self.log.write("saveFile index out of range")

	def open(self):
		# Check whether textbox contents have changed. If yes, ask to save.
		if self.textFrame.changed == True:
			yesno = messagebox.askyesno("Save current file?", "The currently open file has not been saved. Save it?")

			if yesno is True:
				self.saveFile(1)

		openLocation = filedialog.askopenfilename(initialdir = self.notesDir, title = "Select note to open", filetypes = [("Note files", "*.note"), ("Text files", "*.txt"), ("All files", "*")])

		if openLocation is None or openLocation is "" or openLocation is "\n" or openLocation is False:
			print("No open location selected")
			self.log.write("No open location selected")
		elif self.textFrame.changed == False:
			openFile = open(openLocation, "r")

			self.textFrame.textBox.delete("1.0", "end")

			lineNum = 1

			for line in openFile:
				insertLoc = str(lineNum) + ".0"
				self.textFrame.textBox.insert(insertLoc, line)
				
				lineNum += 1

			print("Opening file from " + openLocation)
			self.log.write("Opening file from " + openLocation)
		else:
			print("Error opening file. The \'changed\' variable may not have been correctly set.")

	def max(self):
		pass

	def min(self):
		pass

	def quit(self):
		print("Closing NoteVelocity...")
		self.log.write("Closing NoteVelocity...")
		self.log.close()

		global root
		root.destroy()
		raise SystemExit

	def log(self, mode):
		if mode == 0:
			pass
		elif mode == 1:
			pass

	def initStyles(self):
		s = Style()

# Set root window properties
root = Tk()

root.title("NoteVelocity")
root.minsize(640,480)

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
windowWidth = int(screenWidth * 3 / 4)
windowHeight = int(screenHeight * 3 / 4)

if screenWidth <=1024 or screenHeight <= 768:
	root.geometry("%dx%d" % (windowWidth, windowHeight))
	print("Resolution set to %dx%d" % (windowWidth, windowHeight))
elif screenWidth == 1024 and screenHeight == 768:
	root.geometry("%dx%d" % (windowWidth, windowHeight))
	print("Resolution set to %dx%d" % (windowWidth, windowHeight))
else:
	root.geometry("800x600")
	print("Resolution set to default 800x600")

# Make window centred on startup
windowXPos = (screenWidth - windowWidth) / 2
windowYPos = (screenHeight - windowHeight) / 2
root.geometry("+%d+%d" % (windowXPos, windowYPos))

# Make sure window is focused at startup
root.focus_set()

## Start main loop
app = AppFrame(root)
root.mainloop()
