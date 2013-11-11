"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Imports
from tkinter import *
from tkinter.ttk import *
import bindings

class tabBar(Frame):
	def __init__(self, master):
		self.master = master

		self.testMessage = "tabBar is initialised"

		self.Frame = Frame(height = 24, style = "TabBar.TFrame")
		self.Frame.pack(fill = X, expand = 0, side = BOTTOM)

		self.tabs = list()

		self.lastSelectedTab = 0
		self.selectedTab = 0

		self.add(self, "New Note")

	def add(self, master, title):
		newTabNum = len(self.tabs)
		self.tabs.append(self.tab(self, title))

		self.switch(1, len(self.tabs)-1)

	def switch(self, mode, amount):
		if mode == 0: #Add amount
			if self.selectedTab + amount < len(self.tabs) and self.selectedTab + amount >= 0:
				self.lastSelectedTab = self.selectedTab
				self.selectedTab += amount

			elif self.selectedTab + amount >= len(self.tabs) - 1:
				self.lastSelectedTab = self.selectedTab
				self.selectedTab = 0

			elif self.selectedTab + amount < 0:
				self.lastSelectedTab = self.selectedTab
				self.selectedTab = len(self.tabs) - 1

		elif mode == 1: # Switch to amount
			if amount < len(self.tabs) and amount >= 0:
				self.lastSelectedTab = self.selectedTab
				self.selectedTab = amount
			elif amount < 0:
				self.lastSelectedTab = self.selectedTab
				self.selectedTab = 0

			elif amount >= len(self.tabs):
				self.lastSelectedTab = self.selectedTab
				self.selectedTab = len(self.tabs) - 1

		self.tabs[self.lastSelectedTab].deselect()
		self.tabs[self.selectedTab].select()

	def closeCurrent(self):
		if len(self.tabs) > 1:
			self.lastSelectedTab = self.selectedTab
			self.selectedTab -= 1

			self.tabs[self.lastSelectedTab].close()
			del self.tabs[self.lastSelectedTab]
			self.tabs[self.selectedTab].select()

		else:
			self.lastSelectedTab = 0
			self.selectedTab = 0

			self.tabs[self.lastSelectedTab].close()
			del self.tabs[0]
			self.add(self, "New Note")

	def closeSpecific(self, tabNum):
		if tabNum < self.selectedTab:
			self.tabs[tabNum].close()
			del self.tabs[tabNum]
			self.selectedTab -= 1
			
		elif tabNum > self.selectedTab:
			self.tabs[tabNum].close()
			del self.tabs[tabNum]

		else: # if the selected tab is the one being closed
			if tabNum == 0: # if it's the first tab
				if len(self.tabs) == 1: # if it's the only tab
					self.tabs[tabNum].close()
					del self.tabs[tabNum]
					self.add(self, "New Note")

				else: # if it's not the only tab
					self.tabs[tabNum].close()
					del self.tabs[tabNum]
					self.selectedTab = 0
					self.switch(1, self.selectedTab)

			elif tabNum == len(self.tabs) - 1: # if it's the last tab
				self.tabs[tabNum].close()
				del self.tabs[tabNum]

				if self.selectedTab == tabNum:
					self.selectedTab -= 1

				self.switch(1, self.selectedTab)

			else: # if it's somewhere in the middle
				if self.selectedTab == tabNum:
					self.selectedTab -= 1

				self.tabs[tabNum].close()
				del self.tabs[tabNum]
				self.switch(1, self.selectedTab)

	class tab():
		def __init__(self, master, title):
			self.master = master

			self.text = StringVar()

			self.Frame = Frame(self.master.Frame, style = "Tab.TFrame")

			if len(title) > 16:
				title = title[:16] + "..."

			self.title = Label(self.Frame, style = "TT.TLabel")
			self.title.config(text = title)

			self.titleBox = Entry(self.Frame, width = 20)
			self.titleBox.insert(0, title)

			self.closeButton = Button(self.Frame, style = "Tab.TButton", text = "X", width = 1)

			self.bindings()

			self.show()

		def bindings(self):
			self.title.bind("<Button-1>", lambda event: self.master.switch(1, self.findPlace()))
			self.Frame.bind("<Button-1>", lambda event: self.master.switch(1, self.findPlace()))
			self.closeButton.bind("<Button-1>", lambda event: self.master.closeSpecific(self.findPlace()))

		def findPlace(self):
			return self.master.tabs.index(self)

		def show(self):
			self.Frame.pack(side = LEFT, expand = 0, ipadx = 2, ipady = 2, padx = 4, pady = 2)
			self.title.pack(side = LEFT, expand = 0, ipadx = 4, ipady = 2, padx = 4)
			self.closeButton.pack(side = LEFT, expand = 0, ipadx = 1, ipady = 0)

			self.select()

		def select(self):
			self.Frame.config(style = "TabSelected.TFrame")
			self.title.config(style = "TTS.TLabel")

		def deselect(self):
			self.Frame.config(style = "Tab.TFrame")
			self.title.config(style = "TT.TLabel")

		def rename(self):
			self.titleBox.pack(side = LEFT, expand = 0, ipadx = 4, ipady = 2, padx = 4)

		def close(self):
			self.Frame.pack_forget()

			# save file