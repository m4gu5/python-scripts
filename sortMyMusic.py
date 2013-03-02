#!/usr/bin/python

# Creates directories for every interpret with more than one title in the specified directory
# File names must have the format "<Interpret> - <Title>"
# Example usage: python sortMyMusic /home/$USER/Music
# Author: @m4gu5
# License: GPL

import sys
import os

try:
    directory = sys.argv[1]
except:
    print("Usage: python " + sys.argv[0] + " <directory>")
    print("Important: File names must be in format <Interpret> - <Title>")
    exit(1)

fileList = []

if not directory.endswith('/'):
    directory += '/'

for f in os.listdir(directory):
    fileList.append(f)

# Sort entries
fileList.sort()


interpretBuffer = ''
fileBuffer = ''

# Iterate over all files
for f in fileList:
    interpret = f.split(' -')[0]
    if interpret == interpretBuffer:
        if not os.path.isdir(directory + interpret):
            # When directory doesn't exist
            # Create a new directory
            print("\nCreating directory for " + interpret + "...")
            os.mkdir(directory + interpret)
        if os.path.exists(directory + fileBuffer):
            # If first file from interpret wasn't yet moved, do it now
            os.rename(directory + fileBuffer, directory + interpretBuffer + '/' + fileBuffer)
        # Move file
        print("Moving " + f + " into directory " + directory + interpret + "...")
        os.rename(directory + f, directory + interpret + '/' + f)
    else:
        interpretBuffer = interpret
        fileBuffer = f
