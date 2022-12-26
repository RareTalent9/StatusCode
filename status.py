#!/usr/bin/python3
import sys, requests
def status():
	for i in sys.stdin.readlines():
		f=i.strip("\n")
		if f.startswith("https://") or f.startswith("http://"):
			r=requests.get(f,timeout=10,allow_redirects=False)
			#print(f,"\t","[{}]".format(r.status_code))
			d=r.headers
			print(d.get('Location'),"\t","HTTPS\t[{}]".format(r.status_code))
		else:
			f="http://"+f
			r=requests.get(f,timeout=10,allow_redirects=False)
			#print(f,"\t","[{}]".format(r.status_code))
			d=r.headers
			print(d.get('Location'),"\t","HTTPS\t[{}]".format(r.status_code))
try:
	status()
except IOError as a:
	print("Input/Output Error: ",a)
except Exception as a:
	print("Regular Error: ",a)
except KeyboardInterrupt as a:
	print("Execution Interrupted")
else:
	print("Execution Successful")
finally:
	print("Execution Completed")
