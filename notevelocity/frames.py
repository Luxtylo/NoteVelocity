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
from time import sleep
import bindings
from copy import deepcopy


class titleBar(Frame):

    def __init__(self, master, root):
        """Initialise titlebar"""

        self.master = master
        self.root = root

        self.testMessage = "titleBar is initialised"

        self.Frame = Frame(style="TB.TFrame")
        self.Frame.pack(
            fill=X,
            side=TOP,
            expand=0,
            ipadx=2,
            ipady=2)

        self.icon = Frame(self.Frame)
        self.icon.pack(expand=0, side=LEFT)

        self.buttonA = Button(
            self.Frame,
            text="Save",
            style="TB.TButton",
            takefocus=0)
        self.buttonA.pack(expand=0, side=LEFT)

        self.buttonB = Button(
            self.Frame,
            text="Open",
            style="TB.TButton",
            takefocus=0)
        self.buttonB.pack(expand=0, side=LEFT)

        self.title = Label(
            self.Frame,
            text="   New note",
            anchor="w",
            style="T.TLabel")
        self.title.pack(expand=1, fill=BOTH, side=LEFT)

        self.rewriteSave = Button(
            self.Frame,
            text="Save",
            style="TB.TButton",
            takefocus=0)

        self.rewriteHide = Button(
            self.Frame,
            text="Hide",
            style="TB.TButton",
            takefocus=0)

        self.changedIndicator = Frame(
            self.Frame,
            style="CIOff.TFrame",
            height=20)
        self.changedIndicator.pack(expand=0, fill=Y, side=RIGHT)

        self.changedIndicatorText = Label(
            self.changedIndicator,
            style="CITextOff.TLabel",
            text="Changed")
        self.changedIndicatorText.pack(expand=0, side=RIGHT, padx=4)

        self.Bindings()

    def Bindings(self):
        """Initialise bindings"""
        self.buttonA.bind("<Enter>", lambda event: self.buttonASave())
        self.buttonA.bind("<Leave>", lambda event: self.buttonASave())

        self.buttonA.bind("<Shift-Enter>", lambda event: self.buttonASaveAs())
        self.buttonA.bind("<Shift-Leave>", lambda event: self.buttonASave())

        self.buttonA.bind(
            "<Control-Enter>", lambda event: self.buttonARename())
        self.buttonA.bind("<Control-Leave>", lambda event: self.buttonASave())

        self.buttonB.bind("<Enter>", lambda event: self.buttonBOpen())
        self.buttonB.bind("<Leave>", lambda event: self.buttonBOpen())

        self.buttonB.bind(
            "<Control-Enter>", lambda event: self.buttonBRewrite())
        self.buttonB.bind(
            "<Control-Leave>", lambda event: self.buttonBRewrite())

    def buttonASave(self):
        """Make button A save"""
        self.buttonA.config(
            text="Save", command=lambda: self.master.saveFile(1))

    def buttonASaveAs(self):
        """Make button A save as"""
        self.buttonA.config(
            text="Save As", command=lambda: self.master.saveFile(2))

    def buttonARename(self):
        """Make button A rename"""
        self.buttonA.config(
            text="Rename", command=lambda: self.master.saveFile(3))

    def buttonBOpen(self):
        """Make button B open"""
        self.buttonB.config(
            text="Open", command=lambda: self.master.openFile())

    def buttonBRewrite(self):
        """Make button B rewrite"""
        self.buttonB.config(
            text="Rewrite",
            command=lambda: self.master.textFrame.toggleRewrite())

    def changed(self):
        """Activate visual change indicator"""
        self.changedIndicator.config(style="CIOn.TFrame")
        self.changedIndicatorText.config(style="CIText.TLabel")

    def unChanged(self):
        """Deactivate visual change indicator"""
        self.changedIndicator.config(style="CIOff.TFrame")
        self.changedIndicatorText.config(style="CITextOff.TLabel")

    def showRewrite(self):
        """Show the rewrite controls"""
        self.rewriteSave.pack(expand=0, side=RIGHT)
        self.rewriteHide.pack(expand=0, side=RIGHT)
        self.rewriteBindings()

    def hideRewrite(self):
        """Hide the rewrite controls"""
        self.rewriteSave.pack_forget()
        self.rewriteHide.pack_forget()

    def rewriteBindings(self):
        """Bind the rewrite buttons"""
        self.rewriteSave.config(command=lambda: self.master.saveFile(4))
        self.rewriteHide.config(command=lambda: self.master.textFrame.hideRewrite())


class formatBar(Frame):

    def __init__(self, master):
        """Initialise formatbar"""

        self.master = master

        self.testMessage = "formatBar is initialised"

        self.Frame = Frame(style="TB.TFrame")
        self.Frame.pack(fill=Y, side=LEFT, expand=0, ipadx=2, ipady=2)

        self.spacer1 = Frame(self.Frame, height=2)
        self.spacer1.pack(expand=0, side=TOP)

        self.title = Button(
            self.Frame, text="T", style="F.TButton", takefocus=0)
        self.title.pack(expand=0, side=TOP)
        self.title.bind(
            "<Button-1>",
            lambda event: self.master.textFrame.makeLevel("title"))

        self.subTitle = Button(
            self.Frame, text="S", style="F.TButton", takefocus=0)
        self.subTitle.pack(expand=0, side=TOP)
        self.subTitle.bind(
            "<Button-1>",
            lambda event: self.master.textFrame.makeLevel("subtitle"))

        self.notes = Button(
            self.Frame, text="N", style="F.TButton", takefocus=0)
        self.notes.pack(expand=0, side=TOP)
        self.notes.bind(
            "<Button-1>",
            lambda event: self.master.textFrame.makeLevel("notes"))

        """self.spacer2 = Frame(self.Frame, height=5)
        self.spacer2.pack(expand=0, side=TOP)
        self.equation = Button(
            self.Frame, text="E", style="F.TButton", takefocus=0)
        self.equation.pack(expand=0, side=TOP)"""

        self.spacer3 = Frame(self.Frame, height=5)
        self.spacer3.pack(expand=0, side=TOP)

        self.rewriteToggle = Button(
            self.Frame, text="R", style="F.TButton", takefocus=0)
        self.rewriteToggle.pack(expand=0, side=TOP)
        self.rewriteToggle.bind(
            "<Button-1>", lambda event: self.master.textFrame.toggleRewrite())

        """self.settings = Button(
            self.Frame, text="Set", style="F.TButton", takefocus=0)
        self.settings.pack(expand=0, side=BOTTOM, padx=2, pady=4)"""


class text(Frame):

    def __init__(self, master, root):
        """Initialise textFrame"""

        self.master = master
        self.root = root

        self.testMessage = "textFrame is initialised"

        self.Frame = Frame(style="TB.TFrame")
        self.Frame.pack(fill=BOTH, expand=1, side=TOP)

        self.textBox = Text(self.Frame)
        self.textBox.config(
            tabs=("0.25c", "0.4c", "0.4c"),
            borderwidth=0,
            width=1,
            wrap=WORD,
            bg=master.master.textBoxBackground,
            fg=master.master.notesFontColour,
            font=master.master.textNotesFont)
        self.textBox.pack(expand=1, fill=BOTH, side=LEFT)

        self.scrollbar = Scrollbar(self.Frame)
        self.scrollbar.pack(expand=0, fill=Y, side=LEFT)

        self.rewriteBox = Text(self.Frame)
        self.rewriteBox.config(
            tabs=("0.25c", "0.4c", "0.4c"),
            borderwidth=0,
            width=1,
            wrap=WORD,
            bg=master.master.textBoxBackground,
            fg=master.master.notesFontColour,
            font=master.master.textNotesFont)

        self.rewriteScrollbar = Scrollbar(self.Frame)

        # Link textboxes and scrollbars
        self.textBox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textBox.yview)
        self.rewriteBox.config(yscrollcommand=self.rewriteScrollbar.set)
        self.rewriteScrollbar.config(command=self.rewriteBox.yview)

        # Bind Enter to newLine
        self.textBox.bind("<Return>", lambda event: self.newLine())
        self.rewriteBox.bind("<Return>", lambda event: self.newLine())

        self.textBox.bind(bindings.increaseIndent, self.increaseIndent)
        self.textBox.bind(bindings.decreaseIndent, self.decreaseIndent)

        self.rewriteBox.bind(bindings.increaseIndent, self.increaseIndent)
        self.rewriteBox.bind(bindings.decreaseIndent, self.decreaseIndent)

        self.textBox.bind("<<Modified>>", lambda event: self.modified())
        self.rewriteBox.bind("<<Modified>>", lambda event: self.rewriteModified())
        self.textBox.bind("<Key>", lambda event: self.updateTags())
        self.rewriteBox.bind("<Key>", lambda event: self.updateTags())

        # Bind link shortcut to link selection
        self.textBox.bind(
            bindings.linkNote,
            lambda event: self.master.master.openLinkBox("textBox"))
        self.rewriteBox.bind(
            bindings.linkNote,
            lambda event: self.master.master.openLinkBox("rewriteBox"))

        self.initTags()
        self.startHypManagers()

        self.selectedBox = 0
        self.changed = False
        self.rewriteShown = False
        self.rewriteExists = False
        
        self.changeCounter = 0

        self.fileName = ""
        self.shortFileName = self.fileName.split("/")[-1]

        self.updateTime = 0
        self.tagsUpToDate = False
        self.updateTags()
        self.checkChanges()

    def newLine(self):
        """Make new lines keep the same indentation"""
        self.tabbed = 0

        focus = self.master.master.getFocus()
        if focus is self.textBox:
            lineNum, columnNum = self.textBox.index("insert").split(".")
            line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")
        elif focus is self.rewriteBox:
            lineNum, columnNum = self.rewriteBox.index("insert").split(".")
            line = self.rewriteBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

        for char in line:
            if char == "\t":
                self.tabbed += 1

            else:
                break

        if self.tabbed != 0:
            insertIndex = str(int(lineNum) + 1) + ".0"
            insertTabs = "\n" + "\t" * self.tabbed

            if focus is self.textBox:
                self.textBox.insert(insertIndex, insertTabs)
            elif focus is self.rewriteBox:
                self.rewriteBox.insert(insertIndex, insertTabs)

        else:
            insertIndex = str(int(lineNum) + 1) + ".0"

            if focus is self.textBox:
                self.textBox.insert(insertIndex, "\n")
            elif focus is self.rewriteBox:
                self.rewriteBox.insert(insertIndex, "\n")

        return "break"

    def decreaseIndent(self, event):
        """Decrease the line indent"""
        self.tabbed = 0

        # Get current line
        lineNum, columnNum = self.textBox.index("insert").split(".")
        line = ""

        focus = self.master.master.getFocus()
        if focus is self.textBox:
            line = self.textBox.get(str(lineNum) + ".0", str(lineNum) + ".end")
        elif focus is self.rewriteBox:
            line = self.rewriteBox.get(str(lineNum) + ".0", str(lineNum) + ".end")

        for char in line:
            if char == "\t":
                self.tabbed += 1

            else:
                break

        if self.tabbed != 0:
            deleteStart = lineNum + ".0"
            deleteEnd = lineNum + ".1"
            if focus is self.textBox:
                self.textBox.delete(deleteStart, deleteEnd)
            elif focus is self.rewriteBox:
                self.rewriteBox.delete(deleteStart, deleteEnd)

        self.updateTags()

        return "break"

    def increaseIndent(self, event):
        """Increase the line indent"""
        focus = self.master.master.getFocus()
        if focus is self.textBox:
            lineNum, columnNum = self.textBox.index("insert").split(".")
            insertIndex = lineNum + ".0"
            self.textBox.insert(insertIndex, "\t")
        elif focus is self.rewriteBox:
            lineNum, columnNum = self.rewriteBox.index("insert").split(".")
            insertIndex = lineNum + ".0"
            self.rewriteBox.insert(insertIndex, "\t")

        self.updateTags()

    def makeLevel(self, level):
        """Make the line a specific level"""
        if self.master.master.getFocus() is self.textBox:
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
        elif self.master.master.getFocus() is self.rewriteBox:
            index = self.rewriteBox.index("insert").split(".")[0]
            lineStart = index + ".0"
            lineEnd = index + ".end"

            line = self.rewriteBox.get(lineStart, lineEnd)

            numberTabs = 0

            for char in line:
                if char == "\t":
                    numberTabs += 1
                else:
                    break

            deleteStart = lineStart
            deleteEnd = index + "." + str(numberTabs)

            self.rewriteBox.delete(deleteStart, deleteEnd)

            if level == "title":
                pass
            elif level == "subtitle":
                self.rewriteBox.insert(deleteStart, "\t")
            elif level == "notes":
                self.rewriteBox.insert(deleteStart, "\t\t")

            self.updateTags

    def modified(self):
        """Mark as changed"""
        self.changed = True
        self.master.titleBar.changed()
        self.tagUpToDate = False
        self.updateTags()

    def rewriteModified(self):
        """Mark as changed, and mark as rewriteExists"""
        self.changed = True
        self.master.titleBar.changed()
        self.rewriteExists = True
        self.tagsUpToDate = False
        self.updateTags()

    def selectText(self):
        """Select the textbox"""
        self.selectedBox = 0
        self.textBox.focus_set()
        if self.changed:
            self.master.titleBar.changed()
        else:
            self.master.titleBar.unChanged()

    def selectRewrite(self):
        """Select the rewrite box"""
        self.selectedBox = 1
        self.rewriteBox.focus_set()
        if self.changed:
            self.master.titleBar.changed()
        else:
            self.master.titleBar.unChanged()

    def showRewrite(self):
        """Show the rewrite box"""
        self.rewriteBox.pack(expand=1, fill=BOTH, side=LEFT)
        self.master.titleBar.showRewrite()
        self.rewriteScrollbar.pack(expand=0, fill=Y, side=LEFT)
        self.rewriteShown = True
        self.selectRewrite()
        self.changeCounter = 5
        self.updateTags(self.rewriteBox)

        rewriteContents = self.rewriteBox.get(1.0, "end")
        if rewriteContents == "" or rewriteContents == "\n":
            self.rewriteExists = False
        else:
            self.rewriteExists = True

    def hideRewrite(self):
        """Hide the rewrite box"""
        self.rewriteBox.pack_forget()
        self.master.titleBar.hideRewrite()
        self.rewriteScrollbar.pack_forget()
        self.rewriteShown = False
        self.selectText

        rewriteContents = self.rewriteBox.get(1.0, "end")
        if rewriteContents == "" or rewriteContents == "\n":
            self.rewriteExists = False
        else:
            self.rewriteExists = True

    def toggleRewrite(self):
        """Toggle the rewrite box"""
        if self.rewriteShown:
            self.hideRewrite()
        else:
            self.showRewrite()

    def initTags(self):
        """Initialise self.textBox tags"""
        self.textBox.tag_config(
            "title",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.titleFontColour,
            font=self.master.master.textTitleFont
            )
        self.textBox.tag_config(
            "subtitle",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.subtitleFontColour,
            font=self.master.master.textSubtitleFont)
        self.textBox.tag_config(
            "notes",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.notesFontColour,
            font=self.master.master.textNotesFont)

        self.rewriteBox.tag_config(
            "title",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.titleFontColour,
            font=self.master.master.textTitleFont
            )
        self.rewriteBox.tag_config(
            "subtitle",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.subtitleFontColour,
            font=self.master.master.textSubtitleFont)
        self.rewriteBox.tag_config(
            "notes",
            background=self.master.master.textBoxBackground,
            foreground=self.master.master.notesFontColour,
            font=self.master.master.textNotesFont)
        
        self.textBox.tag_raise("sel")
        self.rewriteBox.tag_raise("sel")

    def updateTags(self, box=False):
        """Update tags for self.textBox or self.rewriteBox"""
        if self.changeCounter < 2:
            self.changeCounter += 1
            self.tagsUpToDate = False
        else:
            if not box:
                self.getTagIndexes()
                self.addTags()
            else:
                self.getTagIndexes(box)
                self.addTags(box)
            self.updateLinks(self.textLinks, self.rewriteLinks)
            self.changeCounter = 0
            self.updateTime = self.master.master.getTime()
            self.tagsUpToDate = True

    def getTagIndexes(self, box=False):
        """Find points in the textBox widget where tags should be added"""
        if not box:
            focus = self.master.master.getFocus()
        else:
            focus = box

        if focus is self.rewriteBox:
            text = self.rewriteBox.get(1.0, "end").split("\n")
            self.rewriteTagIndexList = list()
        else: #Assume focus is self.textBox
            text = self.textBox.get(1.0, "end").split("\n")
            self.tagIndexList = list()
        
        lineNum = 1
        for line in text:
            tabs = 0
            for char in line:
                if char == "\t":
                    tabs += 1

            lineStr = str(lineNum)
            startIndex = lineStr + ".0"
            endIndex = lineStr + ".end"
            
            if focus is self.textBox:
                self.tagIndexList.append((startIndex, endIndex, tabs))
            elif focus is self.rewriteBox:
                self.rewriteTagIndexList.append((startIndex, endIndex, tabs))

            lineNum += 1

    def addTags(self, box=False):
        """Add tags to the textBox from tagIndexList"""
        if not box:
            focus = self.master.master.getFocus()
        else:
            focus = box

        if focus is self.textBox:
            self.textBox.tag_delete("title", "subtitle", "notes")
        elif focus is self.rewriteBox:
            self.rewriteBox.tag_delete("title", "subtitle", "notes")

        self.initTags()

        if focus is self.textBox:
            for line in self.tagIndexList:
                startIndex = self.textBox.index(line[0])
                endIndex = self.textBox.index(line[1])

                if line[2] == 0:
                    self.textBox.tag_add("title", startIndex, endIndex)
                elif line[2] == 1:
                    self.textBox.tag_add("subtitle", startIndex, endIndex)
                elif line[2] > 1:
                    self.textBox.tag_add("notes", startIndex, endIndex)

        elif focus is self.rewriteBox:
            for line in self.rewriteTagIndexList:
                startIndex = self.rewriteBox.index(line[0])
                endIndex = self.rewriteBox.index(line[1])

                if line[2] == 0:
                    self.rewriteBox.tag_add("title", startIndex, endIndex)
                elif line[2] == 1:
                    self.rewriteBox.tag_add("subtitle", startIndex, endIndex)
                elif line[2] > 1:
                    self.rewriteBox.tag_add("notes", startIndex, endIndex)
    
    def checkChanges(self):
        """Check to see whether changes have occurred"""
        timeNow = self.master.master.getTime()
        if self.changed and timeNow - 2 > self.updateTime and not self.tagsUpToDate:
            self.updateTags()
        self.textBox.after(1, self.checkChanges)
    
    def getLink(self):
        """Add a link from the selection to another note"""
        focus = self.master.master.getFocus()
        self.master.master.openLinkBox(focus)

    def updateLinks(self, textLinks, rewriteLinks):
        """textLinks = self.textLinks
        rewriteLinks = self.rewriteLinks"""
        self.textLinks = deepcopy(textLinks)
        self.rewriteLinks = deepcopy(rewriteLinks)

        for link in textLinks:
            (linkLocation, linkLine) = self.textHypMan.links[link]
            self.insertLink("textBox", linkLocation, linkLine, False)
        for relink in rewriteLinks:
            #self.insertLink("rewriteBox", relink[0], relink[1])
            pass

    def insertLink(self, box, linkLocation, line=None, add=True):
        """Insert a link into box"""
        linkList = linkLocation.split("/")
        defaultLinkName = "".join(linkList[-1].split(".")[:-1])

        selection = self.master.master.selection

        if box == "textBox":
            self.textLinks[selection] = (linkLocation, line)
            if type(selection) is str:
                self.textBox.insert(
                    INSERT,
                    defaultLinkName,
                    self.getLinkTag(box, linkLocation, line, add))
                    
            elif type(selection) is tuple:
                startIndex = selection[0]
                endIndex = selection[1]
                hyper, tag = self.getLinkTag(box, linkLocation, line, add)
                self.textBox.tag_add(hyper, startIndex, endIndex)
                self.textBox.tag_add(tag, startIndex, endIndex)

        elif box == "rewriteBox":
            self.rewriteLinks[selection] = (linkLocation, line)
            if type(selection) is str:
                self.rewriteBox.insert(
                    INSERT,
                    defaultLinkName,
                    self.getLinkTag(box, linkLocation, line, add))
                    
            elif type(selection) is tuple:
                startIndex = selection[0]
                endIndex = selection[1]
                hyper, tag = self.getLinkTag(box, linkLocation, line, add)
                self.rewriteBox.tag_add(hyper, startIndex, endIndex)
                self.rewriteBox.tag_add(tag, startIndex, endIndex)
        
        self.master.master.selection = False

    def getLinkTag(self, box, linkLocation, line, add):
        if add:
            if box == "textBox":
                return self.textHypMan.add(linkLocation, line)
            elif box == "rewriteBox":
                return self.rewriteHypMan.add(linkLocation, line)

    def openLink(self):
        selected = self.master.master.getFocus()
        if selected is self.textBox:
            linkLoc = self.lastLink[0]
            linkLine = self.lastLink[1]
            self.master.master.openFile(linkLoc, linkLine)

    def getSelection(self):
        """Get the current selection range"""
        box = self.master.master.getFocus()
        try:
            start = box.index(SEL_FIRST)
            end = box.index(SEL_LAST)
            return (start, end)
        except TclError:
            insertpos = box.index(INSERT)
            return insertpos

    def startHypManagers(self):
        class HyperlinkManager:
            def __init__(self, text, master, app):
                self.text = text
                self.master = master

                self.text.tag_config(
                    "hyper",
                    foreground=app.hyperlinkColour,
                    underline=1)
                
                self.text.tag_bind("hyper", "<Enter>", self._enter)
                self.text.tag_bind("hyper", "<Leave>", self._leave)
                self.text.tag_bind("hyper", "<Button-1>", self._click)

                self.reset()

            def reset(self):
                self.links = {}

            def add(self, location, line):
                """Add an action to the manager"""
                tag = "hyper-%d" % len(self.links)
                self.links[tag] = (location, line)
                return "hyper", tag
            
            def _enter(self, event):
                self.text.config(cursor="hand2")

            def _leave(self, event):
                self.text.config(cursor="")

            def _click(self, event):
                for tag in self.text.tag_names(CURRENT):
                    if tag[:6] == "hyper-":
                        location = self.links[tag][0]
                        line = self.links[tag][1]
                        self.master.lastLink = (location, line)
                        self.master.openLink()
                        return
            
            def replace(self, newLinks):
                self.links = newLinks

        self.textHypMan = HyperlinkManager(self.textBox, self, self.master.master)
        self.textLinks = {}
        self.rewriteHypMan = HyperlinkManager(self.rewriteBox, self, self.master.master)
        self.rewriteLinks = {}

class arrangementFrame(Frame):

    def __init__(self, master):
        """Initialise arrangement frame"""
        self.master = master

        self.testMessage = "arrangementFrame is initialised"

        self.titleBar = self.master.titleBar

        self.Frame = Frame()
        self.Frame.pack(side=LEFT)
