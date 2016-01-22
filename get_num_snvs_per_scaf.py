#!/usr/bin/python

# This script reads through a genotype likelihood (gl) file and prints the number of variants for each scaffold

# Usage: ~/get_num_snvs_per_scaf.py pubRetStriUG_unlnkd.gl

from sys import argv


# read gl file for scaffold:bp pos
with open(argv[1], 'rb') as gl_file:
    scafNum = dict()
    old_scaf = str()
    for line in gl_file:
        if line.split(' ')[0] == '79' or line.split(' ')[0] == 'CR1043': # watch out, hard-coded!
            continue
        else:
            scaf_bp = line.split(' ')[0]
            scaffold, pos = scaf_bp.split(':')
            if scaffold == old_scaf:
                scafNum[scaffold] += 1
            else:
                scafNum[scaffold] = 1
                old_scaf = scaffold

for key, value in iter(scafNum.iteritems()):
    print key, value


