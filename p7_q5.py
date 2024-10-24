#! /usr/bin/env python3
import re

#question number 5 WORKED MAGICALLY IN THE FIRST TRY
gene_dict = {}
sequence = ""
with open("Python_07.fasta.txt",  'r') as Python_07_fasta:
    #print(Python_07_fasta.read())
    for line in Python_07_fasta:
        gene_found = re.search(r"(^>\S+)\s(.*)", line) #gene_id and description
        seq_found = re.search(r"^[ATGCU]", line)
        if gene_found:
            #print(seq_found)
            geneID = gene_found.group(1)
            #print(seqName)
            gene_dict[geneID] = ""
            sequence = ""
        if seq_found:
            sequence += line
            #print(description)
            gene_dict[geneID]=sequence
    print(gene_dict)