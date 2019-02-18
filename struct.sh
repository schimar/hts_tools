#! /bin/bash
# cd /home/mschilling/Desktop/gbs15/mstr/
# ~/Desktop/boechera/msatsSNV/puReSt/msats

cd /home/mschilling/x_app/console/

for i in {2..16}; do
	echo $i
	./structure -i ~/Desktop/boechera/msatsSNV/puReSt/msats/msats_prs_diploids_BF19dpldzd_numIND.csv -K $i -o ~/Desktop/boechera/msatsSNV/puReSt/msats/structure/k${i}_out_c1 -m ~/Desktop/boechera/msatsSNV/puReSt/msats/structure/mainparams -e ~/Desktop/boechera/msatsSNV/puReSt/msats/structure/extraparams

	


done

