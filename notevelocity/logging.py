"""

NoteVelocity - A speedy note-taking program
Copyright (C) 2013  George Bryant

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Imports
from os import getcwd
from datetime import datetime

# Main
class Log():
	def __init__(self, master):
		self.master = master

		self.open()

	def open(self):
		self.location = getcwd() + "/.log"

		self.logFile = open(self.location, "w+")

		time = self.getTime()
		self.logFile.write("NoteVelocity Log File\n" + time + " - Log initialised")

	def getTime(self):
		timeStamp = str(datetime.now())
		return timeStamp

	def write(self, line):
		time = self.getTime()
		self.logFile.write("\n" + time + " - " + line)

	def writeError(self, line):
		time = self.getTime()
		self.logFile.write("\n#ERROR:\n\t" + time + " - " + line)

	def close(self):
		self.logFile.close()