#!/usr/bin/python

# Script for converting all flv files within a directory recursively to mp3 files
# Default save path is <directory>/mp3/<filename>.mp3
# Can be automated via crond
# Author: @m4gu5
# License: GPL

import os
import subprocess
import argparse

def convertFiles(convertDir):
    for f in os.listdir(convertDir):
        if os.path.isdir(convertDir + f):
            convertFiles(convertDir + f + '/')
        elif not os.path.isdir(convertDir + f):
            if f.endswith('.flv'):

                # Check if there is already a mp3 file for the video
                if os.path.exists(convertDir + saveDir + '/' + f.split('.flv')[0] + '.mp3'):
                    continue

                # Check if mp3 directory already exists, if not create it
                if not os.path.exists(convertDir + saveDir):
                    os.mkdir(convertDir + saveDir) 

                fileName = convertDir + saveDir + '/' + f.split('.flv')[0]
                subprocess.call(['ffmpeg', '-i', convertDir + f, '-ar', '44100', '-b:a', '160k', '-ac', '2', fileName + '.mp3'])
                print("Created mp3 " + fileName + ".mp3")


parser = argparse.ArgumentParser(description='Convert all flv files within a directory to mp3')
parser.add_argument('-d', '--directory', help='Directory where the flv files are present', dest='directory', type=str, required = True)
parser.add_argument('-s', '--saveDir', help='Directory under which the mp3s should be saved (Default: mp3/)', dest='saveDir', type=str, default = 'mp3')
args = parser.parse_args()

directory = args.directory
saveDir = args.saveDir

# Add slash
if not directory.endswith('/'):
    directory += '/'

# Remove slash
if saveDir.endswith('/'):
    saveDir = saveDir[0:len(saveDir) - 1]

convertFiles(directory)

