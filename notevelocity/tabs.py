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
from tkinter import messagebox
from copy import deepcopy


class tabBar(Frame):

    def __init__(self, master):
        """Initialise tabBar using its methods"""
        self.master = master

        self.testMessage = "tabBar is initialised"

        self.Frame = Frame(height=24, style="TabBar.TFrame")
        self.Frame.pack(fill=X, expand=0, side=BOTTOM)

        self.tabs = list()
        self.blank = StringVar()
        self.blank.set("")

        self.lastSelectedTab = 0
        self.selectedTab = 0

        self.add(self, "New Note")

    def add(self, master, title):
        """Add a new tab"""
        self.tabs.append(self.tab(self, title))

        self.switch(1, len(self.tabs) - 1)

        self.tabs[self.selectedTab].changed = False

    def switch(self, mode, amount):
        """Switch tabs
        Modes:
            0:  Add amount to tabNum
            1:  Switch to tab amount"""
        self.lastSelectedTab = self.selectedTab

        if mode == 0:
            if (self.selectedTab + amount < len(self.tabs) and
                    self.selectedTab + amount >= 0):
                self.selectedTab += amount

            elif self.selectedTab + amount >= len(self.tabs) - 1:
                self.selectedTab = 0

            elif self.selectedTab + amount < 0:
                self.selectedTab = len(self.tabs) - 1

        elif mode == 1:
            if amount < len(self.tabs) and amount >= 0:
                self.selectedTab = amount

            elif amount < 0:
                self.selectedTab = 0

            elif amount >= len(self.tabs):
                self.selectedTab = len(self.tabs) - 1

        self.tabs[self.lastSelectedTab].deselect()
        self.tabs[self.selectedTab].select()
        self.swapBoxContents(self.lastSelectedTab, self.selectedTab)
        self.master.master.updateChanged()

    def swapBoxContents(self, last, new):
        """Swap the contents of the textboxes"""
        textBoxContents = self.master.master.textFrame.textBox.get(1.0, "end")
        textBoxContents = textBoxContents[:-1]
        self.tabs[last].text.set(textBoxContents)

        self.master.master.textFrame.textBox.delete(1.0, "end")
        textBoxContents = self.tabs[new].text.get()
        self.master.master.textFrame.textBox.insert(1.0, textBoxContents)

        self.master.master.titleBar.title.config(
            text=self.tabs[self.selectedTab].longTitle)

        # Switch rewrite boxes
        rewriteBoxContents = self.master.master.textFrame.rewriteBox.get(
            1.0,
            "end")
        rewriteBoxContents = rewriteBoxContents[:-1]
        self.tabs[last].rewrite.set(rewriteBoxContents)

        self.master.master.textFrame.rewriteBox.delete(1.0, "end")
        rewriteBoxContents = self.tabs[new].rewrite.get()
        self.master.master.textFrame.rewriteBox.insert(1.0, rewriteBoxContents)

        # Update textBox properties
        self.tabs[last].fileName = self.master.master.textFrame.fileName
        self.master.master.textFrame.fileName = self.tabs[new].fileName

        self.tabs[last].changed = self.master.master.textFrame.changed
        self.master.master.textFrame.changed = self.tabs[new].changed

        self.tabs[last].rewriteExists = self.master.master.textFrame.rewriteExists

        self.updateLinks(last, new)

    def updateLinks(self, last, new):
        if len(self.tabs) > 1:
            self.tabs[last].textLinks = deepcopy(self.master.master.textFrame.textLinks)
            #self.master.master.textFrame.textLinks = self.tabs[new].textLinks

            self.tabs[last].rewriteLinks = deepcopy(self.master.master.textFrame.rewriteLinks)
            #self.master.master.textFrame.rewriteLinks = self.tabs[new].rewriteLinks

            self.master.master.textFrame.updateLinks(
                self.tabs[new].textLinks,
                self.tabs[new].rewriteLinks)

    def updateFilename(self):
        """Update the current tab's filename"""
        self.tabs[
            self.selectedTab].fileName = self.master.master.textFrame.fileName

    def closeCurrent(self):
        """Close the current tab"""
        errorCheck = self.save()

        if errorCheck == 0:
            if len(self.tabs) > 1:
                self.switch(1, self.selectedTab - 1)

                self.tabs[self.lastSelectedTab].close()
                del self.tabs[self.lastSelectedTab]
            else:
                self.lastSelectedTab = 0
                self.selectedTab = 0

                self.tabs[self.lastSelectedTab].close()
                del self.tabs[0]

                self.add(self, "New Note")
                self.master.master.textFrame.textBox.delete(1.0, "end")
                self.master.master.textFrame.textBox.insert(
                    1.0, self.blank.get())

    def closeSpecific(self, tabNum):
        """Close tab with number tabNum"""
        errorCheck = self.save()

        if errorCheck == 0 or errorCheck == 1:
            if tabNum < self.selectedTab:
                self.tabs[tabNum].close()
                del self.tabs[tabNum]
                self.selectedTab -= 1

            elif tabNum > self.selectedTab:
                self.tabs[tabNum].close()
                del self.tabs[tabNum]

            else:  # if the selected tab is the one being closed
                if tabNum == 0:  # if it's the first tab
                    if len(self.tabs) == 1:  # if it's the only tab
                        self.tabs[tabNum].close()
                        del self.tabs[tabNum]
                        self.add(self, "New Note")

                    else:  # if it's not the only tab
                        self.tabs[tabNum].close()
                        del self.tabs[tabNum]
                        self.selectedTab = 0
                        self.switch(1, self.selectedTab)

                elif tabNum == len(self.tabs) - 1:  # if it's the last tab
                    self.tabs[tabNum].close()
                    del self.tabs[tabNum]

                    if self.selectedTab == tabNum:
                        self.selectedTab -= 1

                    self.switch(1, self.selectedTab)

                else:  # if it's somewhere in the middle
                    if self.selectedTab == tabNum:
                        self.selectedTab -= 1

                    self.tabs[tabNum].close()
                    del self.tabs[tabNum]
                    self.switch(1, self.selectedTab)

    def save(self, *tab):
        """Save the contents of the textbox"""
        if tab is int():
            tabToSave = tab
        else:
            tabToSave = self.selectedTab

        self.updateFilename()

        if (self.tabs[tabToSave].changed or
                self.master.master.textFrame.changed):
            yesno = messagebox.askyesno(
                title="Save note?",
                message="The tab has been changed. Would you like to save?")

            if yesno:
                a = self.master.master.saveFile(1)
                b = self.master.master.saveFile(4)
                if a == 1 or b == 1:
                    return 1
                else:
                    return 0
            else:
                return 0

        else:
            return 0

    def renameCurrent(self, name):
        """Rename the current tab"""
        self.tabs[self.selectedTab].rename(name)

    def change(self):
        """Mark the current tab as changed"""
        self.tabs[self.selectedTab].change = True

    def resetChanged(self):
        """Mark the current tab as unchanged"""
        self.tabs[self.selectedTab].change = False

    def checkFilename(self):
        """Return the filename of the current tab"""
        return self.tabs[self.selectedTab].fileName

    def checkChanged(self):
        """Return the change state of the current tab"""
        return self.tabs[self.selectedTab].changed

    class tab():

        def __init__(self, master, title):
            """Initialises tab using its internal functions"""
            self.master = master

            self.text = StringVar()
            self.text.set("")
            self.text.trace("w", lambda *args: self.changeMade())

            self.rewrite = StringVar()
            self.rewrite.set("")
            self.rewrite.trace("w", lambda *args: self.changeMade())

            self.textLinks = {}
            self.rewriteLinks = {}

            self.rewriteExists = False

            self.Frame = Frame(self.master.Frame, style="Tab.TFrame")

            self.changed = False
            self.fileName = ""

            self.title = Label(self.Frame, style="TT.TLabel")
            self.rename(title)

            self.titleBox = Entry(self.Frame, width=20)
            self.titleBox.insert(0, title)

            self.closeButton = Button(
                self.Frame,
                style="Tab.TButton",
                text="X",
                width=1,
                takefocus=0)

            self.bindings()

            self.show()

        def bindings(self):
            """Initialise tab bindings"""
            self.title.bind(
                "<Button-1>",
                lambda event: self.master.switch(1, self.findPlace())
                )

            self.Frame.bind(
                "<Button-1>",
                lambda event: self.master.switch(1, self.findPlace())
                )

            self.closeButton.bind(
                "<Button-1>",
                lambda event: self.master.closeSpecific(self.findPlace())
                )

        def findPlace(self):
            """Find the number of this tab"""
            return self.master.tabs.index(self)

        def show(self):
            """Make tab visible"""
            self.Frame.pack(side=LEFT, expand=0, ipadx=2,
                            ipady=2, padx=4, pady=2)
            self.title.pack(side=LEFT, expand=0,
                            ipadx=4, ipady=2, padx=4)
            self.closeButton.pack(
                side=LEFT, expand=0, ipadx=1, ipady=0)

            self.select()

        def select(self):
            """Make tab appear selected"""
            self.Frame.config(style="TabSelected.TFrame")
            self.title.config(style="TTS.TLabel")

        def deselect(self):
            """Make tab appear deselected"""
            self.Frame.config(style="Tab.TFrame")
            self.title.config(style="TT.TLabel")

        def rename(self, name):
            """Rename tab to name"""
            self.longTitle = "   " + name
            if len(name) > 16:
                name = name[:16] + "..."
            self.title.config(text=name)

        def changeMade(self):
            """Indicate change"""
            self.changed = True

        def changeSaved(self):
            """Indicate no change"""
            self.changed = False

        def close(self):
            """Close tab"""
            self.Frame.pack_forget()

            # save file
