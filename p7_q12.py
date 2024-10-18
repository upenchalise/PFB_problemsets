#! /usr/bin/env python3
import re

#question number 1

Python_07_obj = open("Python_07_nobody.txt",  'r')
#found_nb = re.findall(r"Nobody", Python_07_obj)
#print(found_nb)
##count = len(found_nb)
#print(count)
count = 0
#found_nobody = ""
for line in Python_07_obj:
    print(line)
    # break
    found_nobody = re.search(r"Nobody", line)
    if found_nobody:
        count += 1
    print(found_nobody)
    #break
print(count)

#question number 2
updated_line = ""
with open('Python_07_nobody.txt', 'r') as nb_read, open('Larissa.txt', 'w') as lrs_write:
    for line in nb_read:
        new_line = re.sub(r"Nobody", "Larissa", line)
        print(new_line)
        #updated_line += new_line
        lrs_write.write(f"{new_line}")

print(lrs_write)