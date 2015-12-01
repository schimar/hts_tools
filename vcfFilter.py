#! /usr/bin/python
# 
# This script reads a fasta file (the vsearch output with centroids) and writes a new file where all the sequences with less than 70 reads have been discarded. 

# Usage: ./exclude_short_seqs.py <input-file_name.fasta> <new_file_name.fasta>


import sys
import re
import shutil
#import tempfile

### stringency variables, edit as desired
minCoverage = 128 # minimum number of seqs; DP
minAltRds = 4 # minimum number of sequences with the alternative allele; AC
notFixed = 1.0 # removes loci fixed for alt; AF
mapQual = 30 # minimum mapping quality


#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    for line in enumerate(file):
        if line[0] == '#':
            continue
            #print line
        else:
            dp = re.findall('DP=[0-9]+', line)[0]#.split('=')[1]
            #ac = re.findall('AC=[0-9]+', line)[0].split('=')[1]
            #af = re.findall('AF=[0-9]+', line)[0].split('=')[1]
            #mq = re.findall('MQ=[0-9]+', line)[0].split('=')[1]
            print dp#, ac, af, mq
    file.close()
    #newfile.close()


