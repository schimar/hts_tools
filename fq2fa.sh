
#! /bin/bash

# convert fastq to fasta for all files in the working directory 
# USAGE: ./fq2fa.sh

getArray() {
    array=() # Create array
    while IFS= read -r line # Read a line
    do
        array+=("$line") # Append line to the array
    done < "$1"
}


for i in *.fastq; do
	id=$(echo $i | cut -f1 -d.)
	echo $id
	sed -n '1~4s/^@/>/p;2~4p' $i > $id.fasta
done

