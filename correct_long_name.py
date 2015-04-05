#! /usr/bin/python
# correct_long_name.py
# Checks fasta file for the long name in the lines starting with ">" (i.e. > read_short_name read_long name) and replaces whitespaces (if any) in the long name by underscores. Some tools (such as bwa) do not like the long name having white spaces, which will lead to a messed up sam file. The resulting line will consist of the short name and the long name, seperated by a whitespace. The long name, however will be of the following format: long_name_of_gene_function (instead of
# "long name of gene function")

# Usage: ./correct_long_name.py <input-file_name.fa> <new_file_name.fa>


import sys
#import re
import shutil
import tempfile


with open(sys.argv[1], 'rb') as file:
	newfile = tempfile.NamedTemporaryFile(delete=False)
	for line in file:
		if line[0] == ">":
			short = str(line.split()[0])
			long = "_"
			long = long.join(line.split()[1:])
					#line = line.replace(line, new)
			line = str(short + " " + long + "\n")
		newfile.write(line)
	file.close()
	shutil.move(newfile.name, sys.argv[2])
	newfile.close()

# not needed
#with open(sys.argv[1]) as file: # open the fastq file
#    line_count = 0
#	newfile = []
    #header_start = sys.argv[2]
    #header_start_length = len(header_start)
    #next_line = "header"
#    for line in file:
		#print line, line_count
		#line_count += 1
#		if line[0] == ">":
#			newfile.append(line.replace(line, line.split()[0]))
			#print re.findall('(^>\w+\.\w+\.[0-9]+)', line).strip()
#		else: 
#			newfile.append(line)



