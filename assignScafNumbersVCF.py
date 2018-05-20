#!/usr/bin/python

# This script reads through all variants in a vcf file and prints a numeric scaffold for each new scaffold encountered, with length equal to the number of variants. Additionally, a second file is written that prints both the scaffold  name, the bpPosition, and the assigneed number to a second file.

# Usage: ~/get_num_snvs_per_scaf.py vars.py scafBpNumOut.txt > scafNums.txt

from sys import argv

newfile = open(argv[2], 'a')

# read gl file for scaffold:bp pos
with open(argv[1], 'rb') as vcfile:
    oldScaf = str()
    scafNum = 0
    for line in vcfile:
        if line[0] == "#":
            continue
        else:
            newScaf = line.split('\t')[0]
            bp = line.split('\t')[1]
            #print newScaf, bp
            if newScaf == oldScaf:
                print scafNum
            else:
                scafNum += 1
                print scafNum
                oldScaf = newScaf
                newline = str(newScaf + ' ' + bp + ' ' + str(scafNum) + '\n')
        newfile.write(newline)


vcfile.close()
newfile.close()


