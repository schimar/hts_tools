#!/usr/bin/python

# This script reads through a vcf, its corresponding genotype likelihood file, and the respective mean genotype likelihood file.
# It writes a nexus file for all individuals and the given genotypes. Currently, for heterozygotes, it prints the alternative allele (I'd like to include the "ambiguified" version eventually).

# Usage: ~/vcf2phy.py fltrd_pubRetStri_dipUG35_unlnkd.vcf pntest_pubRetStriUG_unlnkd.txt pubRetStriUG_unlnkd.gl #ambig=T


from sys import argv


#

#ambiUse = argv[4].split('=')[1] # 'ambig=T' for use of ambiguity code when heterozygous; F otherwise


def Ambiguifier(bases):
	"""Take a list or tuple of bases and return the corresonding ambiguity."""
	bases = list(bases)
	ambigs = {"AA": "A", "CC": "C", "TT": "T", "GG": "G", "AC": "M", "AG": "R",
	"AT": "W", "CG": "S", "CT": "Y", "GT": "K", "ACG": "V",
	"ACT": "H", "AGT": "D", "CGT": "B", "ACGT": "N",
	"..": "N"}
	bases.sort()
	return ambigs["".join(bases)]

# read vcf file to get ref and alt alleles
refp_dict = dict()
with open(argv[1], 'rb') as vcf_file:
    for line in vcf_file:
        if line[0:2] == '##':
            continue
        elif line[0:2] == '#C':
            ind_id = line.split('\t')[9:]
        else:
            scafPos = list()
            line_list = line.split('\t')
            scafPos.append(line_list[0].split('d')[1])
            scafPos.append(line_list[1])
            scafPos = ':'.join(scafPos)
            ref = line_list[3]
            alt = line_list[4]
            if len(alt.split(',')) > 1:
                ambiguous = line_list[4].split(',')
                ambiguous = ''.join(ambiguous)
                refp_dict[scafPos] = ref, Ambiguifier(ambiguous)
            else:
                refp_dict[scafPos] = ref, alt
    vcf_file.close()


# read genotype likelihood file to get scaffold:bp (which is not in the same order as the vcf file, resulting from vcf2gl.py)
with open(argv[3], 'rb') as gl_file:
    scafPos_gl = list()
    for line in gl_file:
        if line.split(' ')[0] == '79' or line.split(' ')[0] == 'CR1043':
            continue
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
        #print i, pos, refp_dict[pos], value[i]
        if round(float(value[i])) == 0.0:
            newline.append(refp_dict[pos][0])
            #print value[i], refp_dict[pos], refp_dict[pos][0]
        #    print key, value[i]
        elif round(float(value[i])) == 1.0:
            # ambiguity codes!!
            newline.append(refp_dict[pos][1])
            #print key, value[i]
            #print value[i], refp_dict[pos], refp_dict[pos][1]
        elif round(float(value[i])) == 2.0:
            newline.append(refp_dict[pos][1])
            #print value[i], refp_dict[pos], refp_dict[pos][1]
        #    print key, value[i]
        else:
            continue
    print str(key + '\t' + ''.join(newline))



#print scafPos_gl

#for key, value in iter(refp_dict.iteritems()):
#    print key, ''.join(value)





