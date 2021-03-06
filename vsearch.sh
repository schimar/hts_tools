#! /bin/bash
# 

# NOTE: this script reads through the current working directory and for every *.fasta file, calls vsearch with the id and a supplied name (centroids/sub_centroids)
# Usage: 


idval=$1
idval100=$(echo $idval | cut -f2 -d.)
outname=$2

for i in *.fasta; do
    id=$(echo $i | cut -f1 -d.)
    #echo $i
    vsearch --cluster_fast $i --id $idval --iddef 2 --threads 8 --centroids $outname/$outname$idval100_$i > $outname/rInfos/runInfo$idval100$id.txt 
done

#echo /$idval100/centroids$idval100$i
