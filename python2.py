#! /usr/bin/env python3
import sys

count = int(sys.argv[1])
if count < 50:
	message = "is less than 50"
	print(count, message)
elif count > 50:
	message = "is greater than 50"
	print(count, message)
elif count < 0: 
	message = "is less than 0 and is neagtive"
	print(count, message)
else:
	message = "must be 50"
	print(count, message)

if count == 52:
	print('Aye captain')

x = int(sys.argv[2])

if x < 0:
	print('Negative number')
elif x == 0:
	print('Number is a zero')
else:
	print('Positive number')
	if x < 50:
		print ('Positive but less than 50')
	elif x == 50:
		print ('Positive and 50')
	if x % 2 == 0:
		print('even number')
	else:
		print('odd number')
	if x > 50:
		print('Positive and greater than 50')
		if x % 3 == 0:
			print('divisible by 3')
		else:
			print('not divisible by 3')
