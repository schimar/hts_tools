#! /usr/bin/python
# 
# 

# Usage: ./get_tophat_align_summary.py <sample_no> <new_file_name.txt>


import sys
import re
#import shutil


#newfile = open(sys.argv[2], 'a')
sample = sys.argv[1]
with open('align_summary.txt', 'rb') as file:
	for line in file:
            #line = str(line)
            if line.split() == []:
                continue
            else:
                if re.findall('Input', line):
                    reads = re.findall('[0-9]+', line)
                elif re.findall('Mapped', line):
                    mapped = re.findall('[0-9]+', line)
                elif re.findall('of these', line):
                    mult_aln = re.findall('[0-9]+', line)[0]
                    mult_rate = str(float(re.findall('[0-9]+\.[0-9]+',
                                                     line)[0])/100)
                    align_20 = re.findall('[0-9]+', line)[3]
                elif re.findall('overall', line):
                    aln_rate = str(float(re.findall('[0-9]+\.[0-9]+',
                                                    line)[0])/100)
                else:
                    continue
        newline = str(reads + '\t' + mapped + '\t' + mult_aln + '\t' + mult_rate + '\t' + align_20 + '\t' + aln_rate)



            #        newline = str(line)
            #        newfile.write(newline)
	file.close()
    #newfile.close()


