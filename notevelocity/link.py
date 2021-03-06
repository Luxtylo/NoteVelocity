"""
NoteVelocity - A speedy note-taking program.

Copyright (C) 2014  George Bryant

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


def link(app, box):
    """Choose the note to link to"""
    selectedNote = filedialog.askopenfilename(
        initialdir=app.notesDir,
        title="Select a note to link to",
        filetypes=[
            ("NoteVelocity files", ("*note", "*.rewrite")),
            ("Notes", "*.note"), ("Rewrites", "*.rewrite")])

    if not app.selection:
        app.selection = app.textFrame.getSelection()

    contents = getNoteTitles(selectedNote)
    if contents != 1:
        getLinkLocation(app, contents, selectedNote, box)
    else:
        print("No note selected")
        app.log.write("No note selected")


def getNoteTitles(noteName):
    """Get the titles of the selected note"""
    contentsList = []

    if noteName != () and noteName != "" and noteName is not None:
        lineNum = 1
        for line in open(noteName, "r"):
            tabs = 0
            for char in line:
                if char == "\t":
                    tabs += 1

            if tabs < 2:
                contentsList.append([tabs, line, lineNum])

            lineNum += 1

        return contentsList

    else:
        return 1


def getLinkLocation(app, noteContents, noteName, box):
    """Get a location to link to

    Returns:
        [noteName, None] if whole note is being linked to
        [noteName, lineNum] if linking to a line
        False if going back
        None if cancelled

    Output is not directly returned, but rather calls app.insertLink"""

    def selectNote():
        """Select current note"""
        linkLocation = [noteName, None]
        linkBox.destroy()
        app.insertLink(linkLocation, box)

    def back(app):
        """Go back to note selection"""
        linkBox.destroy()
        app.openLinkBox()
        app.insertLink(False)

    def cancel():
        """Close the linkBox"""
        linkBox.destroy()
        app.insertLink(None)

    def ok(listBox):
        """Get the selected line"""
        if listBox.curselection() != ():
            selectionIndex = int(listBox.curselection()[0])
            linkLocation = [noteName, noteContents[selectionIndex][2]]
            linkBox.destroy()
            app.insertLink(linkLocation, box)

    linkBox = Toplevel()
    linkBox.title("Select point in note to link to")

    topSection = Frame(linkBox)
    topSection.pack(side=TOP, fill=BOTH, expand=1)

    listBox = Listbox(topSection)
    listBox.config(width=60, height=15)
    listBox.pack(side=LEFT, fill=BOTH, expand=1)

    scrollBar = Scrollbar(topSection, orient=VERTICAL)
    scrollBar.pack(side=RIGHT, fill=Y, expand=1)

    scrollBar.config(command=listBox.yview)
    listBox.config(yscrollcommand=scrollBar.set)

    bottomSection = Frame(linkBox)
    bottomSection.pack(side=BOTTOM, fill=X, expand=0)

    cancelButton = Button(bottomSection, text="Cancel", command=cancel)
    cancelButton.pack(side=RIGHT)

    listBox.bind("<Double-Button-1>", lambda event: ok(listBox))

    backButton = Button(
        bottomSection,
        text="Back",
        command=lambda: back(app))
    backButton.pack(side=RIGHT)

    """selectNote = Button(
        bottomSection,
        text="Link note",
        command=selectNote)
    selectNote.pack(side=RIGHT)"""

    select = Button(
        bottomSection,
        text="Link",
        command=lambda: ok(listBox))
    select.pack(side=RIGHT)

    insertList(noteContents, listBox)


def insertList(noteContents, listBox):
    """Insert the note's contents into the listBox"""
    for line in noteContents:
        line[1] = line[1][:-1]
        if line[0] == 0:
            listBox.insert(END, line[1])
        else:
            listBox.insert(END, "    " + line[1][1:])
