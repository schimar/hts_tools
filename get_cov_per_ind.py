#! /usr/bin/python
#
# This file reads through a vcf file and prints a space-separated text file, containing the coverage for each SNV (rows) and individual (columns). Alt and ref alleles are summed to total coverage at each SNV and locus.

# Usage: ~/hts_tools/get_cov_per_ind.py fltrd_pubRetStri_dipUG35_200bp.vcf > outfile

from sys import argv

with open(argv[1], 'rb') as file:
    for line in file:
        if line[0:2] == '##':
            continue #print line.split('\n')[0]
        elif line[0:2] == "#C":
            line_list = line.split('\t')
            inds = line_list[9:len(line_list)]
            last_ind = inds[-1].split('\n')[0]
            inds[-1] = last_ind
            print ' '.join(inds)
        else:
            line_list = line.split('\t')
            ref_count = dict()
            if len(line_list[4]) > 1:
                continue
            else:
                scaf, bp = line.split('\t')[0:2]
                vcf_inds = line_list[9:len(line_list)]
                count_list = list()
                for i, ind in enumerate(inds):
                    count = int()
                    if vcf_inds[i] == './.':
                        count += 0
                    else:
                        ad = vcf_inds[i].split(':')[1]
                        if ad == '.':
                            count += 0
                        else:
                            ad = ad.split(',')
                            count += int(ad[0]) + int(ad[1])
                    count_list.append(str(count))
                print ' '.join(count_list)
    file.close()
