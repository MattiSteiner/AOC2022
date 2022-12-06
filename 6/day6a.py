#!/usr/bin/env python

file1 = open('day6.txt', 'r')
datastream = file1.read()


for i in range(4, len(datastream)):
	block = datastream[i-4:i]
	print(block, datastream[i-1])
	if  len(set(block)) == len(block):
		print(block, datastream[i-1], i)
		break

	


