
#! /bin/bash

# convert fastq to fasta for all files in the working directory 
# USAGE: ./fq2fa.sh

for i in *.fastq; do
	id=$(echo $i | cut -f1 -d.)
	echo $id
	sed -n '1~4s/^@/>/p;2~4p' $i > $id.fasta
done

