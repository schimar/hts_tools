#!/usr/bin/perl

## This script returns a genotype matirx (locus by ind) with genotype
## means (point estimates) from a genotype likelihood file; a HW prior is used based on allele frequencies provided in a separate file

## USAGE: perl gl2genest.pl file.gl af_file.txt
use warnings;

$in = shift (@ARGV);
$af = shift (@ARGV);

## read in and store maf's
open (IN, $af) or die "read failed: $af\n";
while (<IN>){
	chomp;
	push (@af,$_);
}
close (IN);

$nacnt = 0;
$goodcnt = 0;
## read through gl file and estimate genotypes
open (IN, $in) or die "read failed: $in\n";
$out = $in;
$out =~ s/gl$/txt/;
open (OUT, "> pntest_$out") or die;
while (<IN>){
    chomp;
    if (s/^\d+:\d+\s+//){ ## this line has genotype data, get rid of locus id
	$p = shift(@af); ## get alt. af. for this locus
        $prior[0] = (1-$p) ** 3; ## calculate prior probs as q^2, 2pq, p^2
        $prior[1] = 3 * $p * (1-$p) ** 2;
        $prior[2] = 3 * $p ** 2 * (1-$p);
        $prior[3] = $p ** 3;
	@line = split(" ",$_);
	@gest = ();
	while (@line){
	    $sum = 0;
	    for $i (0..3){ ## three genotyple likelihoods for each individual
		$gl[$i] = shift(@line);
		$gl[$i] = (10 ** ($gl[$i]/-10)) * $prior[$i];
		$sum += $gl[$i];
	    }
	    $gest = 0;
	    $maxgprob = 0;
	    for $i (0..3){ ## normalize, and calculate mean genotype
		$gl[$i] = $gl[$i]/$sum;
		if($gl[$i] >= $maxgprob){
			$maxgprob = $gl[$i];
		}
		$gest += $i * $gl[$i];
	    }
	    if($maxgprob >= 0.9){
	    	$gest = sprintf("%.5f",$gest);
                $goodcnt++;
	    }
            else{
		$gest = 'NA';
                $nacnt++;
            }
	    push(@gest, $gest);
	}
	$gest = join(" ",@gest);
	print OUT "$gest\n";
    }
    else {
	print "failed to match $_\n";
    }
}
close (IN);
close (OUT);
print "$goodcnt high prob. genotypes; $nacnt genotypes converted to NA\n";
