from threading import Thread, Lock

lock=Lock()
char='a'
def AtoZ(threadId):
	global char
	for _ in range(40):
		with lock:
			print("Ascii of",char,"is",str(ord(char)),"\t by thread",threadId)
			char=chr(ord(char)+1)

thread1=Thread(target=AtoZ, args=("Thread-1",))
thread2=Thread(target=AtoZ, args=("Thread-2",))

thread1.start()
thread2.start()

