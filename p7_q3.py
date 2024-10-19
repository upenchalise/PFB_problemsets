#! /usr/bin/env python3
import re

#question number 3

Python_07_fasta = open("Python_07.fasta.txt",  'r')
all_seq = []
for line in Python_07_fasta:
    seq_found = re.search(r'^>', line)
    if seq_found:
        all_seq.append(line)
    print(seq_found)
print(all_seq)
length = len(all_seq)
print(length)