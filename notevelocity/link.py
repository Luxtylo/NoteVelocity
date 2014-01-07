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
import styles

class LinkBox(Toplevel):
    def __init__(self, master):
        self.master = master

        noteSummaries = self.getNoteSummaries()

        self.initUI(noteSummaries)

        self.showSummaries(noteSummaries)

    def initUI(self, noteSummaries):
        """Initialise UI elements of LinkBox"""
        self.window = Toplevel()
        self.window.geometry("400x300")

        self.button = Button(self.window,
            text="Close",
            command=self.close)
        self.button.pack(side=BOTTOM, anchor=SE)
        
        self.canvasFrame = Frame(self.window,
            width=400,
            height=300)
        self.canvasFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.canvas = Canvas(self.canvasFrame)
        canvasHeight = 10 + len(noteSummaries) * 35
        self.canvas.config(height=canvasHeight)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollBar = Scrollbar(self.canvasFrame,
            orient=VERTICAL)
        self.scrollBar.pack(side=RIGHT, fill=Y, expand=0)

        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.scrollBar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollBar.set)

        """self.testButton = Button(self.canvasFrame, text="Test")
        self.testButtonWindow = self.canvas.create_window(10, 10,
            anchor=NW, window=self.testButton)"""

        self.window.lift()
    
    def getNoteSummaries(self):
        """Return the titles and subtitles of notes"""
        notesDir = self.master.notesDir
        notes = listdir(notesDir)

        noteSummaryList = list()

        for note in notes:
            noteLocation = notesDir + self.master.slashChar + str(note)
            noteSummary = list()

            with open(noteLocation, "r") as noteContents:
                lineNum = 1
                for line in noteContents:
                    tabs = 0
                    for char in line:
                        if char == "\t":
                            tabs += 1
                    
                    if tabs == 0 or tabs == 1:
                        summary = [lineNum, line]

                    lineNum += 1
                    noteSummary.append(summary)

            noteType = note.split(".")[-1]
            
            noteSummaryList.append([str(note), noteSummary])

        return noteSummaryList

    def close(self):
        """Close the window"""
        self.window.destroy()

    def showSummaries(self, noteSummaries):
        sortedSummaries = sorted(noteSummaries,
            key=lambda x: x[0])
        noteDisplayList = list()
        notesToIgnore = list()

        self.summaryFrame = Frame(self.canvasFrame, width=380)

        summaryNumber = 0
        for summ in sortedSummaries:
            # noteType will be "note" or "rewrite"
            noteType = str(summ[0]).split(".")[-1]

            note = NoteSummary(self, summaryNumber, summ)

            noteDisplayList.append(note)

            summaryNumber += 1

        self.summaryWindow = self.canvas.create_window(1, 1,
            anchor=NW, window=self.summaryFrame)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

class NoteSummary():
    def __init__(self, master, number, summary):
        #print(summary)
        self.master = master
        self.number = number
        self.summary = summary

        self.name = str(summary[0]).split(".")[:-1]
        if len(self.name) > 24:
            self.name = self.name[:21] + "..."
            
        self.nOrR = str(summary[0]).split(".")[-1]
        if self.nOrR == "note":
            self.nOrR = "N"
        elif self.nOrR == "rewrite":
            self.nOrR = "R"
        else:
            print("Extension of " + self.name + " not right")

        x = 10
        y = 10 + 35 * number

        """self.frame = Frame(self.master.summaryFrame, width=380)
        self.frame.pack(fill=X, expand=1, side=TOP, ipady=2)

        self.label = Label(self.frame, text=self.name)
        self.label.pack(expand=0, side=LEFT, padx=4)

        self.paddingFrame = Frame(self.frame, width=50)
        self.paddingFrame.pack(fill=BOTH, expand=1, side=LEFT)

        self.expandButton = Button(self.frame, text="E", width=2)
        self.expandButton.pack(expand=0, side=RIGHT)"""

        self.expandButton = Button(self.master.summaryFrame,
            text="E",
            width=2)
        self.linkButton = Button(self.master.summaryFrame, text="L", width=2)
        self.label = Label(self.master.summaryFrame, text = self.name)
        self.noteOrRewrite = Label(self.master.summaryFrame, text=self.nOrR)

        self.expandButton.grid(row=number, column=0)
        self.linkButton.grid(row=number, column=1)
        self.label.grid(row=number, column=2, sticky=W)
        self.noteOrRewrite.grid(row=number, column=3, sticky=E)

        """self.window = self.master.canvas.create_window(x, y,
            anchor=NW, window=self.frame)"""

        self.addRows(summary)

    def addRows(self, summary):
        pass

    def addTitle(self):
        pass
