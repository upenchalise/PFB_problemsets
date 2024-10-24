#!/usr/bin/env python3

import sys

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 reverse_complement.py <input.fasta>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as fasta_file:
        sequence_name = ""
        sequence = ""

        for line in fasta_file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_name:
                    # Process the previous sequence
                    rev_comp = reverse_complement(sequence)
                    print(f">{sequence_name} reverse complement")
                    for i in range(0, len(rev_comp), 60):  # Print in lines of 60 characters
                        print(rev_comp[i:i + 60])
                
                # Start a new sequence
                sequence_name = line[1:]  # Get the name after '>'
                sequence = ""
            else:
                sequence += line  # Append to the current sequence

        # Don't forget to process the last sequence in the file
        if sequence_name:
            rev_comp = reverse_complement(sequence)
            print(f">{sequence_name} reverse complement")
            for i in range(0, len(rev_comp), 60):
                print(rev_comp[i:i + 60])

if __name__ == "__main__":
    main()