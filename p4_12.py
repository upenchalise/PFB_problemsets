#! /usr/bin/env python3
import sys
num_list = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
odd_numlist = [odd_numlist.append(num) for num in num_list if num%2 !=0]
print(odd_numlist)
