#! /usr/bin/python
#

# This script reads through a vcf file and a corresponding file containing the
# estpEM allele frequencies and calculates Fis values per locus for every locus
# that has MAF >= <MAFthreshold>. If Fis values for said locus are
# < Fisthreshold, then the respective locus will be filtered out (We assume that
# these loci are the result of duplicate reads being incorrectly aligned, thus
# appearing as heterozygotes)

# USAGE: ~/hts_tools/mafFisfltr.py infile.vcf freqfile maf_th Fisthreshold > outfile.vcf
# ~/hts_tools/mafFisfltr.py lasio107rare.vcf l107estpEM.txt 0.3 0.1 > l107Fisfltrd.vcf

from sys import argv


maf_th = float(argv[3])   # maf threshold
fis_th = float(argv[4])   # Fis threshold

pos = list()
mafs = dict()
with open(argv[2], 'rb') as freqs:
    for line in freqs:
        lspl = line.split('\n')[0].split(' ')
        maf = min(float(lspl[2]), 1 - float(lspl[2]))
        mafs[lspl[0]] = maf
        #print lspl[0], mafs[lspl[0]]
    freqs.close()

with open(argv[1], 'rb') as file:
    for line in file:
        if line[0:2] == '##':
            continue
            #print line.split('\n')[0]
        elif line[0:2] == '#C':
            continue
            #print line.split('\n')[0]
        else:
            lspl = line.split('\n')[0].split('\t')
            #print lspl[4]
            if len(lspl[4]) > 1:
                continue
            else:
                #scaf = lspl[0].split('d')[1]      # if "ScaffoldXXXX"
                scaf = lspl[0].split('-')[1]      # if vsearch format
                pos = str(scaf + ':' + lspl[1])
                #print mafs[pos]
                if mafs[pos] >= maf_th:
                    #print pos, mafs[pos]
                    gts = lspl[9:len(lspl)]
                    nInd = len(gts)
                    pq = [0.0, 0.0]
                    nAa = 0.0
                    for gt in gts:
                        gl_ind = list()
                        gl = gt.split(':')[4].split(',')
                        if min(gl) == '.':
                            continue
                        else:
                            gtix = gl.index(min(gl))
                            if gtix == 0:
                                pq[0] += 2
                            elif gtix == 1:
                                pq[0] += 1
                                pq[1] += 1
                                nAa += 1
                            else:
                                pq[1] += 2
                    pq = [pq[0]/(2*nInd), pq[1]/(2*nInd)]
                    Ho = nAa/nInd
                    He = 2*pq[0]*pq[1]
                    if He == 0:
                        continue
                    else:
                        Fis = (He-Ho)/He
                    q = (1-mafs[pos])  # major allele freq
                    maxNegFis = 1 - (1/q)   # maximum possible negative Fis value
                    maxNegFis_ubound = maxNegFis + abs(fis_th*maxNegFis)
                    Fis_scaled = Fis/abs(maxNegFis)
                    #print Fis, maxNegFis, maxNegFis_upper
                    #, mafs[pos], nInd, He, Ho, pq, nAa#, pq, mafs[pos], nInd, nAa, pq  #, mafs[pos], nInd
                    if Fis <= maxNegFis_ubound:
                        #print Fis, maxNegFis, Fis_scaled, maxNegFis_ubound, mafs[pos]
                        continue
                        # divide by maxNegFis
                    else:
                        print Fis, maxNegFis, Fis_scaled, maxNegFis_ubound, mafs[pos]
                        #print line.split('\n')[0]
                        #continue
                else:
                    continue
                    #print line.split('\n')[0]





    file.close()
