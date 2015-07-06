#! /usr/bin/python
# 
### YET TO BE CHANGED: This script reads a fasta file (the vsearch output with centroids) and extracts the sample name-cluster number as well as the number of seqs found in this cluster.
# Note that this script can be used for the consensus or paralogs files
# (paralogs only has one "seqs=" in there, whereas the paralogs file with --id = 0.8 will have "seqs" twice). Simply uncomment the respective lines.

# Usage: ./parse_anno_baySeq.py /home/schimar/Desktop/boechera/rna_seq/parse_anno_baySeq/anno_info_sub1000.txt /home/schimar/Desktop/boechera/rna_seq/manuscript/data/apo_setPriors.csv /home/schimar/Desktop/boechera/rna_seq/stress_response_genes_Su2013.csv

import sys
import re
#import shutil
#import tempfile

#newfile = open(sys.argv[2], 'a')
annotation = dict()
with open(sys.argv[1], 'rb') as file:
	for i, line in enumerate(file):
		line_list = line.split('\t')
		gene = str(line_list[1] + '.v1.2')
		go_terms = line_list[9]
		tair10_hit = line_list[10][:-2]
		tair10_symbol = line_list[11]
		tair10_defline = line_list[12]
		annotation[tair10_hit] = gene, go_terms, tair10_symbol, tair10_defline
		#print tair10_hit, annotation.get(tair10_hit)[0]
		
	file.close()




# read the baySeq files (only one so far)
with open(sys.argv[2], 'rb') as bS_file:
	for i, line in enumerate(bS_file):
		line_list = line.split(',')
		print line_list[1]
	bS_file.close()



# read the list of target genes
with open(sys.argv[3], 'rb') as parse_file:
	for i, line in enumerate(parse_file):
		if i == 0:
			continue
		else:
			line_list = line.split(',')
			at_gene = line_list[1][:-1]
			#if at_gene in annotation:
				#print at_gene, annotation[at_gene][0]
			#else:
				#print 'gene not found in subset'

	parse_file.close()







