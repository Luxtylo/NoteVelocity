"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Imports
from tkinter import *
from tkinter.ttk import *

# Change key bindings here
save = "<Control-s>"
saveAs = "<Control-S>"
rename = "<Control-r>"
openFile = "<Control-o>"

quit = "<Control-w>"

decreaseIndent = "<Control-Shift-space>"
increaseIndent = "<Control-space>" # Or the tab key when at the start of a line

makeTitle = "<Control-t>"
makeSubtitle = "<Control-T>"

margins = 2

# Main
def init(self, root):
	print("bindings initialised")

	# Saving
	root.bind(save, lambda event: self.saveFile(1))
	root.bind(saveAs, lambda event: self.saveFile(2))
	root.bind(rename, lambda event: self.saveFile(3))

	# Opening
	root.bind(openFile, lambda event: self.openFile())

	# Quit
	root.bind(quit, lambda event: self.quit())