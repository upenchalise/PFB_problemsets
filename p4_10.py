#!/usr/bin/env python3
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
for num in range (num1, num2+1):
	print(num)
if num1<num2:
	print(num1, 'is the minimum and' ,num2, 'is the maximum')
else:
	print(num2, 'is the minimum and' ,num1, 'is the maximum')
