#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/mstr/

for i in *.fastq; do
    id=$(echo $i | cut -f1 -d.)
    seqtk seq -a $i > $id.fasta
done

