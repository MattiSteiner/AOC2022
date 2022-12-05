#!/usr/bin/env python
import array as arr

file1 = open('rps.txt', 'r')
Lines = file1.readlines()

score  = 0 

score_l = ["B X\n", "A Y\n", "C Z\n", 
		 "C X\n", "B Y\n", "A Z\n",
		 "A X\n", "C Y\n", "B Z\n"] # 

#task1
# for line in Lines:
# 	index = score_l.index(line) 
# 	score = score + ((index%3)+1) + (int(index/3)) * 3

#task2
for line in Lines:
	index = score_l.index(line) 
	score = score + (int(index/3)+1) + (index%3) * 3
	
	
print(score)