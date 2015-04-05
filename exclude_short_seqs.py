#! /usr/bin/python
# 
# This script reads a fasta file (the vsearch output with centroids) and writes a new file where all the sequences with less than 70 reads have been discarded. 

# Usage: ./exclude_short_seqs.py <input-file_name.fasta> <new_file_name.fasta>


import sys
#import re
import shutil
#import tempfile

newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
	for i, line in enumerate(file):
            if line[0] == ">":
                ind_clust_line = line
                full_line = str()
                all_lines = str()
                short_line = str()
            else:
                if len(line) == 81:
                    full_line = line
                else:
                    if full_line:
                        short_line = line
                        all_lines = str(ind_clust_line + full_line + short_line)
                    elif len(line) > 70: 
                        short_line = line
                        all_lines = str(ind_clust_line + short_line)
                    else:
                        continue
            newfile.write(all_lines)
                
                    #newfile.write(header_line)
                    #newfile.write(line)
	file.close()
        newfile.close()


