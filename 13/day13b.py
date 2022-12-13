#!/usr/bin/env python

from functools import cmp_to_key

s_ind =0 

with open("day13.txt") as inp:
    comps = inp.read().strip().split("\n\n")


def comparison(a, b):

	if isinstance(a, list) and isinstance(b, int):
		b = [b]
	if isinstance(a, int) and isinstance(b, list):
		a = [a]
	if isinstance(a, int) and isinstance(b, int):
		#print("a",a,"b",b)
		if a < b:
			return 1
		elif a > b:
			return -1
		

	#compare lists
	if isinstance(a, list) and isinstance(b, list):
		for a_i, a_num in enumerate(a):
			#print("ai", a_num, a, b)
			try:#if a_i < len(b):
				subcomp = comparison(a_num,b[a_i])
				#print("subcomp", subcomp)
				if subcomp == 1:
					return 1
					
				elif subcomp == -1:
					return -1

			except:
				None
			# 	return -1



		if len(a)<len(b):
			return 1
		elif len(a)==len(b):
			return 0	
		else:
			return -1


	#print(inp_a, inp_a[0])


for index, b_comp in enumerate(comps):
	# get inputs as lists
	inp_a, inp_b = b_comp.split("\n")
	inp_a = eval(inp_a)
	inp_b = eval(inp_b)


	# make all inputs to list or int
	
	if comparison(inp_a,inp_b)==1: 
		
		s_ind += (index+1)



print("Sum of index:", s_ind)


########### Part 2 ###############

lists = list()
#print(comps)
for n, b_comp in enumerate(comps):
	b_split = b_comp.split("\n")
	for i, item in enumerate(b_split):
		lists.append(eval(item))
lists.append([2])
lists.append([6])

lists = sorted(lists, key = cmp_to_key(comparison), reverse = 1)

key = 1
for i, list_i in enumerate(lists):
	if list_i ==[2] or list_i ==[6]:
		key *= (i+1)
print("key: ", key)