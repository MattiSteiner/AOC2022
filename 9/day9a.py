#!/usr/bin/env python
import re
import sys

file1 = open('day9.txt', 'r')
Lines = file1.readlines()


tot_dir = [0,0,0,0] #right left up down


def dis_HT(cH, cT): # distance from head to tail
	disX = cH[0] - cT[0]
	disY = cH[1] - cT[1]
	dlist =  [disX, disY]
	if disX > 1 or disX < -1:
		return dlist
	elif disY > 1 or disY <-1:
		return dlist
	else:
		return [0,0]  


#determine size of coordHinate system
for line in Lines:
	match line[0]:
		case 'R': tot_dir[0] += int(line[2])
		case 'L': tot_dir[1] += int(line[2])
		case 'U': tot_dir[2] += int(line[2])
		case 'D': tot_dir[3] += int(line[2])
			


maxX = int(tot_dir[0]) + int(tot_dir[1])
maxY = int(tot_dir[2]) + int(tot_dir[3])

print(maxX,maxY)

coordH = [tot_dir[1], tot_dir[2]] #x y head
coordT = [tot_dir[1], tot_dir[2]] #x y tail
coordHinatesS = [[0 for Y in range(int(tot_dir[2]) + int(tot_dir[3])) ]for X in range(int(tot_dir[0]) + int(tot_dir[1]))]


pre_dir = 0 
q = 0

tot_sum = 0 

for line in Lines:
	print(q, line)
	q +=1
	match line[0]:
		case 'R':
			for i in range(int(line[2])):
				coordH = [coordH[0]+1 , coordH[1]]
				dis = dis_HT(coordH,coordT)
				if dis[0] != 0 and dis[1] != 0:
					coordT = [coordT[0]+1 , coordT[1]+ dis[1]]
					
				elif dis[0] != 0:
					coordT = [coordT[0]+1 , coordT[1]]
				if not coordHinatesS[coordT[0]][coordT[1]] == 1:
					tot_sum +=1 
				coordHinatesS[coordT[0]][coordT[1]] = 1
				#print(dis, coordH,coordT)

		case 'L':
			for i in range(int(line[2])):
				coordH = [coordH[0]-1,coordH[1]]
				dis = dis_HT(coordH,coordT)
				if dis[0] != 0 and dis[1] != 0:
					coordT = [coordT[0]-1 , coordT[1]+dis[1]]
					#print("Movement D",dis, coordH)
				elif dis[0] != 0:
					coordT = [coordT[0]-1 , coordT[1]]
					#print("move RL")
				if not coordHinatesS[coordT[0]][coordT[1]] == 1:
					tot_sum +=1 
				coordHinatesS[coordT[0]][coordT[1]] = 1
				#print(dis, coordH,coordT)

		case 'U':
			for i in range(int(line[2])):
				coordH = [coordH[0],coordH[1]-1]
				dis = dis_HT(coordH,coordT)
				if dis[0] != 0 and dis[1] != 0:
					coordT = [coordT[0]+dis[0] , coordT[1]-1]
					#print("Movement D",dis, coordH)
				elif dis[1] != 0:
					coordT = [coordT[0], coordT[1]-1]
					#print("move UD")
				if not coordHinatesS[coordT[0]][coordT[1]] == 1:
					tot_sum +=1 
				coordHinatesS[coordT[0]][coordT[1]] = 1
				#print(dis, coordH,coordT)


		case 'D':
			for i in range(int(line[2])):
				coordH = [coordH[0],coordH[1]+1]
				dis = dis_HT(coordH,coordT)
				if dis[0] != 0 and dis[1] != 0:
					coordT = [coordT[0]+dis[0] , coordT[1]+1]
					#print("Movement D",dis, coordH)
				elif dis[1] != 0:
					coordT = [coordT[0], coordT[1]+1]
					#print("move UD")
				if not coordHinatesS[coordT[0]][coordT[1]] == 1:
					tot_sum +=1 
				coordHinatesS[coordT[0]][coordT[1]] = 1

				#print(dis, coordH,coordT)
		case other: 
			print("no command")



print("Tot Fields:", tot_sum)
print("Tot fields: ",sum(i > 0 for i in sum(coordHinatesS,[])))


