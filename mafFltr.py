#! /usr/bin/python
#
# This script filters a vcf file based on minor allele frequency (MAF), where a MAF-threshold has to be supplied as a command line argument. Note that this script can easily be modified to parse for rare variants by changing the sign on line 42 (change '>=' to '<'). Additionally, note that variants with more than alternative allele will be removed, if present.

# Usage: ~/hts_tools/mafFltr.py fltrd80lasio161dip.vcf 0.05 > out.vcf

from __future__ import division
from sys import argv
import re

maf_th = float(argv[2])   # maf threshold


with open(argv[1], 'rb') as file:
    for line in file:
        if line[0:2] == '##':
            print line.split('\n')[0]
        elif line[0:2] == '#C':
            print line.split('\n')[0]
        else:
            line_list = line.split('\n')[0].split('\t')
            if len(line_list[4]) > 1:
                continue
            else:
                gts = line_list[9:len(line_list)]
                allele_list = [0.0,0.0]
                for gt in gts:
                    gl_ind = list()
                    gl = gt.split(':')[4].split(',')
                    if min(gl) == '.':
                        continue
                    else:
                        gtix = gl.index(min(gl))
                        if gtix == 1:
                            allele_list[0] += 2
                        elif gtix == 2:
                            allele_list[0] += 1
                            allele_list[1] += 1
                        else:
                            allele_list[1] += 2
                maf = min(allele_list)/(min(allele_list) + max(allele_list))
                if maf >= maf_th:
                    print line.split('\n')[0]
                else:
                    continue
    file.close()

