import pysam
from collections import Counter

mybam = pysam.AlignmentFile("/home/dalgarno/Documents/GAW/data-sets/bam/myc.hela.chr22.bam", 'rb')

neg = 0
pos = 0
edit_dis = []

for i in mybam:
    edit_dis.append(i.get_tag('NM'))
    if i.flag == 16:
        neg += 1
    if i.flag == 0:
        pos += 1

print('0 Mismatch:', edit_dis.count(0), '>0 Mismatch:', len(edit_dis)-edit_dis.count(0))

print("Neg. Strand:", neg, "Pos. Strand:", pos)
    
