#! /usr/bin/env python3

def get_rev_comp(dna):
    dna = dna.replace("A", "t").replace("C","g").replace("T", "a").replace("G", "c")
    dna_upper = dna.upper()
    return(dna_upper)

if __name__ == "__main__":
    dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCA"
    rev_comp_seq = get_rev_comp(dna)
    print(rev_comp_seq)