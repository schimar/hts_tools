#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/mstr/

for i in ~/Desktop/boechera/data/gbs16/ind_fq/*.fastq; do
    file=$(echo $i | cut -f9 -d/)
    id=$(echo $file | cut -f1 -d.)
    #id=$(echo $id | cut -f7 -d/)
    RG=${variable}'@RG:\tID:'${id}
    # we will use a newer version of bwa (v 0.7.12-r1044)
    ~/bwa/bwa aln -t 14 -l 20 -k 2 -q 10 -Y -n 5 /home/mschilling/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa $i -f ${id}.sai
    #bwa samse -n 1 -r "'$RG'" /home/mschilling/Desktop/gbs15/ref/lasio_contigs.fasta ${id}.sai -f ${id}.sam    
    echo $id

done

