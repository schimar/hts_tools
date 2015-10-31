#! /usr/bin/python


# This script reads through a vcf file and extracts (for each SNV) the SNV id, reference allele frequency, alternative allele frequency, the genotype likelihoods for reference, heterozygote and alternative allele, sequence coverage, and the probability that the genotype call is wrong.
# Usage: ./ngs_tools/get_allele_freq_vcf.py <variants.vcf>  > allele_freq.txt



import sys
import re

with open(sys.argv[2], 'rb') as codS_file:
    scaf = dict()
    for line in codS_file:
        line_list = line.split('\t')
        cscaf = line_list[0].split(':')[1].split('_')[1]
        start = line_list[1]
        stop = line_list[2].split('\n')[0]
        if not cscaf in scaf:
            scaf[cscaf] = [str(start + ' ' + stop)]
        else:
            scaf[cscaf].append((str(start + ' ' + stop)))
#print len(scaf.keys()), len(scaf.values())

with open(sys.argv[1], 'rb') as file:
    for line in file:
        line_list = line.split(' ')
        scaffold, snv_id = line_list[0].split(':')
        naive_freq = line_list[1]
        final_freq = line_list[2]
        if scaffold in scaf:
            for key in scaf[scaffold]:
                print key.split(' ')
        else:
            continue
            
            #print scaffold, len(scaf[scaffold])
        #print scaffold, snv_id, naive_freq, final_freq

   
    file.close()
    codS_file.close()
        
