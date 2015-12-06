#! /usr/bin/python


# This script reads through a vcf file and extracts (for each SNV) the SNV id, reference allele frequency, alternative allele frequency, the genotype likelihoods for reference, heterozygote and alternative allele, sequence coverage, and the probability that the genotype call is wrong.
# Usage: ./ngs_tools/get_allele_freq_vcf.py <variants.vcf>  > allele_freq.txt



import sys
import re
from collections import OrderedDict


af_file = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    n_snv = 0
    n_no_num = 0
    n_num = 0
    line_dict = dict()
    for line in file:
        if line[0:2] == '##':
            continue
        elif line[0:2] == '#C':
            header = line.split('\t')
            ind_ids = header[9:len(header)]
            ind_ids[len(ind_ids)-1] = ind_ids[len(ind_ids)-1].split('\n')[0]
        else:
            line_list = line.split('\t')
            if len(line_list[4]) > 1:
                continue
            else:
                geno_likely = OrderedDict()
                n_snv += 1
                n_ind = len(ind_ids)
                scaffold = line_list[0].split('d')[1]
                pos = line_list[1]
                snv_id = ':'.join([scaffold, pos])
                af = re.findall('AF=[0.0-9.0a-z\-]+', line_list[7])
                af = float(af[0].split('=')[1])
                rf = 1 - af
                af_line = str(snv_id + ' ' + str(af) + '\n')
                af_file.write(af_line)
                for j, ind in enumerate(ind_ids):
                    ind_line = str()
                    if line_list[j+9][0:3] == './.':
                        rr, ra, aa = map(str,[0, 0, 0])
                        ind_line = str(rr + ' ' + ra + ' ' + aa)
                        n_no_num += 1
                        geno_likely[ind] = ind_line
                        #print ind, rr, ra, aa
                    else:
                        n_num += 1
                        gt_lklhd = line_list[j+9].split(':')
                        lklhd = gt_lklhd[4].split('\n')[0]
                        rr, ra, aa = lklhd.split(',')
                        #print ind, rr, ra, aa
                        ind_line = str(rr + ' ' + ra + ' ' + aa)
                        geno_likely[ind] = ind_line
                        #print ind_line
                    line_dict[snv_id] = ' '.join(geno_likely.values())
    file.close()
    af_file.close()

print n_ind, n_snv, n_no_num, n_num
print ' '.join(map(str, ind_ids))
it = iter(sorted(line_dict.iteritems()))
for key, value in it:
    print key, value


