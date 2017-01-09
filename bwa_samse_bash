#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/mstr/bwa_out/

for i in ~/Desktop/boechera/data/gbs16/ind_fq/bwa_out/*.sai; do
    file=$(echo $i | cut -f10 -d/)
    id=$(echo $file | cut -f1 -d.)
    #RG=\'@RG'\t'ID:${id}\'
    echo $id
    ~/bwa/bwa samse -n 1 -r "@RG\tID:$id\tLB:$id\tSM:$id\tPL:ILLUMINA" ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa $file ~/Desktop/boechera/data/gbs16/ind_fq/${id}.fastq -f ${id}.sam  
    #echo $file $id  #\'\@RG\\tID:$id\'
done

# \'\@RG\tID:cmac-"."$ind"."\'

#bwa samse -n 1 -f CR1043.sam -r '@RG:\tID:CR1043' /home/mschilling/Desktop/gbs15/ref/lasio_contigs.fasta CR1043.sai CR1043.fastq
