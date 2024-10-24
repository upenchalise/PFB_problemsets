#! /usr/bin/env python3
#import argparse
def GC_percent(dna):
    count_G, count_C, count_A, count_T = 0, 0, 0, 0
    dna = dna.replace("\n", "")
    for base in dna:
        if base == 'C':
            count_C += 1
        elif base == 'G':
            count_G += 1
        elif base == 'A':
            count_A += 1
        elif base == 'T':
            count_T += 1
    GC_content = count_C + count_G
    Total_content = count_A + count_C + count_G + count_T
    GC_percent = GC_content / Total_content 
    return(GC_percent)

#This is to avoid running it when I call the above funciton in a separate script.
if __name__ == "__main__":
    dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
    print(f"{GC_percent(dna):.2%}")


# def main():
#     parser = argparse.ArgumentParser(description="This test program checks gc content in a DNA sequence")
#     #Add first argument
#     parser.add_argument("dna", type=str, help="string you enter")
#     parser.add_argument("GC_count", type=int, help="how many nucleotide to include in a line before splitting a line")
#     args = parser.parse_args()
#     dna = args.dna
#     n = args.nt_count
# if args.out:
# print(f"This is the new dna output:")
# print(dna_ntmaxwhatever(dna, n))
