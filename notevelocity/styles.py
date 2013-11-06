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
	tabFont = ("Source Sans Pro", 10)

	# Colours - these values should be in hexadecimal
	toolbarColour = "#E8E8E8"
	toolbarFontColour = "#303030"
	toolbarButtonColour = "#FFFFFF"

	# Styles (Do not edit)
	titleBarStyle = Style()
	titleBarStyle.configure("TB.TFrame", background = toolbarColour)

	titleBarButtonStyle = Style()
	titleBarButtonStyle.configure("TB.TButton", foreground = toolbarFontColour, background = toolbarButtonColour, width = 7, font = buttonFont)

	formatButtonStyle = Style()
	formatButtonStyle.configure("F.TButton", foreground = toolbarFontColour, background = toolbarButtonColour, width = 3, font = buttonFont)

	titleStyle = Style()
	titleStyle.configure("T.TLabel", foreground = toolbarFontColour, font = titleFont)

	tabBarStyle = Style()
	tabBarStyle.configure("TabBar.TFrame", background = toolbarColour)

	tabStyle = Style()
	tabStyle.configure("Tab.TFrame", background = toolbarButtonColour)

	tabButtonStyle = Style()
	tabButtonStyle.configure("Tab.TButton", foreground = toolbarFontColour, background = toolbarButtonColour, font = buttonFont)

	tabTitleStyle = Style()
	tabTitleStyle.configure("TT.TLabel", foreground = toolbarFontColour, background = toolbarButtonColour, font = tabFont)