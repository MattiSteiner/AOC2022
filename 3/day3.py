#!/usr/bin/env python
import array as arr

file1 = open('back3.txt', 'r')
Lines = file1.readlines()

#task 1
# length =0 
# result = 0
# for line in Lines:
# 	parta = line[0:int(len(line)/2)]
# 	partb = line[int(len(line)/2):]

# 	doubles = list(set(parta)&set(partb))

# 	for b in doubles:
# 		if b.isupper():
# 			result = result + ord(b) - 38
# 		else:
# 			result = result + ord(b) - 96

	
# print(result)
# print(partb)

#task 2 

e1 = 0
e2 = 0
e3 = 0
i = 0

result = 0
for line in Lines:
	i += 1
	if i%3 == 0:
		e3 = line
		doubles = list(set(e1)&set(e2)&set(e3))

		for b in doubles:
			print(b)
			if b.isupper():
				result = result + ord(b) - 38
			elif b.islower():
				result = result + ord(b) - 96
	elif i%3 == 1:
		e2 = line
	else: 
		e1 = line
	
print(result)
