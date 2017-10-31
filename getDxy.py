#! /usr/bin/python
#
# This script .

# Usage:

from sys import argv
#import numpy as np
#import re

import egglib


vcf = egglib.io.VcfParser(argv[1])









#maxCoverage = 997.2841
#
#
#dpList = list()
#with open(argv[1], 'rb') as vcfile:
#    for line in vcfile:
#        if line[0] == '#':
#            #continue
#            print line.split('\n')[0]
#        else:
#            dp = int(re.findall('DP=[0-9]+', line)[0].split('=')[1])
#            #dpList.append(dp)
#    #print np.mean(dpList), np.std(dpList), len(dpList)
#            if dp > maxCoverage:
#                continue
#            else:
#                print line.split('\n')[0]




