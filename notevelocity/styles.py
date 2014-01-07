"""
NoteVelocity - A speedy note-taking program.

Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under
    the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

You should have received a copy of the GNU General Public License along with
    this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from tkinter import *
from tkinter.ttk import *


def init(master):
    # Fonts
    buttonFont = ("Source Sans Pro", 10)
    smallButtonFont = ("Source Sans Pro", 8)
    titleFont = ("Source Sans Pro", 11, "bold")
    tabFont = ("Source Sans Pro", 10)
    textTitleFont = ("Source Sans Pro", 14)
    textSubtitleFont = ("Source Sans Pro", 12)
    textNotesFont = ("Source Sans Pro", 10)

    # Colours - these values should be in hexadecimal
    toolbarColour = "#E8E8E8"
    toolbarFontColour = "#303030"
    toolbarButtonColour = "#FFFFFF"

    tabColour = "#DDDDDD"
    tabSelectedColour = "#B8B8B8"

    textBoxBackground = "#FCFCFC"
    textBoxTextColour = "#444444"

    changedIndicatorOn = "#888888"
    changedIndicatorOff = "#E8E8E8"
    changedIndicatorText = "#101010"

    titleFontColour = "#000000"
    subtitleFontColour = "#222222"
    notesFontColour = "#444444"

    testHighlightingColour = "#FF0000"

    # Adding attributes to master
    master.textBoxBackground = textBoxBackground
    master.textBoxTextColour = textBoxTextColour
    master.titleFontColour = titleFontColour
    master.subtitleFontColour = subtitleFontColour
    master.notesFontColour = notesFontColour

    master.textTitleFont = textTitleFont
    master.textSubtitleFont = textSubtitleFont
    master.textNotesFont = textNotesFont

    # Styles (Do not edit)
    titleBarStyle = Style()
    titleBarStyle.configure(
        "TB.TFrame",
        background=toolbarColour)

    titleBarButtonStyle = Style()
    titleBarButtonStyle.configure(
        "TB.TButton",
        foreground=toolbarFontColour,
        background=toolbarButtonColour,
        width=7,
        font=buttonFont)

    formatButtonStyle = Style()
    formatButtonStyle.configure(
        "F.TButton",
        foreground=toolbarFontColour,
        background=toolbarButtonColour,
        width=3,
        font=buttonFont)

    titleStyle = Style()
    titleStyle.configure(
        "T.TLabel",
        foreground=toolbarFontColour,
        font=titleFont)

    tabBarStyle = Style()
    tabBarStyle.configure("TabBar.TFrame", background=toolbarColour)

    tabStyle = Style()
    tabStyle.configure("Tab.TFrame", background=tabColour)
    tabSelectedStyle = Style()
    tabSelectedStyle.configure(
        "TabSelected.TFrame", background=tabSelectedColour)

    tabButtonStyle = Style()
    tabButtonStyle.configure(
        "Tab.TButton",
        foreground=toolbarFontColour,
        background=toolbarButtonColour,
        font=smallButtonFont)

    tabTitleStyle = Style()
    tabTitleStyle.configure(
        "TT.TLabel",
        foreground=toolbarFontColour,
        background=tabColour,
        font=tabFont)

    tabTitleSelectedStyle = Style()
    tabTitleSelectedStyle.configure(
        "TTS.TLabel",
        foreground=toolbarFontColour,
        background=tabSelectedColour,
        font=tabFont)

    chIn = Style()
    chIn.configure(
        "CIOn.TFrame",
        width=20,
        height=20,
        background=changedIndicatorOn)

    chInOff = Style()
    chInOff.configure(
        "CIOff.TFrame",
        width=20,
        height=20,
        background=changedIndicatorOff)

    chInT = Style()
    chInT.configure(
        "CIText.TLabel",
        foreground=changedIndicatorText,
        background=changedIndicatorOn,
        font=tabFont)

    chInTOff = Style()
    chInTOff.configure(
        "CITextOff.TLabel",
        foreground=changedIndicatorOff,
        background=changedIndicatorOff,
        font=tabFont)

    highlightedFrame = Style()
    highlightedFrame.configure(
        "HL.TFrame",
        background=testHighlightingColour)
