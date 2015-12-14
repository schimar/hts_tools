#! /usr/bin/python


# This scripts converts a vcf file to a simpler format for downstream analyses.
# Zach Gompert is calling this format genotype likelihood (gl). The first line
# lists the number of individuals and loci. The next line has individual ids.
# This is followed by one line per SNP that gives the SNP id (scaffold,
# position) and the phred-scaled genotype likelihoods, three per individual.
# A separate file with the allele frequency for each locus is being written. 
# This version does not yet include a filter for maf. 
#
# Usage: ./vcf2gl.py filtered_vcf_file.vcf ref_allele_freqs.txt alt_allele_freqs.txt > outfile.gl


import sys
import re
#from collections import OrderedDict


sample_file = open(sys.argv[2], 'a')

with open(sys.argv[1], 'rb') as file:
    for line in file:
        if len(line) >= 10:
            print line
        elif line[0] == "C":
            inds = line.split(' ')
        else: 
            continue
    print inds
        
        
    





    file.close()

