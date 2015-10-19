#! /usr/bin/python


# This script reads through a vcf file and extracts (for each SNV) the SNV id, reference allele frequency, alternative allele frequency, the genotype likelihoods for reference, heterozygote and alternative allele, sequence coverage, and the probability that the genotype call is wrong.
# Usage: ./ngs_tools/get_allele_freq_vcf.py <variants.vcf>  > allele_freq.txt



import sys
import re



#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    n_snv = 0
    for line in file:
        if line[0:2] == '##':
            continue
        elif line[0:2] == '#C':
            header = line.split('\t')
            ind_ids = header[9:len(header)]
            print ind_ids, len(ind_ids)
        else:
            line_list = line.split('\t')
            if len(line_list[4]) > 1:
                continue
            else:
                n_snv += 1
                gt_lklhd = line_list[9].split(':')
                id = line_list[1]
                rr, ra, aa = map(int, gt_lklhd[1].split(','))
                cov = int(gt_lklhd[2])
                prob_F = 10**(int(gt_lklhd[3])/-10)
                af = re.findall('AF1=[0.0-9.0]+', line_list[7])
                af = float(af[0].split('=')[1])
                rf = 1 - af
                rr = 10**(rr/-10)
                ra = 10**(ra/-10)
                aa = 10**(aa/-10)
                #print id, rf, af, rr, ra, aa, cov, prob_F

#    print n_snv
    file.close()
        
