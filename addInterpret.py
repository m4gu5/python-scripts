#!/usr/bin/python

# Appends the name of an interpret to existing music files within a directory
# Example: Blut im Auge.mp3 >> Equilibrium - Blut im Auge.mp3
# Example usage: python addInterpret.py /home/$USER/Musik/Equilibrium 'Equilibrium'
# Author: @m4gu5
# License: GPL

import os
import sys

try:
    directory = sys.argv[1]
    interpret = sys.argv[2]
except:
    print("Usage: python " + sys.argv[0] + " <directory> <interpret>")
    exit(1)

if not directory.endswith('/'):
            # The slash is needed in order to rename the files
            directory += '/'

for f in os.listdir(directory):
    if not f.startswith(interpret):
        # If interpret is not already included
        os.rename(directory + f, directory + interpret + ' - ' + f)


