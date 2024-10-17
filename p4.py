#! /usr/bin/env python3

taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)
taxa_list = taxa_string.split(' : ')
print(taxa_list)
print(taxa_list[1])
print(type(taxa_list))
print(type(taxa_string))
print("Sorted taxa list:", sorted(taxa_list))
len_sorted = sorted(taxa_list, key=len)
print("Length sorted:", len_sorted)


#question number 4
x = 0
while x < 101:
	print("x:", x)
	x += 1
print("DONE")

#question number 5

import math
print(math.factorial(100))

n = 5
factorial = 1
while n > 1:
	factorial*=n
	n-=1
	print(factorial)
print("DONE")

n = 100
factorial = 1
while n > 1:
	factorial*=n
	n-=1
print(format(factorial, '.2e'))

#question number 6
numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
	if num%2 == 0:
		print(num)
#question number 7
numbers = [101,2,15,22,95,33,2,27,72,15,52]
numbers_sorted = sorted(numbers)
numbers_it = iter(numbers)
odd_sum=0
even_sum=0
for num in numbers_it:
	print(num)
	if num%2 == 0: 
		even_sum+=num
	else:
		odd_sum+=num
print(even_sum)
print(odd_sum)

sum_of_odd_numbers = 101+15+95+33+27+15
sum_of_even_numbers = 2+22+2+72+52
print(sum_of_even_numbers)
print(sum_of_odd_numbers)

#question number 8

for num in range(100):
	print(num)	

print(list(range(100)))

num_list = []
for num in range(1, 101):
	num_list.append(num)

print(num_list)

print(list(range(101)))

#question number 9
numbers = [ num  for num in range(1, 101)]
print(numbers)

