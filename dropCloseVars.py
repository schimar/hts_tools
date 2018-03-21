#! /usr/bin/python
#
# This script filters a vcf file, where all variants that are physically less than 4 bp apart are dropped (since those might represent small inversions, or more generally, variants with bad alignment). A separate file, containing the scaffold and position (bp) has to be supplied (which can easily be generated with something like "grep -v '#' variants.vcf | cut -f1,2 -d$'\t' > snpids.txt"

# Usage: ./dropCloseVars.py snpids.txt helico30f1.vcf > helico30f2.vcf

import sys

mindist = 4
lc = 14807574



scaf = list()
pos = list()
keep = list()


with open(sys.argv[1], 'rb') as snpids:
    for j in range(lc):
        line = snpids.readline()
        scaf.append(line.split('\t')[0])
        pos.append(int(line.split('\t')[1]))



for i in range(lc):
    if i == lc - 1 :
        if scaf[i] == scaf[i-1] and pos[i]-pos[i-1] < mindist:
            keep.append(0)
            #print i, scaf[i], pos[i], scaf[i-1], pos[i-1], keep[i], pos[i]-pos[i-1]
        else:
            keep.append(1)
            #print i, scaf[i], pos[i], scaf[i-1], pos[i-1], keep[i], pos[i]-pos[i-1]
    elif i == 0:
        if scaf[i] == scaf[i+1] and pos[i+1]-pos[i] < mindist:
            keep.append(0)
            #print i, scaf[i], pos[i], scaf[i+1], pos[i+1], keep[i], pos[i+1]-pos[i]
        else:
            keep.append(1)
            #print i, scaf[i], pos[i], scaf[i+1], pos[i+1], keep[i], pos[i+1]-pos[i]
    else:
        if scaf[i] == scaf[i-1] and pos[i]-pos[i-1] < mindist and scaf[i] == scaf[i+1] and pos[i+1]-pos[i] < mindist:
            keep.append(0)
            #print i, scaf[i], pos[i], scaf[i+1], pos[i+1], scaf[i-1], pos[i-1], keep[i]
        else:
            keep.append(1)
            #print i, scaf[i], pos[i], scaf[i+1], pos[i+1], scaf[i-1], pos[i-1], keep[i]

#print len(keep), keep.count(0), keep.count(1)

with open(sys.argv[2], 'rb') as vcfile:
    for i, line in enumerate(vcfile):
        if line[0] == '#':
            print line.split('\n')[0]
        else:
            j = i - 828
            if keep[j] == 1:
                print line.split('\n')[0]
            else:
                continue



#nCommentLines = 0
#for i, line in enumerate(vcfile):
#    if line[0] == '#':
#        #print line.split('\n')[0]
#        nCommentLines += 1
#    else:
#        indx = i + 2 #+ nCommentLines
#        #"head -n829 helico30.vcf | tail -n2"
#        cmd = "head -n%i %s | tail -n2" % (indx, sys.argv[1])
#        #var = os.system(cmd)
#        varStr = subprocess.check_output([cmd], shell=True)
#        posList = varStr.split('\n')
#        scaf1, pos1 = posList[0].split('\t')[0:2]
#        scaf2, pos2 = posList[1].split('\t')[0:2]
#        print line.split('\t')[0], line.split('\t')[1], scaf1, pos1, scaf2, pos2, nCommentLines


#    for i, line in enumerate(vcfile):
#        vcfile.tell()
#        if line[0] == '#':
#            continue
#        else:
#            lastline = line
#            scaf1, pos1 = lastline.split('\t')[0:2]
#            newline = next(vcfile)
#            #newline = line
#            scaf2, pos2 = newline.split('\t')[0:2]
#            print scaf1, pos1, scaf2, pos2 #lastline, newline
#    else:
#        print scaf1, pos1



