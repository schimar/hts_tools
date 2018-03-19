#! /usr/bin/python
#
# This file subsets a vcf file to only print variants from a list of scaffolds

# Usage: ~/subVCFbyChromList.py in.vcf scafs.txt > out.vcf


from sys import argv

with open(argv[2], 'rb') as chromfile:
    chromls = list()
    for line in chromfile:
        chrom = line.split('\n')[0]
        chromls.append(chrom)


with open(argv[1], 'rb') as vcfile:
    for line in vcfile:
        if line[0] == '#':
            print line.split('\n')[0]
            #continue
        else:
            scaf = line.split('\t')[0]
            chrom = scaf[0:7]
            #print chrom == tChrom
            if chrom in chromls:
                print line.split('\n')[0]
            else:
                continue


