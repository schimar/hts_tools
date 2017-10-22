#! /usr/bin/python
#
# This file subsets a vcf file to only print variants from a given chromosome (which has to match the chromosome naming scheme for the respective organism)

# Usage: ~/subVCFbyChrom.py in.vcf Hmel201 > out.vcf


from sys import argv


tChrom = argv[2]        # target chromosome to be kept

with open(argv[1], 'rb') as vcfile:
    for line in vcfile:
        if line[0] == '#':
            print line.split('\n')[0]
        else:
            scaf = line.split('\t')[0]


            #if scaf != old_scaf:
            #    print line.split('\n')[0]
            #else:
            #    if bp > old_bp + n_th:
            #        print line.split('\n')[0]
            #    else:
            #        continue
            #old_scaf, old_bp = scaf, bp
