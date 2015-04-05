#! /usr/bin/python
# 
# 

# Usage: ./clean_runInfo.py <input-file_name.txt> <new_file_name.txt>


import sys
#import re
import shutil
#import tempfile

newfile1 = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
	for line in file:
            line = str(line)
            if line.split() == []:
                continue
            else:
                str_line = str(line).split()[0]
                if str_line == "Reading" or str_line == "Indexing" or str_line == "Masking":
                    continue
                elif str_line == "Sorting" or str_line == "Counting" or str_line == "Clustering":
                    continue
                elif str_line == "Writing":
                    continue
                else: 
                    newline = str(line)
                    newfile1.write(newline)
	file.close()
        newfile1.close()


