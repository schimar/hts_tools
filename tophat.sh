#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/mstr/

for i in *.fastq; do
    id=$(echo $i | cut -f1 -d.)
    echo $id
    tophat -p 4 -N 3 -o /home/mschilling/Desktop/gbs15/mstr/tophat_out/ Bstricta $i
    
done

