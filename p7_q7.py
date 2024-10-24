#! /usr/bin/env python3
import re

#question number 7
sequence = ""
with open("Python_07_ApoI.fasta.txt", 'r') as ApoI_fasta:
    #print(ApoI_fasta.read())
    for line in ApoI_fasta:
        line=line.rstrip()
        gene_found=re.search(r'^>', line)
        if gene_found:
            geneID = line
        else:
            sequence += line
    print(sequence)

new_sequence = re.findall(r"[AG]AATT[CT]" , sequence)
restriction_site= re.sub(r"([AG])AATT([CT])", r"\1^AATT\2", sequence)
print(restriction_site.count("^"))
print(restriction_site)

cut_sites = []
for match in re.finditer(r"(\^(\w+)\^)", restriction_site):
    cut_sites.append(match.group(2))
    print(cut_sites)
    print(len(cut_sites))
    print(match.group(2))

#question number 8
lengths = [len(item) for item in cut_sites]
print(lengths)

sorted_cut_sites = sorted(cut_sites,key=len)
print(sorted_cut_sites)

#other way to do question number 7 b or 8, nothing makes sense anymore
cutsites = re.findall(r"\^(\w+)\^" , restriction_site)
print(cutsites)

# cutsites = restriction_site.split("^")
# print(cutsites)