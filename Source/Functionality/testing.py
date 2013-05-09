"""Main functionality file."""


## Imports
import os
import getThe
import markup
import reptest

## Main Function
def main(inputFilename, outputFilename, tempFilename):

	# Opens temporary and output files.
	tempfile = open (tempFilename, "r")
	outputfile = open ("Notes/" + outputFilename, "w+")

	# Call markup to convert file
	reptest.markItUp(tempfile, outputfile)

	# Close files
	tempfile.close()
	outputfile.close()
	# Delete temp file
	os.remove(tempFilename)

## Get filenames, then run main function
# Get input filename
inFilename = getThe.inputFile()
# Get output filename
outFilename = getThe.outputFile()
#Get temporary filename, and initialise temporary file
tempFilename = getThe.tempFile(inFilename)
# Run main function
main(inFilename, outFilename, tempFilename)