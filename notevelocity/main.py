"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *
import frames

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

		## Top level frames
		try:
			self.titleBar = frames.titleBar(self, root)
			print(self.titleBar.testMessage)
		except:
			print("titleBar was not initialised properly")
			self.quit()

		try:
			self.formatBar = frames.formatBar(self)
			print(self.formatBar.testMessage)
		except:
			print("formatBar was not initialised properly")
			self.quit()

		try:
			self.textFrame = frames.text(self)
			print(self.textFrame.testMessage)
		except:
			print("textFrame was not initialised properly")
			self.quit()

	def saveFile(self, mode):
		if mode == 1:
			# Save file
			print("Saving file")
		elif mode == 2:
			# Save file as
			print("Saving file as <filename>")
		elif mode == 3:
			# Rename
			print("Renaming file to <filename>")
		else:
			print("saveFile index out of range")

	def open(self):
		pass

	def max(self):
		pass

	def min(self):
		pass

	def quit(self):
		print("Closing NoteVelocity...")

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
