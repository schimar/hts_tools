#! /usr/bin/python
#
# This file subsets a vcf file based on a threshold number of base pairs, which needs to be supplied as the second argument. (I used 200 bp)

# Usage: ~/sub_vcf_by_snv.py file.vcf 200 > outfile.vcf


import sys
n_th = int(sys.argv[2])

with open(sys.argv[1], 'rb') as file:
    old_scaf = int()
    old_bp = int()
    for line in file:
        if line[0] == '#':
            print line.split('\n')[0]
        else:
            scaf, bp = line.split('\t')[0:2]
            bp = int(bp)
            if scaf != old_scaf:
                print line.split('\n')[0]
            else:
                if bp > old_bp + n_th:
                    print line.split('\n')[0]
                else:
                    continue
            old_scaf, old_bp = scaf, bp
