#! /usr/bin/python
#
# This script returns a genotype matirx (locus by ind) with genotype
## means (point estimates) from a genotype likelihood file; a HW prior is used based on allele frequencies provided in a separate file

## USAGE:  ~/hts_tools/gl2genestDip.py file.gl af_file.txt

from __future__ import division

from sys import argv

with open(argv[2], 'rb') as freq_file:
    freqs = list()
    freqs.append(0)
    freqs.append(0)
    for line in freq_file:
        freq = line.split('\n')[0]
        freqs.append(float(freq))

    #for freq_line in freqs:
    #    fq = freq_line
        #print fq**2, (fq*(1-fq)), ((1-fq)**2), fq
    #print len(freqs)
    freq_file.close()



with open(argv[1], 'rb') as file:
    for i, line in enumerate(file):
        if line[0:3] == '79 ':     # hard-coded, change as needed (the first 3 characters of line 1)
            continue
        elif line[0:2] == 'CR':    # hard-coded, change as needed (the first two letters of line 2 (individuals)
            inds = line.split('\n')[0].split(' ')
            #print ' '.join(inds)
        else:
            newline = list()
            line_list = line.split('\n')[0].split(' ')
            scafPos = line_list[0]
            gl_list = line_list[1:len(line_list)]
            fq = freqs[i]
#           if freqs[i] == 0.0000:
#               fq = 0.0001
#           else:
#               fq = freqs[i]
            for j, ind in enumerate(inds):
                lklhd_list = list()
                for k in [0,1,2]:        # there are 3 values per variant
                    l = j*3+k
                    lklhd = 10**(float(gl_list[l])/-10) # convert from phred
                    lklhd_list.append(lklhd)
                #print lklhd_list, scafPos
                priors = [(1-fq)**2, 2*((1-fq)*fq), (fq**2)] # Hardy-Weinberg priors
                post_freqs = [priors[0]*lklhd_list[0], priors[1]*lklhd_list[1], priors[2]*lklhd_list[2]]
                pfq_sum = sum(post_freqs)
                #maxgprob = int()
                prob012list = list()
                ##### test
#               if sum(post_freqs) == 0.0:
#                   print i, post_freqs, sum(post_freqs), ind, scafPos, lklhd_list, priors, fq
#               else:
#                   continue
                for m in [0,1,2]:
                    nm_pf = post_freqs[m]/pfq_sum # divide posterior frequencies by their sum (for each genotype) to normalize
                    prob012 = nm_pf * m      # scale to 0-1-2 format
                    prob012list.append(prob012)
                    #print nm_pf, post_freqs[m], m, prob012list
                    #if maxgprob < prob012list[m]:
                    #    maxgprob = prob012list[m]
                    #else:
                    #    continue
                    if m == 2:
                        newline.append(sum(prob012list)) #, maxgprob
                    else:
                        continue
            if 'newline' in locals():
                print ' '.join(map(str, newline))
            else:
                continue

    file.close()


