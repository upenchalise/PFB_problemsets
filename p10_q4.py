#! /usr/bin/env python3
import argparse
from p10_q3 import dna_ntmaxwhatever

#question number 4
parser = argparse.ArgumentParser(description="This test program parses through a dna sting with or without spaces and splits the string into n length lines")
#Add first argument
parser.add_argument("dna", type=str, help="string you enter")
parser.add_argument("nt_count", type=int, help="how many nucleotide to include in a line before splitting a line")
args = parser.parse_args()
dna = args.dna
n = args.nt_count
# if args.out:
print(f"This is the new dna output:")
print(dna_ntmaxwhatever(dna, n))
