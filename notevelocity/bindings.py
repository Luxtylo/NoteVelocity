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

# Main
def init(self, root):
	print("bindings initialised")

	root.bind("<Control-s>", lambda event: self.saveFile(1))
	root.bind("<Control-S>", lambda event: self.saveFile(2))
	root.bind("<Control-r>", lambda event: self.saveFile(3))