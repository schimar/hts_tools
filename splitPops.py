#! /usr/bin/python


# This scripts reads a vcf file and a file with individuals to be selected (one sample id per line).
# The output is a vcf file with only the selected individuals.
#
# Usage: ./sub_vcf.py <vcf_file> <select ids file> > outfile.vcf


import sys
#import re
import fileinput as fi

def vcf_ify(name):
    """Take a variable and attach ".vcf" to its end"""
    name = str(name)
    new = str('fltrd_200bp' + name + '.vcf')
    print new

#def split_line_per_pop(line_list, inds):
#    """Read a data line in a vcf file and a list of individuals to create separate lists (for each population/species), containing the first 9 objects (CHROM POS ID etx.) and each individual's data entry for the given population/species"""
#    chromPos = line_list[0:9]
#    geno = line_list[9:len(line_list)]
#    for i, ind in enumerate(inds):
#        continue





# read the pop_spec file (ind, pop/species; space-separated)
with open(sys.argv[2], 'rb') as pop_spec:
    pop_dict = dict()
    pop_list = list()
    ind_dict = dict()
    for line in pop_spec:
        ind, pop = line.split(' ')
        pop = pop.split('\n')[0]
        if not ind in pop_dict:
            pop_dict[ind] = list()
            pop_dict[ind].append(pop)
        else:
            pop_dict[ind].append(pop)
        if not pop in pop_list:
            pop_list.append(pop)
        else:
            continue



with open(sys.argv[2], 'rb') as pop_spec:
    ind_dict = dict()
    for line in pop_spec:
        ind, pop = line.split(' ')
        pop = pop.split('\n')[0]
        if not pop in ind_dict:
            ind_dict[pop] = list()
            ind_dict[pop].append(ind)
        else:
            ind_dict[pop].append(ind)
pop_spec.close()


# open files for writing (for each pop/species)
file_list = dict()
for i, name in enumerate(pop_list):
    pop_file = str('fltrd_200bp_' + name + '.vcf')
    file_list[name] = open(pop_file, 'a')


#file_list['stricta'].write("hello\n")



#for key, value in ind_dict.iteritems():
#    print key, len(value)



with open(sys.argv[1], 'rb') as file:
#   ix_list = list()
#   select_inds = list()
    for line in file:
#       new_line = list()
        if line[0:2] == '##':
            #print line.split('\n')[0]
            continue
        elif line[0:2] == '#C':
            line_list = line.split('\n')[0].split('\t')
            chromPos = line_list[0:9]
            inds = line_list[9:len(line_list)]

        else:
            line_list = line.split('\n')[0].split('\t')
            pre_line = line_list[0:9]
            if len(pre_line[4]) > 1:
                continue
            else:
                spec_dict = dict()
                vcf_inds = dict()
                for i, sample in enumerate(inds):
                    geno = line_list[9:len(line_list)]
                    spec_sam = ''.join(pop_dict[sample]) # species/pops
                    if not spec_sam in spec_dict:
                        vcf_inds[spec_sam] = list()
                        vcf_inds[spec_sam].append(sample)
                        spec_dict[spec_sam] = list()
                        spec_dict[spec_sam].append(pre_line)
                        spec_dict[spec_sam].append(geno[i])
                    else:
                        spec_dict[spec_sam].append(geno[i])
                        vcf_inds[spec_sam].append(sample)
                    if i == len(inds)-1:
                        for key, value in spec_dict.iteritems():
                            pre = value[0]
                            pre = '\t'.join(pre)
                            post = '\t'.join(value[1:])
                            full = str(pre + '\t' + post + '\n')
                            file_list[key].write(full)
                            print key, full #key, len(value[1:]), pre, post
                        for key, value in vcf_inds.iteritems():
                            print key, value



                            #print spec_sam, spec_dict[spec_sam], len(spec_dict[spec_sam]) - 1, len(ind_dict[spec_sam]), sample
#                   for key, value in spec_dict.iteritems():
#                       if len(value) == len(ind_dict[spec_sam]):
#                           print key, value, len(value), len(ind_dict[spec_sam])
#                       else:
#                           continue




                break # will only run for the first data line


                        #print spec_sam, spec_dict[spec_sam]
                    #print len(spec_dict[spec_sam])#, len(ind_dict[spec_dict[spec_sam]])
                        #    print 'reached length'
                        #else:
                        #    continue
#                   cleanline = str('\t'.join(spec_dict[spec_sam]) + '\n')
                #print inds, cleanline#len(cleanline), len(spec_dict[spec_sam]) -9 #, cleanline
                    #file_list[spec_sam].write(cleanline)
                #print cleanline#, newline[spec_sam]

    #print spec_sam, spec_dict['stricta'], len(spec_dict['stricta'])


#for key, value in newline.iteritems():
#    print key, value


    #for i, ind in enumerate(inds):    # loop through a list of all pop_dict[ind] (species)
                #print ind, pop_dict[ind], geno[i]
                #continue
#for key, value in newline.iteritems():
#    print key, value




    file.close()

# close all species/pop-specific files
for name in pop_list:
    file_list[name].close()
