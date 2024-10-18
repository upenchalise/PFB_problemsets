#! /usr/bin/env python3

with open("Python_06_q9.fasta", "r") as fasta_read:
    for lines in fasta_read:
        lines = lines.rstrip()
        print(lines)

genes_dict = {}
#seq = []
with open("Python_06_q9.fasta", "r") as gene_read:
    for line in gene_read:
        line = line.rstrip()
        if line.startswith(">"):
           gene_id = line
           genes_dict[gene_id] = ""
        else:
            #seq = line
            #seq.append(line)
            genes_dict[gene_id] += line
        #genes_dict={gene_id, seq}
        
print(genes_dict)