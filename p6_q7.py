#! /usr/bin/env python3

genes = {}
with open("Python_06.seq.txt", "r") as gene_read:
    for line in gene_read:
        line = line.rstrip()
        gene_id,seq = line.split()
        genes[gene_id] = seq
#print(genes)

with open("Python_06_uc.fasta", "w") as Python_06_edited:
    #print(genes['c66_g2_i1'])
    for gene_id in genes:
        seq = genes[gene_id] 
        A = seq.replace('A', '4').replace('T' , '5').replace('G' , '6').replace('C' , '7')
        T = A.replace('4', 'T').replace('5', 'A').replace('6' , 'C').replace('7' , 'G')
        #print(T)
        #print(A)
        rev_dna1 = T[::-1]
        #rev_complement.append(rev_dna1)
        #print(rev_complement)
        genes[gene_id]=rev_dna1
    #Python_06_edited.write(genes)
    #print(genes['c66_g2_i1'])
    
# for gene in genes:
#     #print(gene)

        print(f'Reverse complement of {gene_id} is {rev_dna1}')