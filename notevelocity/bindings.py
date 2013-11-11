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

nextTab = "<Control-d>"
prevTab = "<Control-D>"
newTab = "<Control-n>"
newTabTwo = "<Control-t>"
closeTab = "<Control-w>"

quit = "<Control-W>"

decreaseIndent = "<Control-Shift-space>"
increaseIndent = "<Control-space>" # Or the tab key when at the start of a line

makeHeading = "<Control-h>"
makeSubheading = "<Control-H>"

# Binding (Do not edit)
def init(self, root):
	print("bindings initialised")

	# Saving
	root.bind(save, lambda event: self.saveFile(1))
	root.bind(saveAs, lambda event: self.saveFile(2))
	root.bind(rename, lambda event: self.saveFile(3))

	# Opening
	root.bind(openFile, lambda event: self.openFile())

	# Tab control
	root.bind(nextTab, lambda event: self.tabBar.switch(0, 1))
	root.bind(prevTab, lambda event: self.tabBar.switch(0, -1))
	root.bind(newTab, lambda event: self.tabBar.add(self, "New Note"))
	root.bind(newTabTwo, lambda event: self.tabBar.add(self, "New Note"))
	root.bind(closeTab, lambda event: self.tabBar.closeCurrent())

	root.bind(makeHeading, lambda event: print("Making heading"))
	root.bind(makeSubheading, lambda event: print("Making subheading"))

	# Quit
	root.bind(quit, lambda event: self.quit())