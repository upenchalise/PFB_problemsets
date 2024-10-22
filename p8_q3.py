#! /usr/bin/env python3
import re

#question number 1

gene_dict = {}

with open("Python_08.fasta.txt", 'r') as P8fasta_obj:
    #print(P8fasta_obj.read())
    for line in P8fasta_obj:
        line = line.rstrip()
        # seq = "sequence"
        gene_found = re.search(r"^>(\S+)\s(\w+)\=(\d+)\s(\w+)\=(\S+)", line) #gene_id and description
        if gene_found:
            geneID = gene_found.group(1)
            # len = gene_found.group(2)
            # count = gene_found.group(3)
            # path = gene_found.group(4)
            # loc = gene_found.group(5)
            # gene_dict[geneID] = {}
            # gene_dict[geneID][len] = count
            # gene_dict[geneID][path] = loc
            gene_dict[geneID] = ""
            # gene_dict[geneID]["nt_count"] = {"A": 0, "T": 0, "C": 0, "G": 0} 
        else:
            gene_dict[geneID] += line
            # A = seq.count("A")
            # T = seq.count("T")
            # C = seq.count("C")
            # G = seq.count("G")
            # gene_dict[geneID]["nt_count"]["A"] = gene_dict[geneID][seq].count("A")
            # gene_dict[geneID]["nt_count"]["T"] = gene_dict[geneID][seq].count("T")
            # gene_dict[geneID]["nt_count"]["C"] = gene_dict[geneID][seq].count("C")
            # gene_dict[geneID]["nt_count"]["G"] = gene_dict[geneID][seq].count("G")
    #print(gene_dict)

# i = 0
with open('Python_08.codons-frame-1.nt', 'w') as file_obj:
    codon_dict_frame1={}
    codon_dict_frame2={}
    codon_dict_frame3={}
    for i in gene_dict:
        # print(gene_dict[i])
        print (i)
        frame1 = re.findall(r"(.{3})", gene_dict[i])
        frame2 = re.findall(r"(.{3})", gene_dict[i][1:])
        frame3 = re.findall(r"(.{3})", gene_dict[i][2:])
        codon_frame1 = " ".join(frame1)
        codon_frame2 = " ".join(frame2)
        codon_frame3 = " ".join(frame3)
        print(codon_frame1)
        print(codon_frame2)
        print(codon_frame3)
        codon_dict_frame1[i] = codon_frame1
        codon_dict_frame2[i] = codon_frame2
        codon_dict_frame3[i] = codon_frame3
        # i += 1
    file_obj.write(f"All the codons for each of the genes Codon frame 1: {codon_dict_frame1}\n codon frame 2\n: {codon_dict_frame2}\n codon frame 3:\n{codon_dict_frame3}")