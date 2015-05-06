#! /usr/bin/python

# this script takes the output from DESeq2 and creates a list 
# containing the gene and a binary vector for significant differential 
# expression (at a given p-value cutoff, e.g. 0.01)
#
# Usage: ./get_DESeq2_signif.py <p-value_threshold> <input_file_name> <output_file.txt>


import sys
import re

###
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
###


newfile = open(sys.argv[3], 'a')
with open(sys.argv[2], 'rb') as file:
    for line in file:
        if line[1] == '"':
            continue
        else:
            line_list = line.split(',')
            gene = line_list[0]
            p = line_list[6]
            if is_number(p):
                if float(p) < float(sys.argv[1]):
                    newfile.write(str(gene + '\t' + '1' + '\t' + p + '\n'))
                else:
                    newfile.write(str(gene + '\t' + '0' + '\t' + p + '\n'))
            else:
               newfile.write(str(gene + '\t' + 'NA' + '\t' + p + '\n'))
            
    file.close()
    newfile.close()
