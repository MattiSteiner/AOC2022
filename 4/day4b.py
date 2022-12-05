#!/usr/bin/env python
import array as arr

file1 = open('day4.txt', 'r')
Lines = file1.readlines()


doubles  = 0
value = list(['0','0','0','0'])

#task2

for line in Lines:
	i = 0
	lin = line.split(',')
	
	for values in lin:
		value[i:(i+1)] = values.split('-')
		i += 2
	v1 = [x for x in range(int(value[0]),int(value[1])+1)]
	v2 = [x for x in range(int(value[2]),int(value[3])+1)]
	print(v1)
	print(v2)
	
	print(list(set(v1)&set(v2)))
	if len(list(set(v1)&set(v2))) > 0:
		doubles += 1
	

	
	
print(doubles)