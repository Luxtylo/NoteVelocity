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

	def saveFile(self, rename):
		if rename == True:
			pass
		else:
			pass

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
windowWidth = int(screenWidth * 3 / 4)
windowHeight = int(screenHeight * 3 / 4)

if screenWidth <=1024 or screenHeight <= 768:
	root.geometry(str(windowWidth) + "x" + str(windowHeight))
	print("Resolution set to %dx%d" % (windowWidth, windowHeight))
elif screenWidth == 1024 and screenHeight == 768:
	root.geometry(str(windowWidth) + "x" + str(windowHeight))
	print("Resolution set to %dx%d" % (windowWidth, windowHeight))
else:
	root.geometry("800x600")

# Remove title bar
#root.overrideredirect(1)

# Make window centred on startup
windowXPos = (screenWidth - windowWidth) / 2
windowYPos = (screenHeight - windowHeight) / 2
root.geometry("+%d+%d" % (windowXPos, windowYPos))

root.focus()

## Start main loop
app = AppFrame(root)
root.mainloop()
