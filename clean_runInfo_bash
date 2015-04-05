#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/scripts_zg/ind/

for i in runInfo*; do
    id=$(echo $i | cut -f2 -do)
    #echo $id
    ./clean_runInfo.py $i vsearch_ri_$id 
done  

# and then delete all runInfo* files, no longer needed
