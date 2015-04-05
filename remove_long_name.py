#! /usr/bin/python

# remove_long_name.py
# Checks fasta file for the long name in the lines starting with ">" (i.e. > read_short_name read_long name) and deletes the long name. Some tools (such as bwa) do not like the long name having white spaces, which will lead to a messed up sam file. 

# Usage: ./remove_long_name.py <input-file_name.fa> <new_file_name.fa>


import sys
import shutil
import tempfile


with open(sys.argv[1], 'rb') as file:
	newfile = tempfile.NamedTemporaryFile(delete=False)
	for line in file:
		if line[0] == ">":
			new = str(line.split()[0] + "\n")
			line = line.replace(line, new)
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



