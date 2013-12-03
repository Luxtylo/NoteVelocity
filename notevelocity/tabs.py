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
from tkinter import messagebox
import bindings


class tabBar(Frame):

    def __init__(self, master):
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
        newTabNum = len(self.tabs)
        self.tabs.append(self.tab(self, title))

        self.switch(1, len(self.tabs) - 1)

        self.tabs[self.selectedTab].changed = False

    def switch(self, mode, amount):
        self.lastSelectedTab = self.selectedTab

        if mode == 0:  # Add amount to tabNum
            if self.selectedTab + amount < len(self.tabs) and self.selectedTab + amount >= 0:
                self.selectedTab += amount

            elif self.selectedTab + amount >= len(self.tabs) - 1:
                self.selectedTab = 0

            elif self.selectedTab + amount < 0:
                self.selectedTab = len(self.tabs) - 1

        elif mode == 1:  # Switch to tab amount
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
        textBoxContents = self.master.master.textFrame.textBox.get(1.0, "end")
        textBoxContents = textBoxContents[:-1]
        self.tabs[last].text.set(textBoxContents)

        self.master.master.textFrame.textBox.delete(1.0, "end")
        textBoxContents = self.tabs[new].text.get()
        self.master.master.textFrame.textBox.insert(1.0, textBoxContents)

        self.master.master.titleBar.title.config(
            text=self.tabs[self.selectedTab].longTitle)

        # Update textBox properties
        self.tabs[last].fileName = self.master.master.textFrame.fileName
        self.master.master.textFrame.fileName = self.tabs[new].fileName

        self.tabs[last].changed = self.master.master.textFrame.changed
        self.master.master.textFrame.changed = self.tabs[new].changed

    def updateFilename(self):
        self.tabs[
            self.selectedTab].fileName = self.master.master.textFrame.fileName

    def closeCurrent(self):
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

    def save(self):
        self.updateFilename()

        if self.tabs[self.selectedTab].changed or self.master.master.textFrame.changed:
            yesno = messagebox.askyesno(
                title="Save note?",
                message="The tab has been changed. Would you like to save?")

            if yesno:
                return self.master.master.saveFile(1)
            else:
                return 0

        else:
            #print(str(self.tabs[self.selectedTab].changed) + " " + str(self.master.master.textFrame.changed))
            return 0

    def renameCurrent(self, name):
        self.tabs[self.selectedTab].rename(name)

    def change(self):
        self.tabs[self.selectedTab].change = True

    def resetChanged(self):
        self.tabs[self.selectedTab].change = False

    def checkFilename(self):
        return self.tabs[self.selectedTab].fileName

    def checkChanged(self):
        #self.tabs[self.selectedTab].changed = self.master.master.textFrame.changed
        return self.tabs[self.selectedTab].changed

    class tab():

        def __init__(self, master, title):
            self.master = master

            self.text = StringVar()
            self.text.set("")
            self.text.trace("w", lambda *args: self.changeMade())

            self.Frame = Frame(self.master.Frame, style="Tab.TFrame")

            self.changed = False
            self.fileName = ""

            self.title = Label(self.Frame, style="TT.TLabel")
            self.rename(title)

            self.titleBox = Entry(self.Frame, width=20)
            self.titleBox.insert(0, title)

            self.closeButton = Button(
                self.Frame, style="Tab.TButton", text="X", width=1, takefocus=0)

            self.bindings()

            self.show()

        def bindings(self):
            self.title.bind("<Button-1>", lambda event:
                            self.master.switch(1, self.findPlace()))
            self.Frame.bind("<Button-1>", lambda event:
                            self.master.switch(1, self.findPlace()))
            self.closeButton.bind("<Button-1>", lambda event:
                                  self.master.closeSpecific(self.findPlace()))

        def findPlace(self):
            return self.master.tabs.index(self)

        def show(self):
            self.Frame.pack(side=LEFT, expand=0, ipadx=2,
                            ipady=2, padx=4, pady=2)
            self.title.pack(side=LEFT, expand=0,
                            ipadx=4, ipady=2, padx=4)
            self.closeButton.pack(
                side=LEFT, expand=0, ipadx=1, ipady=0)

            self.select()

        def select(self):
            self.Frame.config(style="TabSelected.TFrame")
            self.title.config(style="TTS.TLabel")

        def deselect(self):
            self.Frame.config(style="Tab.TFrame")
            self.title.config(style="TT.TLabel")

        def rename(self, name):
            self.longTitle = "   " + name
            if len(name) > 16:
                name = name[:16] + "..."
            self.title.config(text=name)

        def changeMade(self):
            self.changed = True

        def changeSaved(self):
            self.changed = False

        def close(self):
            self.Frame.pack_forget()

            # save file
