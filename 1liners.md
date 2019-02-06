

### fastq/a 

Find out if you have some unusually abundant sequences 
(this gives a ranked list of the most abundant sequences from among the first 25,000 sequences (remember 4 lines per sequence in a fastq))

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | sort | uniq -c | sort -n -r | head```



It can be easy to fool this algorithm, especially if your sequences are long and have higher error rate at the end, in which case you can adjust the uniq command to, say, the first 30 bp:

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | sort | uniq -c -w 30 | sort -n -r | head```

If you are expecting a constant motif somewhere in all your data, it's a good idea to see if it's there. Just add an awk to sniff out where the CR should be (bp 12 to 22 in this example):

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | awk '{print substr($1,12,10)}' | sort | uniq -c | sort -n -r | head```


Take two fastq files and turn them into a paired fasta file - drop the quality info and put each read pair one after the other:

```paste $read1s1 $read2s1  | awk 'BEGIN {c=0} {c++; if (tag!="") {print tag "\n" $1 "\n" tag "\n" $2; tag=""} if (substr($1,1,4)=="@HWI") {tag=$1}}' \
| sed s/'^@HWI'/'>HWI'/  > $output.paired_s1.fasta 2> $output.log &```

If you'd like to filter only on read pairs with quality values no smaller than 10, it's a bit more work:

```
paste $read1s1 $read2s1  | \
awk 'BEGIN {c=0} {c++; if (c==4) {print $1 "\t" $2 "\t" seq1 "\t" seq2 "\t" tag; c=0} if (c==2) {seq1=$1; seq2=$2;} if (c==1) {tag=$1}}' \
| awk 'BEGIN \
  { convert="!\"#$%&\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"; \
    convert=convert "ABCDEFGHIJKLMNOPQRSTUVWXYZ" } \
  { badQual=0; \
     for (i=1;i<=length($1);i++) {if (index(convert, substr($1,i,1))-1<10) {badQual=1} }; \
     for (i=1;i<=length($2);i++) {if (index(convert, substr($2,i,1))-1<10) {badQual=1} }; \
  if (badQual!=1) { print $5 "\n" $3 "\n" $5 "\n" $4 }  }'
| sed s/'^@HWI'/'>HWI'/  > $output.paired_s1.fasta 2> $output.log &
```

(Note that you could have combined the two awk commands - I don't like to do that because it's harder for me to see what I'm doing, and harder for me to copy it for the next problem I need to solve.)


### sam/bam 

bam &rarr; sam 
```samtools view <infile.bam> > outfile.sam```


sam &rarr; bam 
```samtools view -S -b <infile.sam> > outfile.bam ```

change the headers in sam file:
```
cat notrrna.genome.sam | awk 'BEGIN {FS="\t"; OFS="\t"} \
   {if ($3=="mitochondria") {$3="ChrM"} if ($3=="chloroplast") {$3="ChrC"} \
   if ($3=="2") {$3="Chr2"} if ($3=="1") {$3="Chr1"}  if ($3=="3") {$3="Chr3"}  \
   if ($3=="4") {$3="Chr4"}  if ($3=="5") {$3="Chr5"}  \
   print}' > notrrna.genome.tair.sam
```

or with samtools reheader:
```
samtools view -h notrrna.genome.bam | sed s/'mitochondria'/'ChrM'/g | samtools view -S -b - > blah.bam
```










