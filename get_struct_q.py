#!/usr/bin/python

# This script reads through a genotype likelihood (gl) file and prints the number of variants for each scaffold

# Usage: ~/get_num_snvs_per_scaf.py pubRetStriUG_unlnkd.gl

from sys import argv


with open(argv[1], 'rb') as file:
    for line in file:
        line_list = line.split('\n')[0].split(' ')
        if len(line_list) == 1:
            continue
        else:
            #print line_list
            lline = ' '.join(line_list).split(': ')[-1]#.split(' ')
            print lline

    file.close()
