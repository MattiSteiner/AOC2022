#!/usr/bin/env python


s_ind =0 

with open("day13.txt") as inp:
    comps = inp.read().strip().split("\n\n")


def comparison(a, b):

	if isinstance(a, list) and isinstance(b, int):
		b = [b]
	if isinstance(a, int) and isinstance(b, list):
		a = [a]
	if isinstance(a, int) and isinstance(b, int):
		#print("a",a,"b",b)
		if a < b:
			print("a<b")
			return True
		elif a > b:
			return False
		

	#compare lists
	if isinstance(a, list) and isinstance(b, list):
		for a_i, a_num in enumerate(a):
			#print("ai", a_num, a, b)
			try:#if a_i < len(b):
				subcomp = comparison(a_num,b[a_i])
				#print("subcomp", subcomp)
				if subcomp:
					return True
					
				elif subcomp == False:
					return False

			except:
				None
			# 	return False



		if len(a)<len(b):

			return True
		elif len(a)==len(b):
			return True	
		else:
			return False


	#print(inp_a, inp_a[0])


for index, b_comp in enumerate(comps):
	# get inputs as lists
	inp_a, inp_b = b_comp.split("\n")
	inp_a = eval(inp_a)
	inp_b = eval(inp_b)


	# make all inputs to list or int
	
	if comparison(inp_a,inp_b): 
		
		s_ind += (index+1)
		print(index+1, s_ind)


print("Sum of index:", s_ind)


