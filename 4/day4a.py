#!/usr/bin/env python
import array as arr

file1 = open('day4.txt', 'r')
Lines = file1.readlines()


doubles  = 0
value = list(['0','0','0','0'])

#task1
for line in Lines:
	i = 0
	lin = line.split(',')
	
	for values in lin:
		value[i:(i+1)] = values.split('-')
		i += 2


	if (int(value[0])<= int(value[2]) and int(value[1]) >= int(value[3])) or (int(value[0])>= int(value[2]) and int(value[1]) <= int(value[3])):
		doubles +=1
		print(value[0],value[1],value[2],value[3])

	
	
print(doubles)

