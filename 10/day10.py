#!/usr/bin/env python
import re
import sys

file1 = open('day10.txt', 'r')
Lines = file1.readlines()
cycle = 0
regx = 1
sumreg = []

def check_reg():
	if cycle == 20 or ((cycle-20)%40) == 0:
		sumreg.append(regx*cycle)
		print(cycle,regx)

for line in Lines:
	inp = line.split()

	if len(inp) > 1:
		cycle +=1
		check_reg()
		cycle +=1
		check_reg()
		regx += int(inp[1])
	else:
		cycle += 1
		check_reg()
	print(cycle, regx)
print("Register Val:", regx)
print("Summe von Reg:", sum(sumreg))
print(sumreg)