"""NoteVelocity - A speedy note-taking program.

Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under
    the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your
    option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
    more details.

You should have received a copy of the GNU General Public License along with
    this program.  If not, see <http://www.gnu.org/licenses/>.

"""

## Imports
from tkinter import *
from tkinter.ttk import *
import bindings
import styles

## Main
# Title bar
class titleBar(Frame):
    """Bar along the top of the program.
    Contains:
        Button A - Save, Save as, rename
        Button B - Open, Rewrite"""
    def __init__(self, master, root):

        self.master = master
        self.root = root

        self.testMessage = "titleBar is initialised"

        self.Frame = Frame(style = "TB.TFrame")
        self.Frame.pack(fill = X, side = TOP, expand = 0, ipadx = 2, ipady = 2)

        self.icon = Frame(self.Frame)
        self.icon.pack(expand = 0, side = LEFT)

        self.buttonA = Button(self.Frame, text = "Save", style = "TB.TButton", takefocus = 0)
        self.buttonA.pack(expand = 0, side = LEFT)

        self.buttonB = Button(self.Frame, text = "Open", style = "TB.TButton", takefocus = 0)
        self.buttonB.pack(expand = 0, side = LEFT)

        self.title = Label(self.Frame, text = "   New note", anchor = "w", style = "T.TLabel")
        self.title.pack(expand = 1, fill = BOTH, side = LEFT)

        self.changedIndicator = Frame(self.Frame, style = "CIOff.TFrame", height = 20)
        self.changedIndicator.pack(expand = 0, fill = Y, side = RIGHT)

        self.changedIndicatorText = Label(self.changedIndicator, style = "CITextOff.TLabel", text = "Changed")
        self.changedIndicatorText.pack(expand = 0, side = RIGHT, padx = 4)

        self.Bindings()

    def Bindings(self):
        """Change function of buttons depending on keys held."""
        self.buttonA.bind("<Enter>", lambda event: self.buttonASave())
        self.buttonA.bind("<Leave>", lambda event: self.buttonASave())

        self.buttonA.bind("<Shift-Enter>", lambda event: self.buttonASaveAs())
        self.buttonA.bind("<Shift-Leave>", lambda event: self.buttonASave())

        self.buttonA.bind("<Control-Enter>", lambda event: self.buttonARename())
        self.buttonA.bind("<Control-Leave>", lambda event: self.buttonASave())

        self.buttonB.bind("<Enter>", lambda event: self.buttonBOpen())
        self.buttonB.bind("<Leave>", lambda event: self.buttonBOpen())

        self.buttonB.bind("<Control-Enter>", lambda event: self.buttonBRewrite())
        self.buttonB.bind("<Control-Leave>", lambda event: self.buttonBRewrite())

    def buttonASave(self):
        """Change button A to function as a save button"""
        self.buttonA.config(text = "Save", command = lambda: self.master.saveFile(1))

    def buttonASaveAs(self):
        """Change button A to function as a save as button"""
        self.buttonA.config(text = "Save As", command = lambda: self.master.saveFile(2))

    def buttonARename(self):
        """Change button A to function as a rename button"""
        self.buttonA.config(text = "Rename", command = lambda: self.master.saveFile(3))

    def buttonBOpen(self):
        """Change button B to function as an open button"""
        self.buttonB.config(text = "Open", command = lambda: self.master.openFile())

    def buttonBRewrite(self):
        """Change button B to function as a rewrite button"""
        self.buttonB.config(text = "Rewrite", command = lambda: self.master.rewriteFile())

    def changed(self):
        """Change changedIndicator to show a change"""
        self.changedIndicator.config(style = "CIOn.TFrame")
        self.changedIndicatorText.config(style = "CIText.TLabel")

    def unChanged(self):
        """Change changedIndicator to show no change"""
        self.changedIndicator.config(style = "CIOff.TFrame")
        self.changedIndicatorText.config(style = "CITextOff.TLabel")

# Formatting bar
class formatBar(Frame):
    """Formatting bar down the left side of the program"""
    def __init__(self, master):

        self.master = master

        self.testMessage = "formatBar is initialised"

        self.Frame = Frame(style = "TB.TFrame")
        self.Frame.pack(fill = Y, side = LEFT, expand = 0, ipadx = 2, ipady = 2)

        self.spacer1 = Frame(self.Frame, height = 2)
        self.spacer1.pack(expand = 0, side = TOP)

        self.title = Button(self.Frame, text = "T", style = "F.TButton", takefocus = 0)
        self.title.pack(expand = 0, side = TOP)
        self.title.bind("<Button-1>", lambda event: self.master.textFrame.makeLevel("title"))

        self.subTitle = Button(self.Frame, text = "S", style = "F.TButton", takefocus = 0)
        self.subTitle.pack(expand = 0, side = TOP)
        self.subTitle.bind("<Button-1>", lambda event: self.master.textFrame.makeLevel("subtitle"))

        self.notes = Button(self.Frame, text = "N", style = "F.TButton", takefocus = 0)
        self.notes.pack(expand = 0, side = TOP)
        self.notes.bind("<Button-1>", lambda event: self.master.textFrame.makeLevel("notes"))

        self.spacer2 = Frame(self.Frame, height = 5)
        self.spacer2.pack(expand = 0, side = TOP)

        self.equation = Button(self.Frame, text = "E", style = "F.TButton", takefocus = 0)
        self.equation.pack(expand = 0, side = TOP)

        self.settings = Button(self.Frame, text = "Set", style = "F.TButton", takefocus = 0)
        self.settings.pack(expand = 0, side = BOTTOM, padx = 2, pady = 4)

# Text Frame
class text(Frame):
    """Contains the text box which is typed into"""
    def __init__(self, master, root):

        self.master = master
        self.root = root

        self.testMessage = "textFrame is initialised"

        self.Frame = Frame(style = "TB.TFrame")
        self.Frame.pack(fill = BOTH, expand = 1, side = TOP)

        self.scrollbar = Scrollbar(self.Frame)
        self.scrollbar.pack(expand = 0, fill = Y, side = RIGHT)

        self.textBox = Text(self.Frame)
        self.textBox.pack(expand = 1, fill = BOTH, side = LEFT)
        self.textBox.config(tabs = ("0.5c", "0.75c", "0.825c"), borderwidth = 0)
        self.textBox.config(bg = master.master.textBoxBackground, fg = master.master.textBoxTextColour)

        # Link self.textBox and self.scrollbar
        self.textBox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.textBox.yview)

        # Bind Enter to newLine
        self.textBox.bind("<Return>", lambda event: self.newLine())

        self.textBox.bind(bindings.increaseIndent, self.increaseIndent)
        self.textBox.bind(bindings.decreaseIndent, self.decreaseIndent)

        self.textBox.bind("<<Modified>>", lambda event: self.modified())

        self.changed = False
        self.fileName = ""
        self.shortFileName = self.fileName.split("/")[-1]

    def newLine(self):
        """Make new lines but keep their indentation"""
        self.tabbed = 0

        # Get current line
        lineNum, columnNum = self.textBox.index("insert").split(".")
        line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

        for char in line:
            if char == "\t":
                self.tabbed += 1

            else:
                break

        if self.tabbed != 0:
            insertIndex = str(int(lineNum) + 1) + ".0"
            insertTabs = "\n" + "\t" * self.tabbed
            self.textBox.insert(insertIndex, insertTabs)

        else:
            insertIndex = str(int(lineNum) + 1) + ".0"
            self.textBox.insert(insertIndex, "\n")

        return "break"

    def decreaseIndent(self, event):
        """Decrease the indent of the current line by one tab"""
        self.tabbed = 0

        # Get current line
        lineNum, columnNum = self.textBox.index("insert").split(".")
        line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

        for char in line:
            if char == "\t":
                self.tabbed += 1

            else:
                break

        if self.tabbed != 0:
            deleteStart = lineNum + ".0"
            deleteEnd = lineNum + ".1"
            self.textBox.delete(deleteStart, deleteEnd)

        return "break"

    def increaseIndent(self, event):
        """Increase the indent of the current line by one tab"""
        lineNum, columnNum = self.textBox.index("insert").split(".")

        insertIndex = lineNum + ".0"

        self.textBox.insert(insertIndex, "\t")

    def makeLevel(self, level):
        """Set the number of tab chars before start of the current line to 'level'"""
        index = self.textBox.index("insert").split(".")[0]
        lineStart = index + ".0"
        lineEnd = index + ".end"

        line = self.textBox.get(lineStart, lineEnd)

        numberTabs = 0

        for char in line:
            if char == "\t":
                numberTabs += 1
            else:
                break

        deleteStart = lineStart
        deleteEnd = index + "." + str(numberTabs)

        self.textBox.delete(deleteStart, deleteEnd)

        if level == "title":
            pass
        elif level == "subtitle":
            self.textBox.insert(deleteStart, "\t")
        elif level == "notes":
            self.textBox.insert(deleteStart, "\t\t")

    def modified(self):
        """Show that the contents of the textBox have been modified"""
        self.changed = True
        self.master.titleBar.changed()

class arrangementFrame(Frame):
    """Frame to make arrangement of textFrame and tabBar work properly"""
    def __init__(self, master):
        self.master = master

        self.testMessage = "arrangementFrame is initialised"

        self.titleBar = self.master.titleBar

        self.Frame = Frame()
        self.Frame.pack(side = LEFT)

