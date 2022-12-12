#!/usr/bin/env python

file1 = open('day7Samp.txt', 'r')
Lines = file1.readlines()


body = 0

files = [] #directory size 
directory = ''
directory_empty = []


for line in Lines:
	if line[0] == '$': #command
		if line.split()[1] == "cd":
			if line.split()[2].isalpha(): #move to directory in
				directory = line.split()[2] + ',' + directory

			
			elif line.split()[2] == '/': #dir out
				directory =""

			else:	#change directory up
				directory = directory[directory.index(',')+1:]

	elif line.split()[0].isnumeric(): # if file
		if any(directory in x for x in files): # if dir exist add size
			index = files.index([ind for ind in files if directory in ind][0])
			files[index][1] = int(line.split()[0]) + int(files[index][1])

		else: #create dir 
			files.append([directory[:-1], line.split()[0]])

	# elif line.split()[0] == "dir": # save all directorys
	# 	for i in files:
	# 	directory_empty.append(line.split()[1])


files.sort(reverse=True)


dir_path = [] 
dir_size = []

#add all files from directroy 
for i in range(len(files)):
	if files[i][0] in dir_path:
		dir_index = dir_path.index(files[i][0])
		dir_size[dir_index] = int(dir_size[dir_index]) + int(files[i][1])
	else:

		dir_path.append(files[i][0])
		dir_size.append(files[i][1])

print("size:", len(dir_path))
#add subdir to dir


def total_folder():

	for i in range(len(dir_path)):
		print("path",dir_path[i])
		if ',' in dir_path[i]:
			if dir_path[i][dir_path[i].index(',')+1:] in dir_path:
				dir_index = dir_path.index(dir_path[i][dir_path[i].index(',')+1:])
				dir_size[dir_index] = int(dir_size[dir_index]) + int(dir_size[i])
				print("hi",dir_path[i][dir_path[i].index(',')+1:], dir_size[dir_index])
			else:
				dir_path.insert(i,dir_path[i][dir_path[i].index(',')+1:])
				dir_size.insert(i,0)#dir_size[i])
				print(dir_path[i])
				total_folder()


total_folder()


#add subdir to dir

#count size
print(dir_size,dir_path)
tot_size = 0
for i in range(len(dir_path)):
	if int(dir_size[i]) <= 100000:
		print(dir_size[i])
		tot_size += int(dir_size[i])

print("Sum of Data:", tot_size)





