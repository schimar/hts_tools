#! /usr/bin/python
#
# This file reads through a vcf file and a space-separated file assigning populations to individuals (ind, pop). The resulting file prints the number of reference and alternative alleles pewr population. Note that currently, the population names are printed in the last line of the file, which needs to be moved to line 1.

# Usage: ~/hts_tools/freq2treemix.py *_freq

from sys import argv



with open(argv[2], 'rb') as pop_file:
    pops = dict()
    for line in pop_file:
        ind, pop = line.split(' ')
        pops[ind] = pop.split('\n')[0]

#for key, value in pops.iteritems():
#    print value


with open(argv[1], 'rb') as file:
    for line in file:
        if line[0:2] == '##':
            continue #print line.split('\n')[0]
        elif line[0:2] == "#C":
            line_list = line.split('\t')
            inds = line_list[9:len(line_list)]
            last_ind = inds[-1].split('\n')[0]
            inds[-1] = last_ind
        else:
            line_list = line.split('\t')
            ref_count = dict()
            if len(line_list[4]) > 1:
                continue
            else:
                scaf, bp = line.split('\t')[0:2]
                vcf_inds = line_list[9:len(line_list)]
                for i, ind in enumerate(inds):
                    if not pops[ind] in ref_count:
                        ad = vcf_inds[i].split(':')[1]
                        if ad == '.':
                            ref_count[pops[ind]] = [0, 0]
                        else:
                            ad = ad.split(',')
                            ref_count[pops[ind]] = map(int, ad)
                    else:
                        if ad == '.':
                            ref_count[pops[ind]][0] += 0
                            ref_count[pops[ind]][1] += 0
                        else:
                            ref_count[pops[ind]][0] += int(ad[0])
                            ref_count[pops[ind]][1] += int(ad[1])
                newline = list()
                keys = list()
                for key, value in ref_count.iteritems():
                    keys.append(key)
                    val = ','.join(map(str, value))
                    newline.append(val)
                newline = ' '.join(newline)
                print newline

    print keys
    file.close()
