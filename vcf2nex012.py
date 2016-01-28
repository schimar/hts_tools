#!/usr/bin/python

# This script reads through a enotype likelihood file and the respective mean genotype likelihood file. It writes a nexus file for all individuals and the given genotypesi, with '0' for ref homozygote, '1' for heterozygote, and '2' for alt homozygote.

# Usage: ~/vcf2nex012.py pubRetStriUG_unlnkd.gl pntest_pubRetStriUG_unlnkd.txt


from sys import argv



# read genotype likelihood file to get scaffold:bp (which is not in the same order as the vcf file, resulting from vcf2gl.py)
with open(argv[1], 'rb') as gl_file:
    scafPos_gl = list()
    for line in gl_file:
        if line.split(' ')[0] == '65':
            continue
        elif line.split(' ')[0] == 'CR1043':
            ind_id = line.split(' ')
            ind_id[len(ind_id)-1] = ind_id[len(ind_id)-1].split('\n')[0]
        else:
            scafPos_gl.append(line.split(' ')[0])


# read the file with mean genotypes
with open(argv[2], 'rb') as mean_gt_file:
    ind_dict = dict()
    for line in mean_gt_file:
        gt_line = line.split(' ')
        for i, ind in enumerate(ind_id):
            if not ind in ind_dict:
                gt_line[i]
                ind_dict[ind] = [float(gt_line[i])]
            else:
                ind_dict[ind].append(float(gt_line[i]))


# parse the mean genotypes and write the proper bases
for key, value in ind_dict.iteritems():
    newline = list()
    for i, pos in enumerate(scafPos_gl):
        if round(float(value[i])) == 0:
            newline.append(str(0))
        elif round(float(value[i])) == 1:
            newline.append(str(1))
        elif round(float(value[i])) == 2:
            newline.append(str(2))
        else:
            continue
    print str(key + '\t' + ''.join(newline))



#print scafPos_gl

#for key, value in iter(refp_dict.iteritems()):
#    print key, ''.join(value)





