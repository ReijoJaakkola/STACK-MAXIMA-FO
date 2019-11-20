import sys

# Python script for removing comments and linebreaks from
# Maxima code.

try:
	with open(sys.argv[1]) as inputFile:
		lines = inputFile.readlines()
	strippedLines = []
	comment = False
	for line in lines:
		if '/*' in line:
			comment = True
		if not comment:
			strippedLines.append(line.replace('\n',''))
		if '*/' in line:
			comment = False
	output = str()
	for line in strippedLines:
		output += line
	with open(sys.argv[1],'w') as outputFile:
		outputFile.write(output)
except Exception as e:
	print(Exception.__str__(e))