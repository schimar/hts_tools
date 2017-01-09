#! /usr/bin/python
#
# This script reads a fasta file (the vsearch output with centroids) and extracts the sample name-cluster number as well as the number of seqs found in this cluster.
# Note that this script can be used for the consensus or paralogs files, simply
# specify the seqtype (2nd argv), with either cons or para  (consensus or paralogs))

# Usage: ./get_cluster_n_of_seqs.py seqtype <input-file_name.fasta> <new_file_name.csv>


from sys import argv
import re
#import shutil
#import tempfile
seqtype = argv[1]

newfile = open(argv[3], 'a')
with open(argv[2], 'rb') as file:
        for i, line in enumerate(file):
            if line[0] == ">":
                cluster = re.findall('centroid=[A-Z0-9_a-z]+-[0-9]+', line)[0]
                if seqtype == "cons":
                    seq_n = re.findall(';seqs=[0-9]+', line)[0]
                    newline = str(cluster + ',' + seq_n + '\n')
                elif seqtype == "para":
                    cluster = re.findall('[A-Z0-9_a-z]+-[0-9]+', cluster)[0]
                    seq_n = re.findall('seqs=[0-9]+;;seqs=[0-9]+', line)[0]
                    seq_n_1, seq_n_2 = re.findall('[0-9]+', seq_n)
                    newline = str(cluster + ',' + seq_n_1 + ',' + seq_n_2 + '\n')
                newfile.write(newline)
                #print seq_n_1, seq_n_2
            else:
                continue
	file.close()
        newfile.close()


