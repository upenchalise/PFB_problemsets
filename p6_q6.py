#! /usr/bin/env python3
with open("Python_06.txt", "r") as p6_file_obj:
    Python_06_content = p6_file_obj.read() 

with open("Python_06_uc.txt", "w") as p6_edited_file_obj:
    for line in Python_06_content:
        p6_edited_file_obj.write(line.upper())



