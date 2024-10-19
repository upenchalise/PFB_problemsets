#! /usr/bin/env python3
import re

#question number 6
sequence = ""
with open("Python_07_ApoI.fasta.txt", 'r') as ApoI_fasta:
    #print(ApoI_fasta.read())
    for line in ApoI_fasta:
        gene_found=re.search(r'^>', line)
        if gene_found:
            geneID = line
        else:
            sequence += line
    print(sequence)

new_sequence = re.findall(r"[AG]AATT[CT]" , sequence)
print(new_sequence)