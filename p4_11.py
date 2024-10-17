#!/usr/bin/env python3
import sys
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num_list = list(range(num1, num2+1))

odd_num_list= []
for num in num_list:
	if num%2 != 0:
		odd_num_list.append(num)
print(odd_num_list)

