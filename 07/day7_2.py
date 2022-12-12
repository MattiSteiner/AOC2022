#!/usr/bin/env python
import re
import sys

file1 = open('day7.txt', 'r')
Lines = file1.readlines()



dir_down = "cd ([A-Za-z0-9]+)"
dir_up = "cd \.\."
file = "([0-9]+) (?:[A-Za-z0-9]+)"
dir_0 = [""]

filesys = dict()
fsize =0 

for line in Lines:
	if re.search(dir_up, line):
		dir_0 = dir_0[:-1]
	elif re.search(dir_down, line):
		dir_0.append(re.findall(dir_down,line)[0])
	elif re.search(file, line):
		
		fsize = int(re.findall(file,line)[0])
		fpath = ""
		for dir in dir_0:
			fpath = fpath + ',' + dir
			if not fpath in filesys:
				filesys[fpath] = 0
			filesys[fpath] += fsize
tot_sum = 0

for x in filesys:
	if filesys[x] <= 100000:
		tot_sum += filesys[x]

print("totsum: ", tot_sum )

tot_sum = sys.maxsize

for x in filesys:
	if filesys[x] >= (filesys[','] - 40000000) and filesys[x] < tot_sum:
		tot_sum = filesys[x]
print("filesum min: ", tot_sum)


