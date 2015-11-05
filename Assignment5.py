#Problem 1
import sys
import csv
import itertools

#get and create files for analysis
outfile = open('Q1_Results.txt', 'w')
filename1 = "Ecoli-vs-Senterica.BLASTP.tab"
filename2 = "Ecoli-vs-Yersinia.BLASTP.tab"

#Create all the dictionaries at once
bestsalmonella = {}
bestyersinia = {}
ecolihits = {}
allsalmonella = {}
allyersinia = {}

#go through and create dictionary entries for the best hit for each species
with open(filename1, 'rb') as salmonella:
	for hit in reversed(list(csv.reader(salmonella, delimiter='\t'))):
		bestsalmonella[hit[0]] = hit[1]

with open(filename2, 'rb') as yersinia:
	for hit in reversed(list(csv.reader(yersinia, delimiter='\t'))):
		bestyersinia[hit[0]] = hit[1]

#get a list of every coli hit from both lists
ecolihits = bestsalmonella.copy()
ecolihits.update(bestyersinia)

#output the data
print >>outfile, "EcoliID" + '\t' "YersiniaHit" + '\t' + "SalmonellaHit"
for k,v in ecolihits.iteritems():
	print >> outfile, k + '\t' + str(bestyersinia.get(k)) + '\t' + str(bestsalmonella.get(k))

#get a list of the hits with greater than 40% identity
with open(filename1, 'rb') as salmonella:
	for hit in filter(lambda p: float(p[2])>40, csv.reader(salmonella, delimiter='\t')):
		allsalmonella[hit[0]] = hit[2]

with open(filename2, 'rb') as yersinia:
	for hit in filter(lambda p: float(p[2])>40, csv.reader(yersinia, delimiter='\t')):
		allyersinia[hit[0]] = hit[2]

#output the data
print >> outfile, str(len(allsalmonella)) + " proteins in Ecoli had a salmonella hit"
print >> outfile, str(len(allyersinia)) + " proteins in Ecoli had a yersinia hit"

outfile.close()


##Question 2
import sys
from Bio import SeqIO
from Bio.Seq import Seq

filename = "Ixodes-scapularis-Wikel_TRANSCRIPTS_IscaW1.4.fa"
outfile = open('Q2_Results.txt', 'w')

seqnum = 0
seqlength = 0
atgnum = 0
GC = 0
seqlens = []

for seq_record in SeqIO.parse(filename, "fasta"):
	seqnum += 1
	seqlength += len(seq_record)
	seqlens.append(len(seq_record))
	if seq_record.seq[0:3]=='ATG':
		atgnum += 1
	for base in seq_record.seq:
		if (base == "G") or (base == "C"):
			GC += 1

print >> outfile, "Max length is " + str(max(seqlens)) + "."
print >> outfile, "Min length is " + str(min(seqlens)) + "."
print >> outfile, "Average length is " + str(seqlength/seqnum) + "."
print >> outfile, str(atgnum) + " transcripts begin with ATG."
print >> outfile, "The GC content of the sequences is " + str(round((GC+.0)/seqlength*100,2)) + "%."

outfile.close()
