#!/usr/bin/env python

file1 = open('day5.txt', 'r')
Lines = file1.readlines()

ctrl = [0,0,0]


body = 0

stack = [[]  for n in range(9)]


for line in Lines:
	i = 0
	c_pos = 0
	
	if body == 0:
		for char in line:
			if char.isalpha():
				stack[int((c_pos-1)/4)].append(char)
			c_pos += 1
			
	else:
		for numbers in line.split():
		 	if numbers.isdigit():
		 		ctrl[i] = int(numbers)
		 		i += 1
		print(stack)
		t_values = stack[ctrl[1]-1][0:ctrl[0]]
		for p in t_values:

			stack[ctrl[2]-1].insert(0,p)
			stack[ctrl[1]-1].pop(0)
			
	if line.strip() == '':
		body = 1
		print("body reached")
	

	

for d in range(9):
	print(stack[d][0])