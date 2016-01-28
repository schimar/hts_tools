#! /usr/bin/python

# Usage: ./extract_short_long_from_fa.py <input-file_name.fa> <new_file_name.fa>


import sys
#import re
import shutil
import tempfile


with open(sys.argv[1], 'rb') as file:
	newfile = tempfile.NamedTemporaryFile(delete=False)
	for line in file:
		if line[0] == ">":
			short = str(line.split()[0])
			long = "_"
			long = long.join(line.split()[1:])
					#line = line.replace(line, new)
			line = str(short + " " + long + "\n")
			newfile.write(line)
	file.close()
	shutil.move(newfile.name, sys.argv[2])
	newfile.close()

