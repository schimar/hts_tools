#! /usr/bin/python
# 
### YET TO BE CHANGED: This script reads a fasta file (the vsearch output with centroids) and extracts the sample name-cluster number as well as the number of seqs found in this cluster.
# Note that this script can be used for the consensus or paralogs files
# (paralogs only has one "seqs=" in there, whereas the paralogs file with --id = 0.8 will have "seqs" twice). Simply uncomment the respective lines.

# Usage: ./parse_anno_baySeq.py /home/schimar/Desktop/boechera/rna_seq/manuscript/data/df_baySeq_all_GO.txt /home/schimar/Desktop/boechera/rna_seq/stress_response_genes_Su2013.csv

import sys
import re
#import shutil
#import tempfile

# this is no longer needed, as the baySeq_df has the annotations already.
#newfile = open(sys.argv[2], 'a')
#annotation = dict()
#with open(sys.argv[1], 'rb') as file:
#    for i, line in enumerate(file):
#        line_list = line.split('\t')
#	gene = str(line_list[1] + '.v1.2')
#	go_terms = line_list[9]
#	tair10_hit = line_list[10][:-2]
#	tair10_symbol = line_list[11]
#	tair10_defline = line_list[12]
#	annotation[tair10_hit] = gene, go_terms, tair10_symbol, tair10_defline
	#print tair10_hit, annotation.get(tair10_hit)[0]
#	print line_list

#    file.close()



bayS_dict = dict()
no_anno = 0
# read the baySeq file 
with open(sys.argv[1], 'rb') as bS_file:
    for i, line in enumerate(bS_file):
        line_list = line.split('\t')
        tair10hit = line.split('\t')[63][1:-3]
        tair10hit_descr = line.split('\t')[64]
        if tair10hit == '':
            no_anno += 1
        else: 
            bayS_dict[tair10hit] = line_list#, 30:31, 34:35, 38:39, 42:43, 46:47, 50, 54:55, 57:59, 62:] 
            bayS_dict[tair10hit].pop()
            bayS_dict[tair10hit].pop(0)
            #print bayS_dict[tair10hit]
     #print 'We found %i genes with no A. thaliana annotation' % no_anno # 837 genes without AT annotations
    bS_file.close()


# read the list of target genes
with open(sys.argv[2], 'rb') as parse_file:
    for i, line in enumerate(parse_file):
        line_list = line.split(',')
        if line_list[0][0] == '#':
            print line 
        else:
            at_gene = line_list[0]#[:-1]
            name = line_list[1]
            if at_gene in bayS_dict:
                #bayS_dict.get(at_gene).append(name)
                #print bayS_dict.get(at_gene)
                print '\t '.join(map(str, bayS_dict.get(at_gene)))
            else:
                line_if_not_found = str(at_gene + name + 'not found in dataset')
                print line_if_not_found
    parse_file.close()



