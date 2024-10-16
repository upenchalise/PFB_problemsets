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


