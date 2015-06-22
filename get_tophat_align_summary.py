#! /usr/bin/python
# 
# 

# Usage: ./get_tophat_align_summary.py <sample_no> <new_file_name.txt>


import sys
import re
#import shutil


#newfile = open(sys.argv[2], 'a')
sample = sys.argv[1]
mapped= str()
mult_aln= str()
mult_rate= str()
align_20= str()
aln_rate= str()
with open('align_summary.txt', 'rb') as file:
	for line in file:
            if line.split() == []:
                continue
            else:
                if re.findall('Input', line):
                    reads = re.findall('[0-9]+', line)[0]
                elif re.findall('Mapped', line):
                    mapped = re.findall('[0-9]+', line)
                elif re.findall('of these', line):
                    mult_aln = re.findall('[0-9]+', line)[0]
                #    mult_rate = str(float(re.findall('[0-9]+\.[0-9]+', line)[0])/100)
                    align_20 = re.findall('[0-9]+', line)[3]
                #elif re.findall('overall', line):
                #    aln_rate = str(float(re.findall('[0-9]+\.[0-9]+', line)[0])/100)
                else:
                    continue
        print reads, mapped[0], float(mapped[1])/100, mult_aln, align_20
        #newline = str(reads + '\t' + mapped[0] + '\t' + mult_aln + '\t' + mult_rate + '\t' + align_20 + '\t' + aln_rate)
        #print newline


            #        newline = str(line)
            #        newfile.write(newline)
	file.close()
    #newfile.close()


