#!/usr/bin/perl
#
# This scripts conversts a vcf file to a simpler format for downstream analysis. I am calling this format genetoype likelihood (gl). The first line lists: the number of individuals and loci. The next line has individual ids. This if followed by on line per SNP that gives the SNP id (scaffold, position) and the phred-scaled genotype likelihoods, three per individual. This version only prints a sub-set of loci with maf > $maf. 
#
# 16vi14, this script now prints the non-reference allele frequency for the retained loci to a file so that they can be used to estimate genotypes
#
# 20vii14, this now combines data from multiple files
#
# USAGE: perl vcf2mpgl.pl maf *.vcf
#

my @line = ();
my $word;
my $nind = 0;
my $nloc = 0;
my $first = 1; ## first vcf file, get ids from here
my $out = "sub_filtered2x_combinedDip.gl";

open (OUT, "> $out") or die "Could not write the outfile\n";

if ($out =~ s/gl/txt/){
	open (OUT2, "> af_$out") or die "Count not write the alt. af file\n";
}

open (OUT3, "> depth_$out") or die "failed to write depth file\n";

my $maf = shift (@ARGV);

foreach my $in (@ARGV){
	open (IN, $in) or die "Could not read the vcf file\n";
	while (<IN>){
		chomp;
		## get individual ids
		if (m/^#CHROM/ & ($first == 1)){
			@line = split(m/\s+/, $_);	
			foreach $word (@line){
				if ($word =~ m/[A-Z]+_[A-Z0-9]+_[DTN]/){
					push (@inds, $word);
					$nind++;
				}
			}
			print OUT "$nind $nloc\n";
			$word = join (" ", @inds);
			print OUT "$word\n";
		}
		## read genetic data lines, write gl
		elsif ((m/^Potrs(\d+)\s+(\d+)/) && (!m/[AGCT],[AGCT]/)){
			$word = "$1".":"."$2";
			if (m/AF=([0-9\.e]+);/){
				$palt = $1;
				if ($palt > 0.5){
					$p = 1 - $palt;
				}
				else {
					$p = $palt;
				}
				if ($p >= $maf){ ## keep this locus
					print OUT "$word";
					@line = split(m/\s+/, $_);
					$i = 0;
					@depth = ();
					foreach $word (@line){
						if ($word =~ s/^\d\/\d\:\d+,\d+\:(\d+)\:\d+\://){
							push(@depth,$1);
							$word =~ s/,/ /g;
							print OUT " $word";
						}
						elsif ($word =~ m/\.\/\./){
							push(@depth,0);
							print OUT " 0 0 0";
						}
				
					}
					print OUT "\n";
					print OUT2 "$palt\n"; ## print p before converting to maf
					$depth = join(" ",@depth);
					print OUT3 "$depth\n";
					$nloc++;
				}
			}
		}
		
	}
}
close (OUT);
close (OUT2);
close (OUT3);
print "Number of loci: $nloc; number of individuals $nind\n";
