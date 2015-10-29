#File to be run from within python that does all of the BEDTools/Shell stuff

wget http://hyphaltip.github.io/GEN220_2015/data/rice_chr6_3kSNPs_filt.bed.gz
wget http://hyphaltip.github.io/GEN220_2015/data/Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz

#because zgrep can't search on columns, unzip the file and use awk to search for just genes or cRNA genes

gzip -dc Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz | awk '$3=="gene"' >Osativa_genes.gff3

module load bedtools
bedtools intersect -b Osativa_genes.gff3 -a rice_chr6_3kSNPs_filt.bed.gz -wb |cut -f7,8,12| sort | uniq -c >> PreSNPs


