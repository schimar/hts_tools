#! /usr/bin/python
# 
# This script reads a fasta file (the vsearch output with centroids) and extracts the sample name-cluster number as well as the number of seqs found in this cluster.
# Note that this script can be used for the consensus or paralogs files
# (paralogs only has one "seqs=" in there, whereas the paralogs file with --id = 0.8 will have "seqs" twice). Simply uncomment the respective lines.

# Usage: ./get_cluster_n_of_seqs.py <input-file_name.fasta> <new_file_name.csv>


import sys
import re
#import shutil
#import tempfile

#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
        for i, line in enumerate(file):
            freq = line.split(' ')[1]
            print freq.split('\n')[0]
	file.close()


