#! /bin/bash
# 

for i in *.sam; do
    #file=$(echo $i | cut -f7 -d/)
	id=$(echo $i | cut -f1 -d.)   # keep the path in id  (for output)
    #id=$(echo $id | cut -f7 -d/)
    #RG=\'@RG'\t'ID:${id}\'
    echo $id
    ~/x_app/samtools/samtools view -S -u $i -o ${id}.bam

done


