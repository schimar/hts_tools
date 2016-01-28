#! /usr/bin/python
#
# This script reads

# Usage: ./

import sys
import re
#import shutil
#import tempfile

#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
        for i, line in enumerate(file):
            freq = line.split('\n')[0]
            line_list = freq.split(' ')
            print line_list[2]  #, line_list[2] #freq.split('\n')[0]
	file.close()


