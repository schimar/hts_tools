#! /usr/bin/python
#
# This script reads through a gprob file (output of entropy) and calculates heterozygosity for each individual across all SNVs.

###
from __future__ import division
import sys

with open(sys.argv[1], 'rb') as file:
    for line in file:
        line_spl = line.split(',')
        if line_spl[0] == 'individual':
            n_vars = int(len(line_spl)-1)
        else:
            #hets = float()
            n_hets = int()
            gprobs = line_spl[1:len(line_spl)]
            for gt in gprobs:
                gtr = round(float(gt))
                if gtr == 2.0:
                    n_hets += 1
                else:
                    continue
            hets = n_hets/n_vars
            print(hets)


    file.close()


