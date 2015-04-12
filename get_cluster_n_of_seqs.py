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

newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
        for i, line in enumerate(file):
            if line[0] == ">":
                cluster = re.findall('centroid=[A-Z0-9]+-[0-9]+', line)[0]
                seq_n = re.findall('seqs=[0-9]+;;seqs=[0-9]+', line)[0]
                #seq_n = re.findall(';seqs=[0-9]+', line)[0]
                cluster = re.findall('[A-Z0-9]+-[0-9]+', cluster)[0] # double-seqs
                #seq_n = re.findall('[0-9]+', seq_n)[0]
                seq_n_1, seq_n_2 = re.findall('[0-9]+', seq_n) # for double-"seqs"
                # newline = str(cluster + ',' + seq_n + '\n') 
                newline = str(cluster + ',' + seq_n_1 + ',' + seq_n_2 + '\n') # dbl-seqs
                newfile.write(newline)
                #print seq_n_1, seq_n_2
            else: 
                continue
	file.close()
        newfile.close()


