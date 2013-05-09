"""Building the functionality for note program.
	Start with the basics."""


## Imports
import os
import getThe


## Main Function
def main(inputFilename, outputFilename, tempFilename):
	# Opens temporary and output files.
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
	superscriptMarker = ["<sup>","</sup>"]
	subscriptMarker = ["<sub>","</sub> "]
	tabMarker = "&nbsp;&nbsp;&nbsp;&nbsp;"
	bulletMarker = chr(149)

	# Formatting state variables
	italic = 0
	bold = 0
	underlined = 0
	strikethrough = 0
	equation = 0
	superscript = 0
	subscript = 0
	tabbed = 0
	 # Currently redundant, but may be useful in future for making indented bullet points.

	# Iterate through file, line by line
	for line in tempfile:

		# Turn line string into list
		lineBuffer = list(line)

		# Create list with same length as line buffer
		lineBufferLength = range(len(lineBuffer))

		## FORMATTING:

		# Iterate through each line
		for n in lineBufferLength:

			## Tabs
			if lineBuffer[n] == "\t":
				lineBuffer[n] = tabMarker

			## Bullet points

			# Check for bulletPointPlacement
			if lineBuffer[n] == "*" and n == 0 and lineBuffer[n+1] == " ":
				lineBuffer[n] = bulletMarker

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
			if lineBuffer[n] == "_" and lineBuffer[n-1] != "\\" and underlined == 0 and equation != 1:

				# Make current character into a underline start marker, and set underlined to 1
				lineBuffer[n] = underlineMarker[0]
				underlined = 1

			# Check for underlineEnd, and ignore escaped "_"s
			elif lineBuffer[n] == "_" and lineBuffer[n-1] != "\\" and underlined == 1 and equation != 1:

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

			## SUPERSCRIPT (only in equations)

			# Check for superscriptStart, and ignore escaped "^"s, only when equation == 1 and there is an opening bracket.
			if lineBuffer[n] == "^"and lineBuffer[n-1] != "\\" and equation == 1 and superscript == 0 and lineBuffer[n+1] == "(":

				# Make current character into a superscript start marker, remove opening bracket and set superscript to 1
				lineBuffer[n] = superscriptMarker[0]
				lineBuffer[n+1] = None
				superscript = 1

			# Check for superscriptEnd, and ignore escaped "^"s, only when equation == 1 and there is a closing bracket.
			if lineBuffer[n] == ")"and lineBuffer[n-1] != "\\" and equation == 1 and superscript == 1:

				# Make current character into a superscript end marker and set superscript to 0
				lineBuffer[n] = superscriptMarker[1]
				superscript = 0

			## SUBSCRIPT (only in equations)

			# Check for subscriptStart, and ignore escaped "_"s, only when equation == 1 and there is an opening bracket.
			if lineBuffer[n] == "_"and lineBuffer[n-1] != "\\" and equation == 1 and subscript == 0 and lineBuffer[n+1] == "(":

				# Make current character into a subscript start marker, remove opening bracket and set subscript to 1
				lineBuffer[n] = subscriptMarker[0]
				lineBuffer[n+1] = None
				subscript = 1

			# Check for subscriptEnd, and ignore escaped ")"s, only when equation == 1 and there is a closing bracket.
			if lineBuffer[n] == ")"and lineBuffer[n-1] != "\\" and equation == 1 and subscript == 1:

				# Make current character into a subscript end marker and set superscript to 0
				lineBuffer[n] = subscriptMarker[1]
				subscript = 0

			# Make charBuffer
			charBuffer = lineBuffer[n]

			# Write output file, ignoring non-escaped backslashes
			# Check for \\, and write \
			if lineBuffer[n] == "\\" and lineBuffer[n+1] == "\\":
				outputfile.write(lineBuffer[n])
			# Check for \, and ignore
			elif lineBuffer[n] == "\\" and lineBuffer[n+1] != "\\":
				pass
			# Ignore nulls
			elif lineBuffer[n] is None:
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


## Get filenames, then run main function
# Get input filename
inFilename = getThe.inputFile()
# Get output filename
outFilename = getThe.outputFile()
#Get temporary filename, and initialise temporary file
tempFilename = getThe.tempFile(inFilename)
# Run main function
main(inFilename, outFilename, tempFilename)