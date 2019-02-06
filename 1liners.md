
(see also [this great ressource](https://github.com/stephenturner/oneliners) for some cool awk, sed and other wizardry)


## **fastq/a** 

basic sequence stats. Print total number of reads, total number unique reads, percentage of unique reads, most abundant sequence, its frequency, and percentage of total in file.fq:
```
cat myfile.fq | awk '((NR-2)%4==0){read=$1;total++;count[read]++}END{for(read in count){if(!max||count[read]>max) {max=count[read];maxRead=read};if(count[read]==1){unique++}};print total,unique,unique*100/total,maxRead,count[maxRead],count[maxRead]*100/total}'
```

split a multi-FASTA file into individual FASTA files:
```
awk '/^>/{s=++d".fa"} {print > s}' multi.fa
```

Output sequence name and its length for every sequence within a fasta file:
```
cat file.fa | awk '$0 ~ ">" {print c; c=0;printf substr($0,2,100) "\t"; } $0 !~ ">" {c+=length($0);} END { print c; }'
```

**fastq** &rarr; **fasta**
```
sed -n '1~4s/^@/>/p;2~4p' file.fq > file.fa
```

Calculate the mean length of reads in a fastq file:
```
awk 'NR%4==2{sum+=length($0)}END{print sum/(NR/4)}' input.fastq
```


extract specific reads from fastq file according to reads name :
```
zcat a.fastq.gz | awk 'BEGIN{RS="@";FS="\n"}; $1~/readsName/{print $2; exit}'
```


Find out if you have some unusually abundant sequences 
(this gives a ranked list of the most abundant sequences from among the first 25,000 sequences (remember 4 lines per sequence in a fastq))

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | sort | uniq -c | sort -n -r | head```

It can be easy to fool this algorithm, especially if your sequences are long and have higher error rate at the end, in which case you can adjust the uniq command to, say, the first 30 bp:

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | sort | uniq -c -w 30 | sort -n -r | head```

If you are expecting a constant motif somewhere in all your data, it's a good idea to see if it's there. Just add an awk to sniff out where the CR should be (bp 12 to 22 in this example):

```head -100000 seqs.fastq | grep -A 1 '^@HWI' | grep -v '^@HWI' | awk '{print substr($1,12,10)}' | sort | uniq -c | sort -n -r | head```


Take two fastq files and turn them into a paired fasta file - drop the quality info and put each read pair one after the other:

```
paste $read1s1 $read2s1  | awk 'BEGIN {c=0} {c++; if (tag!="") {print tag "\n" $1 "\n" tag "\n" $2; tag=""} if (substr($1,1,4)=="@HWI") {tag=$1}}' \
| sed s/'^@HWI'/'>HWI'/  > $output.paired_s1.fasta 2> $output.log &
```


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

take matching paired-end reads:
```
sort Sample_1-line_R1.fq > Sample_1-line_sorted_R1.tab
sort Sample_1-line_R2.fq > Sample_1-line_sorted_R2.tab
join Sample_1-line_sorted_R1.tab Sample_1-line_sorted_R2.tab > Sample_1-line_joined.tab
```

write joined one-line fastq info to two fastq files:
```
gawk '{printf($1"\n"$2"\n"$3"\n"$4"\n") >> "Sample_matched_R1.fq"; printf($1"\n"$5"\n"$6"\n"$7"\n") >> "Sample_matched_R2.fq"}' Sample_1-line_joined.tab
```
take matching paired-end reads:
```
sort Sample_1-line_R1.fq > Sample_1-line_sorted_R1.tab
sort Sample_1-line_R2.fq > Sample_1-line_sorted_R2.tab
join Sample_1-line_sorted_R1.tab Sample_1-line_sorted_R2.tab > Sample_1-line_joined.tab
```

write joined one-line fastq info to two fastq files:
```
gawk '{printf($1"\n"$2"\n"$3"\n"$4"\n") >> "Sample_matched_R1.fq"; printf($1"\n"$5"\n"$6"\n"$7"\n") >> "Sample_matched_R2.fq"}' Sample_1-line_joined.tab
```

take a fasta file with a bunch of short scaffolds, e.g., labeled >Scaffold12345, remove them, and write a new fasta without them:
```
samtools faidx genome.fa && grep -v Scaffold genome.fa.fai | cut -f1 | xargs -n1 samtools faidx genome.fa > genome.noscaffolds.fa
```



## **sam/bam** 

**bam** &rarr; **sam** 
```samtools view <infile.bam> > outfile.sam```


**sam** &rarr; **bam** 
```samtools view -S -b <infile.sam> > outfile.bam ```

change headers in sam file:
```
cat notrrna.genome.sam | awk 'BEGIN {FS="\t"; OFS="\t"} \
   {if ($3=="mitochondria") {$3="ChrM"} if ($3=="chloroplast") {$3="ChrC"} \
   if ($3=="2") {$3="Chr2"} if ($3=="1") {$3="Chr1"}  if ($3=="3") {$3="Chr3"}  \
   if ($3=="4") {$3="Chr4"}  if ($3=="5") {$3="Chr5"}  \
   print}' > notrrna.genome.tair.sam
```

If you only need to change the name of one reference, I'd use sed and a trick like this to pipe straight from binary to text and back to binary:
```
samtools view -h notrrna.genome.bam | sed s/'mitochondria'/'ChrM'/g | samtools view -S -b - > blah.bam
```
(You can put any combination of grep/sed/awk you like in between the two samtools commands; this might be useful if you have a mixed population. You should map all the data at once to a concatenated reference, but then might want to separate the BAM file into two - one for organism A and one for organism B. You can also use this for things like searching for indels quickly by scanning the CIGAR string, or parsing any of the custom fields that your mapper/genotyper have produced)


**bam** &rarr; **fastq**
```
samtools view input.bam | \
   awk 'BEGIN {FS="\t"} {print "@" $1 "\n" $10 "\n+\n" $11}' > output.bam.fastq
```
(You can also do this with bamtools and picard)
[This seqanswers post](http://seqanswers.com/forums/showthread.php?t=4180) has a great two-liner to add a read group to a BAM file, and contrasts it with a perl program (many more than 2 lines) to do the same thing.



find most abundant sequence start site:
```
cat in.sam | head -100000 | awk '{print $3"_"$4}' | sort | uniq -c | sort -n -r | head
```
(Note that this samples just the first 100,000 mapped sequences - works fine on an unsorted sam file, but doesn't make sense on a sorted bam/sam file. On a sorted file, you have to process the whole file. Even so, doing this command on a few tens of millions of sequences should take only a few minutes)

join mated sequences in a sam/bam file onto one line (and discard the unmated sequences) so you can process them jointly, this method is pretty robust:
```
cat in.sam | awk '{if (and(0x0040,$2)&&!(and(0x0008,$2))&&!(and(0x0004,$2))) {print $1 "\t" $2 "\t" $3"\t"$4}}' > r1
cat in.sam | awk '{if (and(0x0080,$2)&&!(and(0x0008,$2))&&!(and(0x0004,$2))) {print $1 "\t" $2 "\t" $3"\t"$4}}' > r2
paste r1 r2 > paired.out
```
(It uses the SAM file's flag field (field 2) and some bitwise operations to confirm that both the read and it's mate are mapped, puts the separate alignments into separate files, then uses paste to join them. Since mappers like BWA may output a variable number of fields for each read, I've just used the first four fields. You can also do this with a one-line awk command and do more processing within that command if you want to.)

## **vcf**

count all variants in all vcf files:
```
cat *.vcf | grep -v '^#' | wc -l
```

count in at least two vcf files:
```
cat *.vcf | grep -v '^#' | awk '{print $1 "\t" $2 "\t" $5}' | sort | uniq -d | wc -l
```

count in three vcf files
```
cat *.raw.vcf | grep -v '^#' | awk '{print $1 "\t" $2 "\t" $5}' | sort | uniq -c | grep ' 3 ' | wc -l
```

number of indels called in vcf:

```grep -c INDEL *.vcf```

histogram of allele freqs:
```
cat *.vcf | awk 'BEGIN {FS=";"} {for (i=1;i<=NF;i++) {if (index($i,"AF1")!=0) {print $i} }}' | \
awk 'BEGIN {FS="="} {print int($2*10)/10}' | sort | uniq -c | sort -n -r | head
```

**vcf** &rarr; **BED**
```
sed -e 's/chr//' file.vcf | awk '{OFS="\t"; if (!/^#/){print $1,$2-1,$2,$4"/"$5,"+"}}'
```

count missing sample in vcf file per line:

bcftools query -f '[%GT\t]\n' a.bcf |  awk '{miss=0};{for (x=1; x<=NF; x++) if ($x=="./.") {miss+=1}};{print miss}' > nmiss.count



## blast 

Keep only top bit scores in blast hits (5 less than the top):
```
awk '{ if(!x[$1]++) {print $0; bitscore=($14-6)} else { if($14>bitscore) print $0} }' blastout.txt
```













