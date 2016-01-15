#!/usr/bin/python

# VCP2phy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# VCP2phy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with VCP2phy. If not, see <http://www.gnu.org/licenses/>.

from sys import argv

def Ambiguifier(bases):
	"""Take a list or tuple of bases and return the corresonding ambiguity."""
	bases = list(bases)
	ambigs = {"AA": "A", "CC": "C", "TT": "T", "GG": "G", "AC": "M", "AG": "R",
	"AT": "W", "CG": "S", "CT": "Y", "GT": "K", "ACG": "V",
	"ACT": "H", "AGT": "D", "CGT": "B", "ACGT": "N",
	"..": "N"}
	bases.sort()
	return ambigs["".join(bases)]

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



with open(argv[3], 'rb') as gl_file:
    scafPos_gl = list()
    for line in gl_file:
        if line.split(' ')[0] == '79' or line.split(' ')[0] == 'CR1043':
            continue
        else:
            scafPos_gl.append(line.split(' ')[0])


with open(argv[2], 'rb') as mean_gt_file:
    ind_dict = dict()
    for line in mean_gt_file:
        gt_line = line.split(' ')
        for i, ind in enumerate(ind_id):
            if not ind in ind_dict:
                gt_line[i]
                ind_dict[ind] = [gt_line[i]]
            else:
                ind_dict[ind].append(gt_line[i])
        for gl_pos in scafPos_gl:
            print refp_dict[gl_pos]


#print scafPos_gl

#for key, value in iter(refp_dict.iteritems()):
#    print key, ''.join(value)

#for key, value in iter(ind_dict.iteritems()):
#    for scafPos in scafPos




