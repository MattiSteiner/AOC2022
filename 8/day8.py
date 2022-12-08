#!/usr/bin/env python
import re
import sys

file1 = open('day8.txt', 'r')
Lines = file1.readlines()

forrest = []
forrest = [forrest + list(line.strip()) for line in Lines] #store all lines in List 
forrest = [[int(j) for j in i]for i in forrest]


v_tree_in = [[0]*(len(forrest[i])-2) for i in range(1, len(forrest)-1)] #create inner list filled 0

v_tree = 0
n_row = 0
max_rowU = forrest[0]
max_rowD = forrest[-1]
max_colL = 0
max_colR = 0

for row in forrest:
	max_colL = forrest[n_row][0]
	max_colR = forrest[n_row][-1]
	
	if n_row == 0 or n_row == len(forrest)-1:
		v_tree += len(forrest)
	else:	
		for collumn in range(1, len(row)-1 ): #each collumnn
			if forrest[n_row][collumn-1] < forrest[n_row][collumn] and forrest[n_row][collumn] > max_colL: #handle left - right
				v_tree_in[n_row-1][collumn-1] = 1
				max_colL = forrest[n_row][collumn]

			if forrest[n_row][len(row)-collumn] < forrest[n_row][len(row)-1-collumn] and forrest[n_row][len(row)-1-collumn] > max_colR: #handle right - left
				v_tree_in[n_row-1][len(row)-2-collumn] = 1
				max_colR = forrest[n_row][len(row)-1-collumn]

			if forrest[n_row-1][collumn] < forrest[n_row][collumn] and forrest[n_row][collumn] > max_rowU[collumn]: #handle up - down
				max_rowU[collumn] = forrest[n_row][collumn]
				v_tree_in[n_row-1][collumn-1] = 1

			if forrest[len(forrest)-n_row][collumn] < forrest[len(forrest)-n_row-1][collumn] and  forrest[len(forrest)-n_row-1][collumn] > max_rowD[collumn]: #handle up - down
				max_rowD[collumn] = forrest[len(forrest)-n_row-1][collumn]
				v_tree_in[len(forrest)-n_row-2][collumn-1] = 1


		
	n_row += 1

v_tree = 2*len(forrest) + 2*(len(forrest[0])-2) + sum(i > 0 for i in sum(v_tree_in,[]))
print("tot vis tree:",v_tree)
