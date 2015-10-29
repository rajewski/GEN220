# This is Python code
#String Manipulations

#open a results file
ofile = open('Results.txt', 'w')

# dna string
dna = ('ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA'
       'GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC'
       'AGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATG'
       'CTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGC'
       'TCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGAT'
       'CCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCA'
       'CCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCA'
       'CTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACT'
       'GGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC')

print >> ofile, "dna is " + dna


# compute the % of G+C bases in the DNA string (e.g. the GC content)

GC = 0;
length = 0;
for c in dna:
	if (c =="G") or (c == "C"):
			GC +=1

length = len(dna)
GC =round((GC+0.0)/length*100.0,2)


print >> ofile, "GC content for dna string is " + str(GC) + "%";
print >> ofile, "length of string is " + str(length);

# identify the location of all

atg_codons = [];
start = 0
pos=0
while dna.find("ATG",pos+1) >0:
	pos = dna.find("ATG", start)
	atg_codons.append(pos)
	start = pos + 1
	

print >> ofile, "The position of the ATG codons is :";
for codon in atg_codons:
    print >> ofile, "ATG at position " + str(codon);


# print the reverse complement
#my original script didn't reverse the sequence, but I'm correcting it to do so here.
revcom = "";

for n in range(len(dna)-1, -1, -1) 
	print "n is ", n
	base = dna[n]
	if base == "A":
		revcom+="T"
	elif base == "T":
		revcom+="A"
	elif base == "G":
		revcom+="C"
	elif base == "C":
		revcom+="G"
	else:
		print "Bro, this isn't DNA"

# your code here

print >> ofile, "The DNA string is: ";
print >> ofile, dna;
print >> ofile, "The reverse complement of DNA string is: ";
print >> ofile, revcom;

####Math Calculations
import os
os.system("wget http://hyphaltip.github.io/GEN220_2015/data/Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz")
os.system("gunzip Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3.gz")

# this code will open the file for reading. You shouldn't need to change it

gff3 = open("Oryza_sativa.IRGSP-1.0.27.chromosome.6.gff3","r")

# these are some variables you will need to update in the loop below
gene_count = 0;
CDS_count = 0;
num_gene_bases = 0;
num_CDS_bases = 0;
chrom_6_length = 31248787; # hardcode this for now - the length of Chr6

for line in gff3:
	if line.find("#") == 0:
		continue 
	else:
        	row = line.split("\t")
		if row[2] == 'gene':
			gene_count += 1
			num_gene_bases += int(row[4]) - int(row[3])
		if row[2] == 'CDS':
			CDS_count += 1
			num_CDS_bases += int(row[4]) - int(row[3])
		

CDS_fraction = 0; # update this to calc the fraction of the chromosome which is coding bases
CDS_fraction = (num_CDS_bases+0.0) / chrom_6_length

print >> ofile, "There are {} genes" .format(gene_count);
print >> ofile, "There are {} exons" .format(CDS_count);
print >> ofile, "There are {} bases which are in genes out of {}".format(num_gene_bases,chrom_6_length);
print >> ofile, "There are {} bases which are in exons out of {}".format(num_CDS_bases,chrom_6_length);
print >> ofile, "{} % of the Chr6 bases are coding".format(round(100*CDS_fraction,2));

##Compute SNP Frequency
#I'm having a lot of trouble with this one

#run a shell script to do the dirty BEDTools work
import os
import re

os.system("chmod +x ShellAddendum.sh")
os.system("./ShellAddendum.sh")
os.system("cp PreSNPs PreSNPs.txt")

#read the file
snps = open('PreSNPs.txt', 'r')


#Add in a header row
print >> ofile, 'Gene_Name', 'Length', 'SNP', 'SNPs_per_kb'

#go line by line
for line in snps:
	row = re.split(r'[;:\t\s]*', line) #this line is sort of witchcraft to me
	length = float(row[3]) - float(row[2])
	spk = float(row[1])/(length/1000)
	print >> ofile, row[5], repr(length), row[1], repr(spk)

ofile.close()










