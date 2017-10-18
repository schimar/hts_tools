#! /usr/bin/python
#
# This script filters a vcf file, where all variants are dropped, that have very high read depth compared
# to the mean read depth across all variants (maxCov = mean + 3*sd).

# Usage: ./dropHighCovVars.py helico30f2.vcf > helico30f3.vcf

from sys import argv
import numpy as np
import re

# helico30f2maf5.vcf: mean + 3sd = 452.655272786 + 3 * 181.54293551

maxCoverage = 997.2841


dpList = list()
with open(argv[1], 'rb') as vcfile:
    for line in vcfile:
        if line[0] == '#':
            #continue
            print line.split('\n')[0]
        else:
            dp = int(re.findall('DP=[0-9]+', line)[0].split('=')[1])
            #dpList.append(dp)
    #print np.mean(dpList), np.std(dpList), len(dpList)
            if dp > maxCoverage:
                continue
            else:
                print line.split('\n')[0]


# mean coverage is 452.655272786 and sd = 181.54293551, with 12795758 variants  (for helico30f2maf5.vcf)


