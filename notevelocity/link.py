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

        self.test = Toplevel()

        self.button = Button(self.test, text="Press me", command=self.getNoteList)
        self.button.pack()

        self.test.lift()
    
    def getNoteList(self):
        notesDir = self.master.notesDir
        notes = listdir(notesDir)
        print(notes)

    def close(self):
        self.test.destroy()
