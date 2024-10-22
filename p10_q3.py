#! /usr/bin/env python3

#question number 3
def dna_ntmaxwhatever(dna, n):
    dna = dna.replace("\n", "")
    new_dna = [(dna[i:i+n]) for i in range(0, len(dna), n)] #list comprehension it is giving a list of nts every nth character 
    new_dna_out="\n".join(new_dna) # joins the list with a new line on the item
    return new_dna_out

#This if statement will indicate the codes when function is imported as module.
if __name__ == "__main__":
    dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
    new_dna = dna_ntmaxwhatever(dna, 80)
    print(f'This is the new dna output split at every 60 nucleotides: \n{new_dna}')
    print(repr(new_dna))