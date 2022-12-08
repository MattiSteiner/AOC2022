#!/usr/bin/env python
import re
import sys

file1 = open('day8.txt', 'r')
Lines = file1.readlines()

forrest = []
forrest = [forrest + list(line.strip()) for line in Lines] #store all lines in List 
forrest = [[int(j) for j in i]for i in forrest]


f_up = []
f_down = []
f_left = []
f_right = []

score = 1
max_score = 1
sol = 0

print(len(forrest[1]))

for row in range(1,len(forrest)-1):

	for collumn in range(1,len(forrest[row])-1): #each collumnn
		#print(forrest[row][collumn])
		f_left =  list(reversed(forrest[row][0:collumn]))
		f_right = forrest[row][collumn+1:]
		f_up = list(reversed([i[collumn] for i in forrest][0:row]))
		f_down = [i[collumn] for i in forrest][row+1:]


		for a in f_left:
			if a >= forrest[row][collumn]:
				score *=  (f_left.index(a)+1)
				sol = 1
				break
		if sol == 0:
			score *= len(f_left) if len(f_left)>0 else 1
		sol = 0




		for a in f_right:
			if a >= forrest[row][collumn]:
				score *=  (f_right.index(a)+1)
				sol = 1
				break
		if sol == 0:
			score *= len(f_right) if len(f_right)>0 else 1
		sol = 0



		for a in f_up:
			if a >= forrest[row][collumn]:
				score *=  (f_up.index(a)+1)
				sol = 1
				break
		if sol == 0:
			score *= len(f_up) if len(f_up)>0 else 1
		sol = 0


		for a in f_down:
			if a >= forrest[row][collumn]:
				score *=  (f_down.index(a)+1)
				sol = 1
				break
		if sol == 0:
			score *= len(f_down) if len(f_down)>0 else 1
		sol = 0

		print(row,collumn,forrest[row][collumn], score)

		if score > max_score:
			max_score = score
		score = 1
	

print("Score:", max_score)