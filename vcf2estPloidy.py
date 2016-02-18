#! /usr/bin/python


# This scripts reads a vcf file and outputs two files, containing 1) the allele depth for the reference allele and 2) for the alternative allele (where only heterozygotes are considered for both) with individuals as rows and SNVs as columns. (Rownames and colnames are being written, as well)
# Homozygotes are given <NA>

# Usage: ./hts_tools/vcf2estPploidy.py b346_sub.vcf ref alt

from sys import argv


ref_file = open(argv[2], 'a')
alt_file = open(argv[3], 'a')

def parsePL(ad, pl):
    """Take the allele depth (AD) and phred-scaled genotype likelihoods (PL), and return the appropriate allele depths for only heterozygotes (determined by highest likelihood), and <NA> otherwise"""
    pl_ix = pl.index(min(pl))
    #return pl_ix
    if pl_ix == 1:
        return ad
    else:
        return 'NA,NA'




with open(argv[1], 'rb') as file:
    snv_per = dict()
    snv_list = list()
    for line in file:
        if line[0:2] == '##':
            continue
        elif line[0:2] == '#C':
            header = line.split('\n')[0].split('\t')
            ind_ids = header[9:len(header)]
            #print len(header), len(ind_ids)
        else:
            line_list = line.split('\t')
            if len(line_list[4]) > 1:
                continue
            else:
                n_ind = len(ind_ids)
                scaffold = line_list[0].split('d')[1]
                pos = line_list[1]
                snv_id = ':'.join([scaffold, pos])
                snv_list.append(snv_id)
                for j, ind in enumerate(ind_ids):
                    ad = line_list[j+9].split(':')[1]
                    pl = line_list[j+9].split(':')[4].split(',')
                    if line_list[j+9][0:3] == './.':
                        if not ind in snv_per:
                            snv_per[ind] = list()
                            snv_per[ind].append('NA,NA')
                            #print 'NA'
                        else:
                            snv_per[ind].append('NA,NA')
                            #print 'NA'
                    else:
                        if not ind in snv_per:
                            snv_per[ind] = list()
                            snv_per[ind].append(parsePL(ad, pl))
                            #print parsePL(ad, pl)
                        else:
                            snv_per[ind].append(parsePL(ad, pl))
    ref_file.write(str(' '.join(snv_list) + '\n'))
    alt_file.write(str(' '.join(snv_list) + '\n'))
#print ' '.join(snv_list)



for key, value in snv_per.iteritems():
    refline = list()
    altline = list()

#    print key, ' '.join(value)
    for snv in value:
        refline.append(snv.split(',')[0])
        altline.append(snv.split(',')[1])
    newref = str(key + ' ' + ' '.join(refline) + '\n')
    newalt = str(key + ' ' + ' '.join(altline) + '\n')
    ref_file.write(newref)
    alt_file.write(newalt)

# maybe don't write two separate files, but simply one (with print ' '.join(value))

alt_file.close()
ref_file.close()
file.close()

