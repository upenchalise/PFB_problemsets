#! /usr/bin/env python3

with open("Python_06.fastq.txt", "r") as fastq_read:
    line_count = 0
    total_chr = 0
    for line in fastq_read:
        line = line.rstrip()
        print(line)
        #Python_06_fastq = fastq_read.read()
        #print(Python_06_fastq)
        line_count += 1
        chr_count = len(line)
        total_chr += chr_count
    print(total_chr)
    print(line_count)
Average = total_chr/line_count
print(f'{Average} is the average number of characters per line')