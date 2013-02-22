#!/usr/bin/python

# RePlaceFromFile

# Replaces all occurences of a given string with a substitute in the specified file
# Author: @m4gu5
# Released under the terms of the GNU General Public License (GPL)

import sys

usageString = "Usage: " + sys.argv[0] + " <file> <old string> <new string>"

# Read the arguments

try:
    alteringFile = sys.argv[1]
    toReplace = sys.argv[2]
    newString = sys.argv[3]
except:
    print(usageString)
    sys.exit(1)



# List holding all lines
lines = []

# Store all lines in list lines
with open(alteringFile, "r") as f:
    lines = f.readlines()
    f.close()

# Replace all occurences of the given string
for line in lines:
    lines[lines.index(line)] = line.replace(toReplace, newString)

# Safe new stuff to the file
with open(alteringFile, "w") as f:
    f.writelines(lines) 
    f.close()
