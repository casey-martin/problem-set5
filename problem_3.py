from Bio import SeqIO
from collections import Counter

myfile = '/home/dalgarno/Documents/GAW/data-sets/fastq/SP1.fq'

myfastq = SeqIO.parse(open(myfile), 'fastq')

fiveprime = []
threeprime = []

for entry in myfastq:
    fiveprime.append(str(entry.seq[0:6]))
    threeprime.append(str(entry.seq[-6:]))

fiveprime = (Counter(fiveprime))
maxfiveprime = (max(fiveprime.keys(), key=(lambda key: fiveprime[key])))

threeprime = (Counter(threeprime))
maxthreeprime = (max(threeprime.keys(), key=(lambda key: threeprime[key])))


print("5':", maxfiveprime, "3':", maxthreeprime)
