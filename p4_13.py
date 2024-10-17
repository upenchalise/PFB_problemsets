#!/usr/bin/env python3
import sys
new_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in new_list:
	print(new_list.index(seq), len(seq), (seq), sep="\t")
