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
		self.titleBar = frames.titleBar(self)

		try:
			print(self.titleBar.test)
		except:
			print("titleBar was not initialised properly")

	def saveFile(self, rename):
		if rename == True:
			pass
		else:
			pass

	def open(self):
		pass

	def quit(self):
		root.quit()

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
	print("%dx%d" % (windowWidth, windowHeight))
else:
	root.geometry("800x600")

## Start main loop
app = AppFrame(root)
root.mainloop()
