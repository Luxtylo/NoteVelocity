"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from tkinter import *
from tkinter.ttk import *

def init():
	# Fonts
	buttonFont = ("Source Sans Pro", 10)
	titleFont = ("Source Sans Pro", 11, "bold")

	# Styles
	titleBarButtonStyle = Style()
	titleBarButtonStyle.configure("TB.TButton", foreground = "#333", background = "#FFF", width = 7, font = buttonFont)

	formatButtonStyle = Style()
	formatButtonStyle.configure("F.TButton", foreground = "#333", background = "#FFF", width = 3, font = buttonFont)

	titleStyle = Style()
	titleStyle.configure("T.TLabel", foreground = "#444", font = titleFont)