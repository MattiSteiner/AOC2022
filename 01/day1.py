#!/usr/bin/env python
import array as arr

file1 = open('elves.txt', 'r')
Lines = file1.readlines()

count = 0 
calories = 0
m1cal = 0
m2cal = 0
m3cal = 0
eleves = 0
totcal = 0

for line in Lines:
	count += 1 
	if line == "\n":
		if calories > m1cal:
			m3cal = m2cal
			m2cal = m1cal
			m1cal = calories
		elif calories > m2cal:
			m3cal = m2cal
			m2cal = calories
		elif calories > m3cal:
			m3cal = calories
		eleves += 1
		calories = 0
		
	else:
		calories = calories + int(line) 
	totcal = m1cal + m2cal + m3cal
	print(calories)
	print("maxcal: {}".format(totcal))
print(eleves)