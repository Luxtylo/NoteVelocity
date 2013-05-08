"""Building the functionality for note program.
	Start with the basics."""

## Imports
import os

## Main Function
def main(inputFilename, outputFilename, tempFilename):
	# Asks for and gets filename - relative to function.py
	#filename = str(raw_input("Point to file to open\n"))
	#print("")

	# Open input and output files
	tempfile = open (tempFilename, "r")
	outputfile = open ("Notes/" + outputFilename, "w+")

	# Write HTML header to output file
	pageHeader = "<html><head><title>Page</title></head><body>\n"
	outputfile.write(pageHeader)

	# Replacement markup
	italicMarker = ["<i>","</i>"]
	boldMarker = ["<b>","</b>"]
	underlineMarker = ["<ins>","</ins>"]
	strikethroughMarker = ["<del>","</del>"]
	equationMarker = ["<b><i>","</i></b>"]

	# Formatting state variables
	italic = 0
	bold = 0
	underlined = 0
	strikethrough = 0
	equation = 0

	# Iterate through file, line by line
	for line in tempfile:

		# Turn line string into list
		lineBuffer = list(line)

		# Create list with same length as line buffer
		lineBufferLength = range(len(lineBuffer))

		## FORMATTING:

		# Iterate through each line
		for n in lineBufferLength:

			## Bullet points

			# Check for bulletPointPlacement
			if lineBuffer[n] == "*" and n == 0 and lineBuffer[n+1] == " ":
				bullet = chr(149)
				lineBuffer[n] = bullet

			## ITALICS:

			# Check for italicStart, and ignore escaped stars
			if lineBuffer[n] == "*" and lineBuffer[n-1] != "\\" and italic == 0:

				# Make current character into an italic start marker, and set italic to 1
				lineBuffer[n] = italicMarker[0]
				italic = 1

			# Check for italicEnd, and ignore escaped stars
			elif lineBuffer[n] == "*" and lineBuffer[n-1] != "\\" and italic == 1:

				# Make current character into an italic end marker, and set italic to 1
				lineBuffer[n] = italicMarker[1]
				italic = 0

			## BOLD:

			# Check for boldStart, and ignore escaped "<"s
			if lineBuffer[n] == "<" and lineBuffer[n-1] != "\\" and bold == 0:

				# Make current character into a bold start marker, and set bold to 1
				lineBuffer[n] = boldMarker[0]
				bold = 1

			# Check for boldEnd, and ignore escaped ">"s
			elif lineBuffer[n] == ">" and lineBuffer[n-1] != "\\" and bold == 1:

				# Make current character into a bold end marker, and set bold to 0
				lineBuffer[n] = boldMarker[1]
				bold = 0

			## UNDERLINED:

			# Check for underlineStart, and ignore escaped "_"s
			if lineBuffer[n] == "_" and lineBuffer[n-1] != "\\" and underlined == 0:

				# Make current character into a underline start marker, and set underlined to 1
				lineBuffer[n] = underlineMarker[0]
				underlined = 1

			# Check for underlineEnd, and ignore escaped "_"s
			elif lineBuffer[n] == "_" and lineBuffer[n-1] != "\\" and underlined == 1:

				# Make current character into a underline end marker, and set underlined to 0
				lineBuffer[n] = underlineMarker[1]
				underlined = 0

			## STRIKETHROUGH:

			# Check for strikethroughStart, and ignore escaped "~"s
			if lineBuffer[n] == "~" and lineBuffer[n-1] != "\\" and strikethrough == 0:

				# Make current character into a strikethrough start marker, and set strikethrough to 1
				lineBuffer[n] = strikethroughMarker[0]
				strikethrough = 1

			# Check for strikethroughEnd, and ignore escaped "~"s
			elif lineBuffer[n] == "~" and lineBuffer[n-1] != "\\" and strikethrough == 1:

				# Make current character into a strikethrough end marker, and set strikethrough to 0
				lineBuffer[n] = strikethroughMarker[1]
				strikethrough = 0

			## EQUATION:

			# Check for equationStart, and ignore escaped "["s
			if lineBuffer[n] == "[" and lineBuffer[n-1] != "\\" and equation == 0:

				# Make current character into a equation start marker, and set equation to 1
				lineBuffer[n] = equationMarker[0]
				equation = 1

			# Check for equationEnd, and ignore escaped "]"s
			elif lineBuffer[n] == "]" and lineBuffer[n-1] != "\\" and equation == 1:

				# Make current character into a equation end marker, and set equation to 0
				lineBuffer[n] = equationMarker[1]
				equation = 0

			# Write output file, ignoring non-escaped backslashes
			# Check for \\, and write \
			if lineBuffer[n] == "\\" and lineBuffer[n+1] == "\\":
				outputfile.write(lineBuffer[n])
			# Check for \, and ignore
			elif lineBuffer[n] == "\\" and lineBuffer[n+1] != "\\":
				pass
			# Otherwise write
			else:
				outputfile.write(lineBuffer[n])
		outputfile.write("<br />")

	# Add HTML footer
	outputfile.write("\n</body></html>")
	# Close files
	tempfile.close()
	outputfile.close()
	# Delete temp file
	os.remove(tempFilename)

## Get Input filename
def getInFile():
	notesDir = str(os.getcwd()) + "/Notes"
	for dirpath, dirnames, filenames in os.walk(notesDir):
		print dirpath
		for f in filenames:
			print f
	filename = str(raw_input("\nWhich note would you like to convert?\n"))
	return filename

## Get Output filename
def getOutFile():
	filename = str(raw_input("\nWhat would you like to save the note as?\n"))
	return filename

## Make temp file, copy input file into temp file.
def makeTempFile(inFilename):
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

## Get filenames, then run main function
# Get input filename
inFilename = getInFile()
# Get output filename
outFilename = getOutFile()
#Get temporary filename
tempFilename = makeTempFile(inFilename)
# Run main function
main(inFilename, outFilename, tempFilename)