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
from tkinter import filedialog
from os import getcwd
from os import remove
from os import path
import platform
import frames
import tabs
import bindings
import logging
import styles


class AppFrame(Frame):

    def __init__(self, master):
        """Initialise Appframe by running other functions"""
        self.master = master

        self.log = logging.Log(self)

        self.osStuff()
        self.initVars()
        self.initUI()

    def initVars(self):
        """Initialise necessary variables."""
        # Probably unused
        #self.files = list()

        self.notesDir = getcwd() + "/notes"

    def getFocus(self):
        return self.master.focus_get()

    def initUI(self):
        """Initialise UI elements."""
        self.log.write("Initialising UI")

        styles.init(self)

        # Top level frames
        """try:
            self.titleBar = frames.titleBar(self, root)
            self.log.write(self.titleBar.testMessage)
        except Exception as ex:
            print("titleBar was not initialised properly")
            self.log.writeError(
                "titleBar was not initialised properly. Error:\n" + str(ex))
            self.quit()"""
        self.titleBar = frames.titleBar(self, root)

        try:
            self.formatBar = frames.formatBar(self)
            self.log.write(self.formatBar.testMessage)
        except Exception as ex:
            print("formatBar was not initialised properly")
            self.log.writeError(
                "formatBar was not initialised properly. Error:\n" + str(ex))
            self.quit()

        try:
            self.arrangementFrame = frames.arrangementFrame(self)
            self.log.write(self.arrangementFrame.testMessage)
        except Exception as ex:
            print("arrangementFrame was not initialised properly")
            e = "arrangementFrame was not initialised properly. Error:\n"
            e += str(ex)
            self.log.writeError(e)
            self.quit()

        try:
            self.textFrame = frames.text(self.arrangementFrame, root)
            self.log.write(self.textFrame.testMessage)
        except Exception as ex:
            print("textFrame was not initialised properly")
            e = "textFrame was not initialised properly. Error:\n"
            e += str(ex)
            self.log.writeError(e)
            self.quit()

        try:
            self.tabBar = tabs.tabBar(self.arrangementFrame)
            self.log.write(self.tabBar.testMessage)
        except Exception as ex:
            print("tabBar was not initialised properly")
            self.log.writeError(
                "tabBar was not initialised properly. Error:\n" + str(ex))
            self.quit()

        try:
            bindings.init(self, root)
        except Exception as ex:
            print("bindings were not initialised properly")
            self.log.writeError(
                "bindings were not initialised properly. Error:\n" + str(ex))
            self.quit()

        self.textFrame.textBox.focus_set()

        self.log.write("All initialised\n")

    def saveFile(self, mode):
        """Save current file.
        Modes:
            1:  Save file
            2:  Save file as
            3:  Rename file
            4:  Save rewrite file"""
        if mode == 1:
            # Save file
            print("Saving file")

            if not self.textFrame.changed and not self.tabBar.checkChanged:
                print("Not changed, so not saving.")
                self.log.write("Not changed, so not saving")
                return 0
            elif self.textFrame.fileName == "":
                print("File has no name. Saving as")
                self.log.write("File has no name. Saving as")
                return self.saveFile(2)
            else:
                saveLocation = self.textFrame.fileName

                fileToSave = open(saveLocation, "w+")

                textContents = self.textFrame.textBox.get("1.0", "end")
                fileToSave.write(textContents)

                print("Saved file at " + saveLocation)
                self.log.write("Saved file at " + saveLocation)

                fileToSave.close()

                self.textFrame.changed = False
                self.tabBar.resetChanged()
                self.indicateNoChange()

                if self.textFrame.rewriteExists:
                    self.saveFile(4)

                return 0

        elif mode == 2:
            # Save file as
            saveLocation = filedialog.asksaveasfilename(
                initialdir=self.notesDir,
                title="Save note as",
                filetypes=[("Note files", "*.note")])
            self.textFrame.fileName = saveLocation
            self.tabBar.updateFilename()

            returnedNothing = [None, False, "", "\n", ()]

            if saveLocation in returnedNothing:
                print("No save location selected. Cancelling")
                self.log.write("No save location selected. Cancelling")
                return 1
            else:
                fileToSave = open(saveLocation, "w+")

                textContents = self.textFrame.textBox.get("1.0", "end")

                fileToSave.write(textContents)

                print("Saved file at " + saveLocation)
                self.log.write("Saved file at " + saveLocation)

                self.textFrame.fileName = saveLocation
                self.tabBar.tabs[
                    self.tabBar.selectedTab].fileName = saveLocation
                shortName = saveLocation.split(
                    self.slashChar)[-1].split(".")[-2]
                self.titleBar.title.config(text="   " + shortName)
                self.tabBar.renameCurrent(shortName)

                fileToSave.close()

                self.textFrame.changed = False
                self.tabBar.resetChanged()
                self.indicateNoChange()

                if self.textFrame.rewriteExists:
                    self.saveFile(4)

                return 0

        elif mode == 3:
            # Rename
            saveLocation = filedialog.asksaveasfilename(
                initialdir=self.notesDir,
                title="Rename note to", filetypes=[("Note files", "*.note")])

            returnedNothing = [None, False, "", "\n", ()]

            if saveLocation in returnedNothing:
                print("No rename location selected. Cancelling")
                return 1
            else:
                fileToSave = open(saveLocation, "w+")

                textContents = self.textFrame.textBox.get("1.0", "end")
                fileToSave.write(textContents)

                print("Renamed file to " + saveLocation)
                self.log.write("Renamed file to " + saveLocation)

                if self.textFrame.fileName != "":
                    remove(self.textFrame.fileName)

                self.textFrame.fileName = saveLocation
                self.tabBar.tabs[
                    self.tabBar.selectedTab].fileName = saveLocation
                shortName = saveLocation.split(
                    self.slashChar)[-1].split(".")[-2]
                self.titleBar.title.config(text="   " + shortName)
                self.tabBar.renameCurrent(shortName)

                fileToSave.close()

                self.textFrame.changed = False
                self.tabBar.resetChanged()
                self.indicateNoChange()

                if self.textFrame.rewriteExists:
                    self.saveFile(4)

                return 0

        if mode == 4:
            # Save rewrite

            if not self.textFrame.changed and not self.tabBar.checkChanged:
                print("Not changed, so not saving.")
                self.log.write("Not changed, so not saving")
                return 0
            elif self.textFrame.fileName == "":
                print("File has no name. Saving as")
                self.log.write("File has no name. Saving as")
                errorCheck = self.saveFile(2)
                if errorCheck == 0:
                    return self.saveFile(4)
                else:
                    return 1
            else:
                fileNameMinusNote = self.textFrame.fileName.split(".")[:-1]
                saveLocation = ".".join(fileNameMinusNote) + ".rewrite"
                fileToSave = open(saveLocation, "w+")

                textContents = self.textFrame.rewriteBox.get("1.0", "end")
                fileToSave.write(textContents)

                print("Saved rewrite at " + saveLocation)
                self.log.write("Saved rewrite at " + saveLocation)

                fileToSave.close()

                self.textFrame.changed = False
                self.tabBar.resetChanged()
                self.indicateNoChange()

                return 0

        else:
            print("saveFile index out of range")
            self.log.write("saveFile index out of range")
            return 0

    def openFile(self):
        """Open a file in a new tab"""
        openLocation = filedialog.askopenfilename(
            initialdir=self.notesDir,
            title="Select note to open",
            filetypes=[("Note files", "*.note")])

        returnedNothing = [None, False, "", "\n", ()]

        if openLocation in returnedNothing:
            print("No open location selected")
            self.log.write("No open location selected")
        else:
            openFile = open(openLocation, "r")

            self.textFrame.fileName = openLocation
            shortName = self.textFrame.fileName.split(
                self.slashChar)[-1].split(".")[-2]
            self.tabBar.add(self.tabBar, shortName)
            self.tabBar.tabs[self.tabBar.selectedTab].fileName = openLocation
            self.titleBar.title.config(text="   " + shortName)

            self.textFrame.textBox.delete("1.0", "end")

            lineNum = 1

            for line in openFile:
                insertLoc = str(lineNum) + ".0"
                self.textFrame.textBox.insert(insertLoc, line)

                lineNum += 1

            print("Opened file from " + openLocation)
            self.log.write("Opened file from " + openLocation)

            fileNameMinusNote = openLocation.split(".")[:-1]
            rewriteLocation = ".".join(fileNameMinusNote) + ".rewrite"
            
            if path.isfile(rewriteLocation):
                rewriteFile = open(rewriteLocation, "r")

                self.textFrame.rewriteBox.delete("1.0", "end")

                lineNum = 1

                for line in rewriteFile:
                    insertLoc = str(lineNum) + ".0"
                    self.textFrame.rewriteBox.insert(insertLoc, line)

                    lineNum += 1

                print("Opened rewrite from " + rewriteLocation)
                self.log.write("Opened rewrite from " + rewriteLocation)

            self.textFrame.changed = False
            self.textFrame.fileName = openLocation
            self.tabBar.resetChanged()
            self.indicateNoChange()

    def updateChanged(self):
        """Update visual change indicator"""
        if self.textFrame.changed:
            self.indicateChange()
        elif not self.textFrame.changed:
            self.indicateNoChange()

    def indicateChange(self):
        """Visually indicate a change"""
        self.titleBar.changed()

    def indicateNoChange(self):
        """Visually indicate no change"""
        self.titleBar.unChanged()

        self.textFrame.hideRewrite()

    def quit(self):
        """Quit NoteVelocity"""
        print("Closing NoteVelocity...")
        self.log.write("Closing NoteVelocity...")
        self.log.close()

        global root
        root.destroy()
        raise SystemExit

    def osStuff(self):
        """Operating system specifics"""
        self.os = platform.system()

        if self.os == "Windows":
            self.slashChar = "\\"
        elif self.os == "Linux":
            self.slashChar = "/"
        elif self.os == "Darwin":
            self.slashChar = "/"
        else:
            self.log.writeError(
                "System not detected as Windows, Mac or Linux."
                " Some features may not work.")
            print(
                "System not detected as Windows, Mac or Linux."
                " Some features may not work.")
            self.slashChar = "/"

# Set root window properties
root = Tk()

root.title("NoteVelocity")
root.minsize(640, 480)

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
windowWidth = int(screenWidth * 3 / 4)
windowHeight = int(screenHeight * 3 / 4)

if screenWidth <= 1024 or screenHeight <= 768:
    root.geometry("%dx%d" % (windowWidth, windowHeight))
    print("Resolution set to %dx%d" % (windowWidth, windowHeight))
elif screenWidth == 1024 and screenHeight == 768:
    root.geometry("%dx%d" % (windowWidth, windowHeight))
    print("Resolution set to %dx%d" % (windowWidth, windowHeight))
else:
    root.geometry("800x600")
    print("Resolution set to default 800x600")

# Make window centred on startup
windowXPos = (screenWidth - windowWidth) / 2
windowYPos = (screenHeight - windowHeight) / 2
root.geometry("+%d+%d" % (windowXPos, windowYPos))

# Make sure window is focused at startup
root.focus_set()

# Start main loop
app = AppFrame(root)
root.protocol("WM_DELETE_WINDOW", app.quit)
root.mainloop()
