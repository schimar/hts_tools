#! /usr/bin/python
# 
# This script reads a fastq file and outputs the number of reads for each
# individual
# Usage: ./get_n_of_reads_per_ind.py <input-file_name.fastq> > n_reads_per_ind.txt


import sys
#import re
#import shutil
#import tempfile

#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    n_seqs = dict()
    for i, line in enumerate(file):
        if line[0] == '@':
            line_list = line.split(' ')
            ind = line_list[0].split('@')[1]
            if not ind in n_seqs:
                n_seqs[ind] = 1
            else:
                n_seqs[ind] += 1
        else:
            continue 
            
            
    file.close()

for key, value in n_seqs.iteritems():
    print key, value
