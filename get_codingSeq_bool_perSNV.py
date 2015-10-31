#! /usr/bin/python


# This script reads through a genotype likelihood file for a given population,
# as obtained by Zach Gompert's script subvcf2gl.pl (which separates populations
# from a vcf file (from bcftools)) and a text file containing the coding
# sequences with their start/stop positions. If a SNV lies in a coding sequence,
# then it will print the respective scaffold:SNV_pos combination.
# (see also sites.google.com/site/evolutionarygenomicsfall15/assignment-6)

# Usage: ./ngs_tools/get_codingSeq_bool_perSNV.py <pop_gl_file> <codingSeq_file>
# > outfile

import sys
import re

with open(sys.argv[2], 'rb') as codS_file:
    scaf = dict()
    for line in codS_file:
        line_list = line.split('\t')
        cscaf = line_list[0].split(':')[1].split('_')[1]
        start = line_list[1]
        stop = line_list[2].split('\n')[0]
        if not cscaf in scaf:
            scaf[cscaf] = [str(start + ' ' + stop)]
        else:
            scaf[cscaf].append((str(start + ' ' + stop)))

with open(sys.argv[1], 'rb') as file:
    for line in file:
        line_list = line.split(' ')
        scaffold, snv_id = line_list[0].split(':')
        naive_freq = line_list[1]
        final_freq = line_list[2]
        if scaffold in scaf:
            for key in scaf[scaffold]:
                start, stop = key.split(' ')
                if snv_id > start and snv_id < stop:
                    print line_list[0]
                else:
                    continue
        else:
            continue
            
    file.close()
    codS_file.close()
        
