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
from os import remove
import platform
import frames
import bindings
import logging
import styles

## Main loop
class AppFrame(Frame):
	def __init__(self, master):
		self.master = master

		self.log = logging.Log(self)

		self.osStuff()
		self.initVars()
		self.initUI()

	def initVars(self):
		self.files = list()

		self.notesDir = getcwd() + "/notes"

	def initUI(self):
		self.log.write("Initialising UI")

		styles.init()

		## Top level frames
		try:
			self.titleBar = frames.titleBar(self, root)
			self.log.write(self.titleBar.testMessage)
		except Exception as ex:
			print("titleBar was not initialised properly")
			self.log.writeError("titleBar was not initialised properly. Error:\n" + str(ex))
			self.quit()

		try:
			self.formatBar = frames.formatBar(self)
			self.log.write(self.formatBar.testMessage)
		except Exception as ex:
			print("formatBar was not initialised properly")
			self.log.writeError("formatBar was not initialised properly. Error:\n" + str(ex))
			self.quit()

		try:
			self.arrangementFrame = frames.arrangementFrame(self)
			self.log.write(self.arrangementFrame.testMessage)
		except Exception as ex:
			print("arrangementFrame was not initialised properly")
			self.log.writeError("arrangementFrame was not initialised properly. Error:\n" + str(ex))
			self.quit()

		try:
			self.textFrame = frames.text(self.arrangementFrame, root)
			self.log.write(self.textFrame.testMessage)
		except Exception as ex:
			print("textFrame was not initialised properly")
			self.log.writeError("textFrame was not initialised properly. Error:\n" + str(ex))
			self.quit()

		"""try:
			self.tabBar = frames.tabBar(self.arrangementFrame)
			self.log.write(self.tabBar.testMessage)
		except Exception as ex:
			print("tabBar was not initialised properly")
			self.log.writeError("tabBar was not initialsed properly. Error:\n" + str(ex))
			self.quit()"""

		self.tabBar = frames.tabBar(self.arrangementFrame)

		try:
			bindings.init(self, root)
		except Exception as ex:
			print("bindings were not initialised properly")
			self.log.writeError("bindings were not initialised properly. Error:\n" + str(ex))
			self.quit()

		self.textFrame.textBox.focus_set()

		self.log.write("All initialised\n")

	def saveFile(self, mode):
		if mode == 1:
			# Save file
			print("Saving file")

			if(self.textFrame.fileName == ""):
				print("File has no name. Saving as")
				self.log.write("File has no name. Saving as")
				self.saveFile(2)
			else:
				saveLocation = self.textFrame.fileName

				fileToSave = open(saveLocation, "w+")

				textContents = self.textFrame.textBox.get("1.0", "end")
				fileToSave.write(textContents)

				print("Saved file at " + saveLocation)
				self.log.write("Saved file at " + saveLocation)

				fileToSave.close()

				self.textFrame.changed = False

		elif mode == 2:
			# Save file as
			fileContents = self.textFrame.textBox.get("1.0", "end")

			saveLocation = filedialog.asksaveasfilename(initialdir = self.notesDir, title = "Save note as", filetypes = [("Note files", "*.note")])
			self.textFrame.fileName = saveLocation

			if saveLocation is None or saveLocation is False or saveLocation is "" or saveLocation is "\n" or saveLocation == ():
				print("No save location selected. Cancelling")
				self.log.write("No save location selected. Cancelling")
			else:
				fileToSave = open(saveLocation, "w+")

				textContents = self.textFrame.textBox.get("1.0", "end")
				
				fileToSave.write(textContents)

				print("Saved file at " + saveLocation)
				self.log.write("Saved file at " + saveLocation)

				self.textFrame.fileName = saveLocation
				self.titleBar.title.config(text = "   " + saveLocation.split(self.slashChar)[-1].split(".")[-2])

				fileToSave.close()

				self.textFrame.changed = False

		elif mode == 3:
			# Rename
			fileContents = self.textFrame.textBox.get("1.0", "end")

			saveLocation = filedialog.asksaveasfilename(initialdir = self.notesDir, title = "Rename note to", filetypes = [("Note files", "*.note")])

			if saveLocation is None or saveLocation is False or saveLocation is "" or saveLocation is "\n" or saveLocation == ():
				print("No rename location selected. Cancelling")
			else:
				fileToSave = open(saveLocation, "w+")

				textContents = self.textFrame.textBox.get("1.0", "end")
				fileToSave.write(textContents)

				print("Renamed file to " + saveLocation)
				self.log.write("Renamed file to " + saveLocation)

				if self.textFrame.fileName != "":
					remove(self.textFrame.fileName)

				self.textFrame.fileName = saveLocation
				self.titleBar.title.config(text = "   " + saveLocation.split(self.slashChar)[-1].split(".")[-2])

				fileToSave.close()

				self.textFrame.changed = False

		else:
			print("saveFile index out of range")
			self.log.write("saveFile index out of range")

	def openFile(self):
		# Check whether textbox contents have changed. If yes, ask to save.
		if self.textFrame.changed == True:
			yesno = messagebox.askyesno("Save current file?", "The currently open file has not been saved. Save it?")

			if yesno:
				self.saveFile(1)
			else:
				self.textFrame.changed = False

		openLocation = filedialog.askopenfilename(initialdir = self.notesDir, title = "Select note to open", filetypes = [("Note files", "*.note")])

		if openLocation is None or openLocation is "" or openLocation is "\n" or openLocation is False or openLocation == ():
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

			self.textFrame.fileName = openLocation
			self.titleBar.title.config(text = "   " + self.textFrame.fileName.split(self.slashChar)[-1].split(".")[-2])

			print("Opening file from " + openLocation)
			self.log.write("Opening file from " + openLocation)

			self.textFrame.changed = False
		else:
			print("Error opening file. The \'changed\' variable may not have been correctly set.")
			self.log.writeError("Error opening file. The \'changed\' variable may not have been correctly set.")

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

	def osStuff(self):
		self.os = platform.system()

		if self.os == "Windows":
			self.slashChar = "\\"
		elif self.os == "Linux":
			self.slashChar = "/"
		elif self.os == "Darwin":
			self.slashChar = "/"
		else:
			self.log.wrteError("System not detected as Windows, Mac or Linux. Some features may not work.")
			print("System not detected as Windows, Mac or Linux. Some features may not work.")
			self.slashChar = "/"

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
root.protocol("WM_DELETE_WINDOW", app.quit)
root.mainloop()
