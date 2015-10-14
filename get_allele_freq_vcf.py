#! /usr/bin/python


# This script reads through an annototation file (in gff3 format) and 
# extracts the length of a gene (only for type gene). The output file
# contains the gene name as well as the length of the given gene. 
#

# Usage: ./get_gene_length_from_gff3.py <gff3-file-name> <output_file.csv>



import sys
import re



#newfile = open(sys.argv[2], 'a')
with open(sys.argv[1], 'rb') as file:
    n_snv = 0
    for line in file:
        if line[0] == '#':
            continue
        else:
            line_list = line.split('\t')
            #print line_list[9]
            if len(line_list[4]) > 1:
                continue#print len(line_list[4])
            else:
                n_snv += 1
                gt_lklhd = line_list[9].split(':')[1]
                rr, ra, aa = map(int, gt_lklhd.split(','))
                print rr, 10**(rr/-10), ra, 10**(ra/-10), aa, 10**(aa/-10)
                #rr = 10**(rr/-10)
                #ra = 10**(ra/-10)
                #aa = 10**(aa/-10)
                #print rr, ra, aa
                #if rr > ra and rr > aa:
                    #print rr, line_list[4], ra, aa, gt_lklhd
                #elif ra > rr and ra > aa:
                    #print ra, line_list[4], rr, aa, gt_lklhd
                #else: 
                    #print aa, line_list[4], rr, aa, gt_lklhd
    print n_snv
            #type = line_list[2]
            #gene = re.findall('[A-Z][a-z]+\.[0-9]+s[0-9]+\.v[0-9]+\.[0-9]+', line_list[8])
            #start, end = int(line_list[3]), int(line_list[4])
            #length = end - start +1
            #if type != 'gene':
                #continue
            #else:
             #   newline = str(gene[0] + '\t' + str(length) + '\n')
             #   newfile.write(newline)

    file.close()
    #newfile.close()
        
