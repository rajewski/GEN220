#This file will be written as a script to be submitted to the cluster as a job.
#It will not contain information about how to log onto the cluster to perform
#the actual analysis


### Question 1

#get the files themselves
wget http://hyphaltip.github.io/GEN220_2015/data/rice_chr6_3kSNPs_filt.bed.gz
wget http://hyphaltip.github.io/GEN220_2015/data/Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz

#because zgrep can't search on columns, unzip the file and use awk to search for just genes or cRNA genes

gzip -dc Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz | awk '$3=="gene"' >Osativa_genes.gff3
gzip -dc Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz | awk '$3=="ncRNA_gene"' >Osativa_ncrnagenes.gff3

#load bedtools so that we can do the intersect later
module load bedtools

#Get the number of genes with SNPs
echo 'The number of protein coding genes with SNPs is:' > Results.txt
bedtools intersect -a Osativa_genes.gff3 -b rice_chr6_3kSNPs_filt.bed.gz |cut -f9| sort | uniq| wc -l >>Results.txt
echo 'The number of ncRNA genes with SNPs is:' >> Results.txt
bedtools intersect -a Osativa_ncrnagenes.gff3 -b rice_chr6_3kSNPs_filt.bed.gz |cut -f9| sort | uniq| wc -l >> Results.txt



####Question 2
#create a list of CDS features
gzip -dc Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz | awk '$3=="CDS"' > Osativa_CDS.gff3

#get a list of SNPs that are in these CDS features and count them
echo 'This number of SNPs in CDS features is:' >> Results.txt
bedtools intersect -a rice_chr6_3kSNPs_filt.bed.gz -b Osativa_CDS.gff3 | uniq | wc -l >> Results.txt

