import itertools
import gzip
import sys
import re
import os
ofile = open('Results.txt', 'w') #an output file

print >> ofile, "Question 1", "\n"

# based on post here
# https://drj11.wordpress.com/2010/02/22/python-getting-fasta-with-itertools-groupby/

# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

# this function reads in fasta file and returns pairs of data
# where the first item is the ID and the second is the sequence
# it isn't that efficient as it reads it all into memory
# but this is good enough for our project
def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = group.next()
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence
        
# here is my program

filename = 'Ecoli_K-12.fasta'


if re.match('(\S+)\.gz$',filename):
    with gzip.open(filename,"rb") as f:
        seqs = dict(aspairs(f))        
else:
    with open(filename,"r") as f:
        seqs = dict(aspairs(f))        

#n=0
#This is some super-verbose code that I don't need
#for k,v in seqs.iteritems():
#    print "id is ",k,"seq is",v
#    n += 1
#print n,"sequences"

#Input the Restriction Enzymes, their readable cut sites, and their RE cut sites
Enzymes = ["EcoRI", "Bsu15I", "Bsu36I", "BsuRI", "EcoRII"]
EnzPat = ["GAATTC", "ATCGAT", "CCTNAAG", "GGCC", "CCWGG"]
EnzRE = ['GAATTC', 'ATCGAT', 'CCT[ATGC]AAG', 'GGCC', 'CC[AT]GG']
Number = []

#iterate through each enzyme, count its cut sites and print the report
for k,v in seqs.iteritems():
	for i in range(0, len(Enzymes)):
		Number.append(len(re.findall(EnzRE[i], v)))
		print >> ofile, "Number of", Enzymes[i], "(", EnzPat[i], ") cut sites:", Number[i]

print >> ofile, "\n", "Question 2", "\n"

##Tackle the Yeast problem

filename = 'orf_trans_all.fasta.gz'

#open the file and define the units
if re.match('(\S+)\.gz$',filename):
    with gzip.open(filename,"rb") as f:
        seqs = dict(aspairs(f))        
else:
    with open(filename,"r") as f:
        seqs = dict(aspairs(f))        

#Define an NLS schematic
NLS = '[R,K]..L.{1,25}[V,Y]..[V,I].[K,R].[K,R]'
pattern = re.compile(NLS)

#Find the sequences which contain this NLS and report them
count = 0
hasNLS = []
noNLS = []
for k,v in seqs.iteritems():
	if re.findall(pattern, v):
		print >> ofile, k, "has the following NLS:", re.findall(pattern,v)
		hasNLS.append(k)
		count += 1
	else:
		noNLS.append(k)

print "The total number of proteins with an NLS is", count


#Tackle the poly-A tail problem
print >> ofile, "\n", "For Question 3 see file called Q3_Results"

#Read in the files and parse the data into pairs
filename = 'Scer_Trinity.fasta'

if re.match('(\S+)\.gz$',filename):
    with gzip.open(filename,"rb") as f:
        seqs = dict(aspairs(f))        
else:
    with open(filename,"r") as f:
        seqs = dict(aspairs(f)) 

#Define a poly-A tail schematic
polyA =re.compile('AA[A,T]AAA')

#create dictionaries for the length and position of the polyA tails

polypos = {} #beginning position of the motif
totlen = {} #total length of the contig
polylen = {} #length of the polyA tail after the motif
ofile.close()
datafile = open('Data.txt', 'w')

#Go line by line and get what we need
for line in seqs:
	m = polyA.search(seqs[line])
	while m:
		totlen[line] = len(seqs[line])
		polypos[line] = m.start()
		m = polyA.search(seqs[line], m.end()+1)
		polylen[line] = totlen[line] - (polypos[line]+7)

for k,v in polylen.iteritems():
	print >> datafile, k, '\t', v

datafile.close()

os.system("R --no-save < Histogram.R")


