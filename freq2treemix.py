#! /usr/bin/python
#
# This file reads through 1) a text file with (ref) allele frequencies as rows and populations/species as columns, and 2) a space-separated file containing the population/species and the number of individuals. It then calculates allele counts for ref and alt alleles, and prints those in treemix format (ref|alt) for each SNV and population.

# Usage: ~/hts_tools/freq2treemix.py freq_all_species.csv spec_num

from __future__ import division
from sys import argv



with open(argv[2], 'rb') as ind_num:
    num_dict = dict()
    for line in ind_num:
        pop, num = line.split('\n')[0].split(' ')
        num_dict[pop] = num
    ind_num.close()

#for key, value in num_dict.iteritems():
#    print key, value



with open(argv[1], 'rb') as freqs:
    for line in freqs:
        if line[0:1] == '#':
            header = line.split('#')[1].split('\n')[0].split(' ')
            print ' '.join(header)
        else:
            freqs_line = list()
            line_list = line.split('\n')[0].split(' ')
            for i, pop in enumerate(header):
                ref_freq = float(line_list[i])*(2*float(num_dict[pop]))
                alt_freq = (1-float(line_list[i]))*(2*float(num_dict[pop]))
                freq2N = ','.join([str(int(round(ref_freq))), str(int(round(alt_freq)))])
                freqs_line.append(freq2N)
            print ' '.join(freqs_line) #, num_dict[pop], line_list[i], 1-float(line_list[i])
    freqs.close()




