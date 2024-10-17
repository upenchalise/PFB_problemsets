#! /usr/bin/env python3
p6_file_obj = open("Python_06.txt", "r")
p6_lower = ""
p6_upper = ""
for line in p6_file_obj:
    print(line)
    p6_upper += line.upper()
    p6_lower += line
print(p6_lower)
print(p6_upper)
