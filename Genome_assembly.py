#!/usr/bin/env python3
import re

contig_dict = {}

with open("ecoli_0.25.contigs.fasta", 'r') as ecoli25fasta_obj:
    for line in ecoli25fasta_obj:
        line = line.rstrip()
        gene_found = re.search(r"^>", line) #gene_id and description
        if gene_found:
            geneID = line
            #contig_dict[geneID] = {}
            #seq = ""
            contig_dict[geneID] = ""
        else:
            contig_dict[geneID] += line
            #contig_length = len(seq)
            #contig_dict[geneID][seq] = contig_length

contigs = list(contig_dict.values())
sorted_contigs = sorted(contigs, key=len, reverse = True)
print(f"This is the longest contig: {sorted_contigs[0]}")
print(f" This is the shortest contig: {sorted_contigs[-1]}")
contig_length = [len(items) for items in sorted_contigs]
print(f"This is the length of longest contig: {contig_length[0]}")
print(f"This is the length of shortest contig: {contig_length[-1]}")
total_contig_length = sum(contig_length)

print(f"This is the total contig length: {total_contig_length}")

L50_size = 0
for item in sorted_contigs:
    if L50_size <= (total_contig_length / 2) :
        L50_size += len(item)
print(f"N50 is the: {len(item)}")
print(f"L50 is: {L50_size}")

