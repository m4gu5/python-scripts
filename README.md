python-scripts
==============

A few python scripts I wrote.

Most scripts use Python 3, so if you encounter any problems while running one of the scripts please check your python version first.

All scripts are licensend under the terms of GPL.

boincUpdate.py
--------------
Periodically issues an Update command for a BOINC project on a given host.
This can be used to grab Workunits even if there are only very few available.

Example usage:

`$ python boincUpdate.py --host 192.168.2.5 --passwd 'notsosecurepassword' --project http://www.worldcommunitygrid.org`

addInterpret.py
---------------
Appends the name of an interpret to existing music files within a directory.

Example: Blut im Auge.mp3 >> Equilibrium - Blut im Auge.mp3

Example usage:

`$ python addInterpret.py /home/$USER/Musik/Equilibrium 'Equilibrium'`

flvConverter.py
---------------
Script for converting all flv files within a directory recursively to mp3 files.

Default save path is  $directory/mp3/$filename.mp3

Depends on ffmpeg.

Example usage:

`$ python flvConverter.py /home/$USER/Videos/`

rpff.py
-------
Replaces all occurences of a given string with a substitute in the specified file.

Example usage:

`$ python rpff.py testfile.txt "Hate" "Love"`

sortMyMusic.py
--------------
Creates subdirectories for every interpret with more than one title in the specified directory.

File names must have the format "$interpret - $title".

Example usage:

`$ python sortMyMusic.py /home/$USER/Music`
