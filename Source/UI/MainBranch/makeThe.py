"""Functions to construct stuff to make it less repetitive"""

# Import
from Tkinter import *

def tkFrame(master, packSide):
	frame = Frame(master)

	# packSide:
	#	0 = not included
	#	1 = LEFT
	#	2 = RIGHT

	if packSide == 0:
		frame.pack(fill = BOTH)

	elif packSide == 1:
		frame.pack(side = LEFT, fill = BOTH)

	elif packSide == 2:
		frame.pack(side = RIGHT, fill = BOTH)

	return frame