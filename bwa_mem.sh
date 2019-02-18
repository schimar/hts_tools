#! /bin/bash
# cd ~/Desktop/boechera/lasio/

for i in *.fastq; do
    file=$(echo $i | cut -f9 -d/)
    id=$(echo $file | cut -f1 -d.)
    #id=$(echo $id | cut -f7 -d/)
    RG=${variable}'@RG:\tID:'${id}
    # we will use a newer version of bwa (v 0.7.12-r1044)
	echo $id

    #~/bwa/bwa mem -t 10 -w 50 -k 20 -a -C -R "@RG\tID:$id\tLB:$id\tSM:$id\tPL:ILLUMINA" ~/Desktop/stricta/stricta_assembly/v1.2/assembly/Bstricta_278_v1.fa $i > bwaMEMout/${id}.sam
	#~/bwa/bwa mem -t 10 -w 50 -k 20 -a -C -R "@RG\tID:$id\tLB:$id\tSM:$id\tPL:ILLUMINA" l105_88strictaMEM2Cns76_5.fasta $i > out/AllRds/${id}.sam
	~/bwa/bwa mem -t 10 -w 50 -k 20 -a -C -R "@RG\tID:$id\tLB:$id\tSM:$id\tPL:ILLUMINA" l105_88strictaMEM2Cons76_5hdr_clnd.fasta $i > ${id}.sam

done

