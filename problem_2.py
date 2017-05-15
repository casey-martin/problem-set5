from Bio import SeqIO

myfile = '/home/dalgarno/Documents/GAW/data-sets/fastq/SP1.fq'

myfastq = SeqIO.parse(open(myfile), 'fastq')

c_count = 0

for entry in myfastq:
    for nt in entry.seq:
        if nt == "C":
            c_count += 1

print(c_count)
