#! /usr/bin/env python3
import re

#question number 4
all_seq = {}
with open("Python_07.fasta.txt",  'r') as Python_07_fasta:
    #print(Python_07_fasta.read())
    for line in Python_07_fasta:
        seq_found = re.search(r"(^>\S+)\s(.*)", line) #(^>\w+)\s(\w+)
        if seq_found:
            print(seq_found)
            seqName = seq_found.group(1)
            print(seqName)
            description = seq_found.group(2)
            print(description)
            all_seq[seqName]=description
    print(all_seq)
        #else:
            #print("Not found")
        # seqName = seq_found.group(1)
        # print(seqName)
        # description = seq_found.group(2)
        # print(description)
        # all_seq[seqName]=description
        # print(all_seq)