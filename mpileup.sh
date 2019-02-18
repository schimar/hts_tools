#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/scripts_zg/ind/

for i in *.sorted.bam; do
    #file=$(echo $i | cut -f7 -d/)
    id=$(echo $i | cut -f1 -d.)
    id=$(echo $id | cut -f7 -d/)
    #RG=\'@RG'\t'ID:${id}\'
    echo $id
    samtools mpileup -u -E -D -C 50 -g -I -q 10 -Q 15 -f /home/mschilling/Desktop/gbs15/ref/lasio_contigs.fasta  $i > ${id}_variants.bcf

done
