#! /usr/bin/python


# This script reads through a file containing the scaffold number and snp_id
# (space-separated) and a second file, containing the allele frequencies in the
# specified format for bayenv2 (see
# http://www.eve.ucdavis.edu/gmcoop/Software/Bayenv/Bayenv.html for more info).
# The output contains allele frequencies for the first SNP of each scaffold. 

# (see also sites.google.com/site/evolutionarygenomicsfall15/assignment-7)
# Usage: ./ngs_tools/get_unlnkd_snp_list.py <scaffold-snp-file> <file> > outfile


import sys
import re

with open(sys.argv[1], 'rb') as scaf_file:
    #scaf = dict()
    n = int()
    snp_id_list = list()
    prior_scaf = str()
    for i, line in enumerate(scaf_file):
        scaffold, snp = line.split(' ')
        if scaffold != prior_scaf:
            n += 1
            snp_line_a1 = i*2
            snp_id_list.append(snp_line_a1)
            snp_id_list.append(snp_line_a1 + 1)
        else: 
            continue 
        prior_scaf = scaffold

# snp_id_double = [x * 2 for x in snp_id_list]
#print snp_id_list
#print snp_id_double


with open(sys.argv[2], 'rb') as allele_file:
    for i, line in enumerate(allele_file):
        if i in snp_id_list:
            print line.split('\n')[0]

    allele_file.close()
    scaf_file.close()
        
