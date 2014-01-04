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
from os import listdir

class LinkBox(Toplevel):
    def __init__(self, master):
        self.master = master

        self.initUI()

        noteSummaries = self.getNoteSummaries()

    def initUI(self):
        self.window = Toplevel()

        self.button = Button(self.window,
            text="Close",
            command=self.close)
        self.button.pack(side=BOTTOM, anchor=SE)
        
        self.canvasFrame = Frame(self.window,
            width=400,
            height=300)
        self.canvasFrame.pack(side=TOP)

        self.canvas = Canvas(self.canvasFrame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=0)

        self.scrollBar = Scrollbar(self.canvasFrame,
            orient=VERTICAL)
        self.scrollBar.pack(side=RIGHT, fill=Y, expand=0)

        self.scrollBar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollBar.set)

        self.testButton = Button(self.canvasFrame, text="Test")
        self.testButtonWindow = self.canvas.create_window(10, 10,
            anchor=NW, window=self.testButton)

        self.test = NoteSummary(self, 10, 40)

        self.window.lift()
    
    def getNoteSummaries(self):
        notesDir = self.master.notesDir
        notes = listdir(notesDir)

        noteSummaryList = list()

        for note in notes:
            noteLocation = notesDir + self.master.slashChar + str(note)
            noteSummary = list()

            with open(noteLocation, "r") as noteContents:
                for line in noteContents:
                    tabs = 0
                    for char in line:
                        if char == "\t":
                            tabs += 1
                    
                    if tabs == 0:
                        noteSummary.append(line)
                    elif tabs == 1:
                        noteSummary.append(line)
            
            noteSummaryList.append([str(note), noteSummary])

        return noteSummaryList

    def close(self):
        self.window.destroy()

class NoteSummary():
    def __init__(self, master, x, y):
        self.master = master

        self.testButton = Button(self.master.canvasFrame, text="Test")
        self.testButtonWindow = self.master.canvas.create_window(x, y,
            anchor=NW, window=self.testButton)
