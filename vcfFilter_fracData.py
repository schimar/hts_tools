#! /usr/bin/python
#
# This script filters a vcf file based on overall sequence coverage, number of
# non-reference reads, number of alleles, and reverse orientation reads.
# See below for default values, and to change them, if necessary. Additionally,
# note that currently, the number of retained loci is being written at the end
# of the file.
# Usage: ./vcfFilter.py <variant file>.vcf > outfile.vcf

from __future__ import division
import sys

### stringency variable, edit as desired
minFracData = 0.8 # skip loci where less than 80% of samples covered


############

n_seqs_retained = int()
with open(sys.argv[1], 'rb') as file:
    for line in file:
        if line[0:2] == '##':
            print line.split('\n')[0]
            continue
        elif line[0:2] == '#C':
            print line.split('\n')[0]
        else:
            line_list = line.split('\n')[0].split('\t')
            if len(line_list[4]) > 1:
                continue
            else:
                #print line_list
                ad_list = list()
                inds = line_list[9:len(line_list)]
                count = int()
                num_data_present = int()
                for i, ind in enumerate(inds):
                    ad = ind.split(':')[1]
                    if ad == '.':
                        continue #no_data += 1
                    else:
                        num_data_present += 1
                #print num_data_present, len(inds), num_data_present/len(inds)
                if num_data_present/len(inds) >= minFracData:
                    print line.split('\n')[0]

    file.close()

