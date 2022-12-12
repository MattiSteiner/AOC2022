#!/usr/bin/env python
import re
import sys


file1 = open('day11S.txt', 'r')
Lines = file1.readlines()



inp = "old|([0-9]+|[*-+])"

monk_it = list()
monk_op = list()
monk_test = list()
monk_div = list()
n_monk = 0

n_insp = [0,0,0,0,0,0,0,0]

for line in Lines:
	#print(re.findall(inp, line))
	if re.findall(inp, line) == []:
		n_monk += 1

	elif(re.search("Starting",line)):
		monk_it.append(re.findall(inp, line))
	elif(re.search("Operation",line)):
		monk_op.append(re.findall(inp, line))
	elif(re.search("Test",line)):
		monk_div.append(re.findall(inp,line))	
	elif(re.search("If",line)):
		monk_test.append(re.findall(inp,line))


monk_div = sum(monk_div,[])
monk_test = sum(monk_test,[])

		
for e in range(10000):
	for n in range(len(monk_it)):
		#print(n,monk_it[n],monk_op[n],monk_div[n],monk_test[n*2],monk_test[n*2+1])
		print(e, n_insp)	
		for x in range(len(monk_it[n])):
			#operation
			n_insp[n] += 1


			v2 = 0
			if monk_op[n][2] == '':
				v2 = int(monk_it[n][0])
			else:
				v2 = int(monk_op[n][2])
			
			wor_val = int(monk_it[n][0])%int(monk_div[n])

			if monk_op[n][1] == '*':
				wor_val = int(monk_it[n][0]) * v2
			elif monk_op[n][1] == '+':
				wor_val = int(monk_it[n][0]) + int(v2)
			
			#wor_val /= 3
						
			#check if divisable
			if int(wor_val)%int(monk_div[n]) == 0:
				monk_it[int(monk_test[n*2])].append(int(wor_val))
			else: 
				monk_it[int(monk_test[n*2+1])].append(int(wor_val))
			monk_it[n].remove(monk_it[n][0])


print(n_insp)
n_insp = sorted(n_insp,reverse=True)
print("Result: " , n_insp[0]*n_insp[1])