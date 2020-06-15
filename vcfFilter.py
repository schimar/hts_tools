#! /usr/bin/python
#
# This script filters a vcf file based on overall sequence coverage, number of
# non-reference reads, number of alleles, and reverse orientation reads.
# See below for default values, and to change them, if necessary. Additionally,
# note that currently, the number of retained loci is not being written at the end
# of the file.
# Usage: ./vcfFilter.py <variant file>.vcf > outfile.vcf

import sys
import re
import shutil
#import tempfile

### stringency variables, edit as desired
minCoverage = 128 # minimum number of seqs; DP
minAltRds = 4 # minimum number of sequences with the alternative allele; AC
notFixed = 1.0 # removes loci fixed for alt; AF
mapQual = 30 # minimum mapping quality

# added 10/02/17
minBqrs = -8 # minimum absolute value of the base quality rank sum test; BaseQRankSum
minMqrs = -12.5 # minimum absolute value of the mapping quality rank sum test; MQRankSum
minRprs = -8 # minimum absolute value of the read position rank sum test; ReadPosRankSum
minQd = 2 # minimum ratio of variant confidenct to non reference read depth; QD
maxFish = 60 # maximum phred-scaled p-value using Fisher's Exact Test to detect strand bias (the variation being seen on only the forward or only the reverse strand) in the reads. More bias is indicative of false positive calls; FS

n_seqs_retained = int()
with open(sys.argv[1], 'rb') as file:
    for line in file:
        line = line.decode('utf-8')
        if line[0] == '#':
            #continue
            print(line.split('\n')[0])
        elif len(line.split('\t')[4]) > 1:
            continue
        else:
            dp = int(re.findall('DP=[0-9]+', line)[0].split('=')[1])
            ac = int(re.findall('AC=[0-9]+', line)[0].split('=')[1])
            af = float(re.findall('AF=[0.0-9.0]+', line)[0].split('=')[1])
            #
            if af == notFixed:
                continue
            else:
                try:
                    bqrs = float(re.findall('BaseQRankSum=[\-?0.0-9.0]+', line)[0].split('=')[1])
                    mqrs = float(re.findall('MQRankSum=[\-?0.0-9.0]+', line)[0].split('=')[1])
                    rprs = float(re.findall('ReadPosRankSum=[\-?0.0-9.0]+', line)[0].split('=')[1])
                    qd = float(re.findall('QD=[0.0-9.0]+', line)[0].split('=')[1])
                    fish = float(re.findall('FS=[0.0-9.0]+', line)[0].split('=')[1])
                    mq = float(re.findall('MQ=[0.0-9.0]+', line)[0].split('=')[1])
                    if (dp >= minCoverage and ac >= minAltRds and af != notFixed and mq >= mapQual and bqrs >= minBqrs and mqrs >= minMqrs and rprs >= minRprs and qd >= minQd and fish <= maxFish):
                        print(line.split('\n')[0])

                    #print bqrs, mqrs, rprs, qd, fish
                    #if re.

                except:
                    continue
                    #print line












            #
            #if re.findall('MQ=NaN', line):
            #    continue # some of the MQ are NaN, let's just skip those (they would be filtered out anyways)
            #else:
            #    mq = float(re.findall('MQ=[0.0-9.0]+', line)[0].split('=')[1])
            #    if (dp >= minCoverage and ac >= minAltRds and af != notFixed and mq >= mapQual):
            #        print line.split('\n')[0]
            #        n_seqs_retained += 1
            #    else:
            #        continue
    file.close()

#print '#Retained %i variable loci' % n_seqs_retained
