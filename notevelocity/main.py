"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
import tkinter as tk

## Main loop
class AppFrame(tk.Frame):
	def __init__(self, parent):
		self.parent = parent

		self.initUI()

	def initUI(self):
		print("Initialising UI...")

# Set root window properties
root = tk.Tk()

root.title("NoteVelocity - New Note")
root.minsize(640,480)

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

if screenWidth <=1024 or screenHeight <= 768:
	windowWidth = screenWidth * 3 / 4
	windowHeight = screenHeight * 3 / 4
	root.geometry("%dx%d",(windowWidth,windowHeight))
else:
	root.geometry("800x600")

## Start main loop
app = AppFrame(root)
root.mainloop()
