#! /usr/bin/python
# 
### This simple bash script reads the gene expression counts from a given file and creates a presence-absence dataframe, where each cell is 0 if no expression and 1 when expressed.

# Usage: ./get_pres_abs_df.py /home/schimar/Desktop/boechera/rna_seq/manuscript/data/df_baySeq_all_GO.txt > <output file>.txt>


import sys
import re
#import shutil
#import tempfile


bayS_dict = dict()
# read the baySeq file 
with open(sys.argv[1], 'rb') as file:
    newline = list()
    for i, line in enumerate(file):
        if i == 0:
            continue
        else:
            line_list = line.split('\t')
            expression = line_list[2:26]
            pres_abs = list()
            for j, value in enumerate(expression):
                #print j,int(value)
                if int(value) == 0:
                    pres_abs.append(0)
                else:
                    pres_abs.append(1)
            if len(pres_abs) == 24:
                #pres_abs.append('\n')
                newline = ", ".join(map(str, pres_abs))
                print(newline)
                #print(str(newline + '\n'))                
            else: 
                continue
                
    file.close()





