##Preambulatory Stuff to get ready to do the assignment

#Set my directory to the proper area for the class and create a folder for the assignment
cd /Users/rajewski/Dropbox/GEN\ 220/
mkdir Assignment\ 1
cd Assignment\ 1

## 1. Getting data
#actually download the file
curl http://www.gutenberg.org/cache/epub/24923/pg24923.txt > /Users/rajewski/Dropbox/GEN\ 220/Assignment\ 1/variation.txt\

#figure out the size of the file in a human-readable format
du -h variation.txt > Assignment\ 1\ Results.txt

## 2. Compressing and Uncompressing
#compress the file with gzip and find its size
gzip variation.txt
du -h variation.txt.gz >> Assignment\ 1\ Results.txt
gunzip variation.txt.gz

#recompress with bzip2, find its size, then uncompress
bzip2 variation.txt
du -h variation.txt.bz2  >> Assignment\ 1\ Results.txt
bunzip2 variation.txt.bz2

## 3. Counting
#get the number of words in the Darwin file
wc -w variation.txt >> Assignment\ 1\ Results.txt

#remove the file that were done with
rm variation.txt

#get the new data file
curl http://hyphaltip.github.io/GEN220_2015/data/Nc20H.expr.tab > data_file

#count the number of lines
wc -l data_file >> Assignment\ 1\ Results.txt

## 4. Sorting
#sort based on FPKM to a new file
sort -n -k6,6 -o Nc20H.expr.sorted.tab data_file
rm data_file

#get new rice file
curl http://hyphaltip.github.io/GEN220_2015/data/rice_chr6.gff.gz > rice.gff.gz

#count the number of exon features
zgrep -c 'exon\t' rice.gff.gz >> Assignment\ 1\ Results.txt
rm rice.gff.gz

## 5. Finding and Counting
#get the genbank file
curl http://hyphaltip.github.io/GEN220_2015/data/D_mel.63B12.gbk > genbank

#this counting is sort of a kludge and I apologize for that in advance
grep -c 'CDS            ' genbank >>Assignment\ 1\ Results.txt
rm genbank

## 6. Column Combining
# get the files
curl http://hyphaltip.github.io/GEN220_2015/data/Nc20H.expr.tab > Nc20H
curl http://hyphaltip.github.io/GEN220_2015/data/Nc3H.expr.tab > Nc3H

#verify their rows
sort -k1,1 -r Nc20H | uniq -c | head -n 3 >> Assignment\ 1\ Results.txt
sort -k1,1 -r Nc3H |uniq -c | head -n 3 >> Assignment\ 1\ Results.txt

#cut and paste the data into a new file
sort -k1,1 -r Nc20H | cut -f-6 > col1to6
sort -k1,1 -r Nc3H |cut -f6 > col6
paste col1to6 col6 > Combined_Data.txt

rm col1to6
rm col6
rm Nc20H
rm Nc3H

