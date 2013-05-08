"""The file for getting filenames and initialising files"""

import os

## Get Input filename
def inputFile():
	notesDir = str(os.getcwd()) + "/Notes"
	for dirpath, dirnames, filenames in os.walk(notesDir):
		print dirpath
		for f in filenames:
			if f.endswith(".note"):
				print f
	fileName = str(raw_input("\nWhich note would you like to convert?\n"))
	fileNameList = list(fileName)
	if fileNameList[-5] != "." and fileNameList[-4] != "." and fileNameList[-3] != ".":
		fileName = fileName + ".note"
	return fileName

## Get Output filename
def outputFile():
	fileName = str(raw_input("\nWhat would you like to save the note as?\n"))
	fileNameList = list(fileName)
	if fileNameList[-5] != "." and fileNameList[-4] != "." and fileNameList[-3] != ".":
		fileName = fileName + ".html"
	return fileName

## Make temp file, copy input file into temp file.
def tempFile(inFilename):
	# Open input file, and create/open temp file
	inputfile = open ("Notes/" + inFilename, "r")
	filename = inFilename + ".temp"
	tempfile = open (filename, "w+")

	# Iterate through inputfile, writing lines to tempfile.
	for line in inputfile:
		tempfile.write(line)

	# Close files
	inputfile.close()
	tempfile.close()
	return filename