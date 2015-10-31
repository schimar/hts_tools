#! /usr/bin/python


# This script reads through a vcf file and extracts (for each SNV) the SNV id, reference allele frequency, alternative allele frequency, the genotype likelihoods for reference, heterozygote and alternative allele, sequence coverage, and the probability that the genotype call is wrong.
# Usage: ./ngs_tools/get_allele_freq_vcf.py <variants.vcf>  > allele_freq.txt



import sys
import re



 = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    for line in file:
        line_list = line.split(' ')
        scaffold, snv_id = line_list[0].split(':')
        naive_freq = line_list[1]
        final_freq = line_list[2]

        #print scaffold, snv_id, naive_freq, final_freq



      
      
      
      
      
    file.close()
        
