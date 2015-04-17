#! /usr/bin/python
# 
# clean_up_fasta_header.py
# 
# Usage: ./clean_up_fasta_header.py <input-file_name.fa> <new_file_name.fa>


import sys
#import re
#import shutil
#import tempfile

newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
	for line in file:
            if line[0] == ">":
                header = str(line.split(';')[0])	
	        header = str(header.split('=')[2])
                newline = str('>' + header + '\n')
            else:
                newline = line
            newfile.write(newline)
	file.close()
	#newfile.close()


