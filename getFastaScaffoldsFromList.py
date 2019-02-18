#! /usr/bin/python

# this script prints only the scaffolds from a supplied file (with scaffolds to keep) from a larger fasta file.
# Usage: ./getFastaScaffoldsFromList.py input_file.fa scaffold_list.txt > new_file.fa


from sys import argv
from Bio import SeqIO
#import re
import shutil
import tempfile

with open(argv[2], 'rb') as scaffoldsFile:
    scafls = list()
    for line in scaffoldsFile:
        scafls.append(line.split('\n')[0])

scaffoldsFile.close()


#with open(argv[1], 'rb') as file:
	#newfile = tempfile.NamedTemporaryFile(delete=False)
for scaf in SeqIO.parse(open(argv[1], 'r'), 'fasta'):
    if scaf.id in scafls:
        print str('>' + scaf.id)
        print scaf.seq


