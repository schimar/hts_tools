#! /usr/bin/python


# This scripts reads a gl (genotype likelihood) file and a file with individuals
# to be selected (one sample id per line). The output is a gl file with only the selected individuals.
# Note that lines 2 and 4 have to be deleted (will hopefully be fixed soon. 
#
# Usage: ./sub_gl.py <gl_file> <select ids file> > outfile.gl


import sys
import re
#from collections import OrderedDict


with open(sys.argv[2], 'rb') as select_ids:
     ind_list = list()
     n_ind = 0
     for line in select_ids:
         n_ind += 1
         ind_list.append(line.split('\n')[0])
select_ids.close()


with open(sys.argv[1], 'rb') as file:
    ix_list = list()
    select_inds = list()
    for line in file:
        new_line = list()
        if len(line) <= 10:
            n_loci = line.split(' ')[1]
            print n_ind, n_loci.split('\n')[0] # number loci
        elif line[0:2] == "CR":
            gl_inds = line.split(' ')
            for j, ind in enumerate(gl_inds):
                if ind in ind_list:
                    ix_list.append((j * 3) + 1), ix_list.append((j*3) + 2),
                    ix_list.append((j*3) + 3)
                    select_inds.append(ind)

                else: 
                    continue
            last_ind = select_inds[-1].split('\n')[0]
            select_inds[-1] = last_ind
            print ' '.join(select_inds)
        else:
            old_line = line.split()
            new_line.append(old_line[0])
            for ix in ix_list:
                new_line.append(old_line[ix])
        print ' '.join(new_line)

    file.close()

