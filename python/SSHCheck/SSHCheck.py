import os, time, subprocess, threading

def check(spid):
	result = os.popen("lsof -i:7070").read()
	if result == "":
		subp = subprocess.Popen(["ssh", "-D", "7070", "-g", "jiangnan@199.115.119.195"])
		spid = subp.pid
	else:
		return 0
	threading.Timer(5,check,(spid))

if __name__ == '__main__':
	check(0)
	#print check()