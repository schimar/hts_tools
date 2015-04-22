#! /usr/bin/python
# 
# This script reads a fasta file (the vsearch output with centroids) and writes a new file where all the sequences with less than 70 reads have been discarded. 

# Usage: ./exclude_short_seqs.py <input-file_name.fasta> <new_file_name.fasta>


import sys
import re
import shutil
#import tempfile

########


from Bio import SeqIO
import sys

header_list = []
seq_list = []


newfile = open(sys.argv[2], 'a')
infile = open(sys.argv[1],'r')
for record in SeqIO.parse(infile,'fasta'):
   header_list.append(record.id)
   seq_list.append(str(record.seq))

for i, seq in enumerate(seq_list):
    out_str = str(header_list[i] + '\t' + str(len(seq)) + '\n')
    newfile.write(out_str)



infile.close()
newfile.close()











