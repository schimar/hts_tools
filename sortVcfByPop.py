#! /usr/bin/python3


# This scripts reads a vcf file and an id file with individuals and their population affiliation (space-separated file format). Note that the id file needs to be sorted by pop (in Bash: sort -k2 id_file.txt).
# The output is a vcf file with individuals ordered by population (where individuals within each pop are not ordered).
#
# Usage: ./sortVcfByPop.py <vcf_file> <ids/pops file> > outfile.vcf

#from collections import OrderedDict
from sys import argv
#import re


with open(argv[2], 'rb') as ids:
    dpops = dict()
    #n_ind = 0
    for line in ids:
        line = bytes.decode(line).strip('\n')
        ind, pop = line.split(' ')
        if not pop in dpops:
            dpops[pop] = [ ind ]
        else:
            dpops[pop].append(ind)
        #n_ind += 1
ids.close()

dpopsflat = [ item for sublist in list(dpops.values()) for item in sublist ]


with open(argv[1], 'rb') as file:
    for line in file:
        line = bytes.decode(line).strip('\n')
        if line[0:2] == '##':
            print(line)
            #continue
        elif line[0:2] == '#C':
            linels = line.split('\t')
            newline = linels[0:9]
            vcf_inds = linels[9:len(linels)]
            INDex = [ vcf_inds.index(x) if x in vcf_inds else None for x in dpopsflat ]
            lineINDex = [ x+9 for x in INDex ]
            newline.extend([ vcf_inds[i] for i in INDex ])
            print('\t'.join(newline))
        else:
            linels = line.split('\t')
            newline = linels[0:9]
            indline = [ linels[i] for i in lineINDex ]
            newline.extend(indline)
            print('\t'.join(newline))
    file.close()

