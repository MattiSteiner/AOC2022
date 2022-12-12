#!/usr/bin/env python
import re
import sys

file1 = open('day10.txt', 'r')
Lines = file1.readlines()
cycle = 0
regx = 1
line = 0
pix = [0 for i in range(0,240)]
adval = 0

def check_draw():
	print(cycle, regx)

	if cycle%40 >= regx-1 and cycle%40 <= regx+1:
		pix[cycle] = '#'
		print("x at", cycle)
	else:
		pix[cycle] = '.'

for cycle in range(240):
	check_draw()
	if adval == 1: 
		regx += int(inp[1])
		adval = 0 
	else:
		inp = Lines[line].split()
		line += 1
		if len(inp) > 1: 
			adval = 1
		


output = list()

for i in range(0, len(pix), 40):
	output.append(pix[i:i+40])
	
for j in range(6):
	print(' '.join(output[j]))



