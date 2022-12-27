#!/usr/bin/python3
import sys
def sub():
	f=open(sys.argv[1],"r")
	inp=f.readlines()
	list=[]
	for i in inp:
		list.append(i.strip("\n"))
	for j in range(0,len(list)):
		print("\n")
		print(list[j]+"."+sys.argv[2])
		for k in range(0,len(list)):
			if list[j] != list[k]:
				print(list[j]+"."+list[k]+"."+sys.argv[2])
try:
	sub()
except IOError as a:
	print("Input/Output Error --> ")
except Exception as a:
	print("Logical Error: ")
except KeyboardInterrupt as a:
	print("Execution Interrupted")
else:
	print("\n")
	print("Execution Successful")
finally:
	print("Execution Completed")

