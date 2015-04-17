#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/scripts_zg/ind/

for i in *.sorted.bam; do
    #file=$(echo $i | cut -f7 -d/)
    id=$(echo $i | cut -f1 -d.)
    id=$(echo $id | cut -f7 -d/)
    #RG=\'@RG'\t'ID:${id}\'
    echo $id
    samtools depth $i > ${id}_depth
    cut -f3 ${id}_depth | sort | uniq -c > ${id}_uniq_depth


done


