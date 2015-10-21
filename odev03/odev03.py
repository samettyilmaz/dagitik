#!/usr/bin/python
import sys
import Queue
import threading
import time

exitFlag = 0

if (len(sys.argv) != 4):
        sys.exit('Usage: sub.py <s> <n> <l> ')

alphabet = list('abcdefghijklmnopqrstuvwxyz')
s,n,l= int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
i,j,wordList,finalList,worker_list,crypte_siralamasi=0,0,[],[],[],[]
input_txt=open("metin.txt") 
dataList =((input_txt.read()).lower()) 


def encrypt(text_to_encrypt):
        cipher = ''
            
        for c in text_to_encrypt:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)-s)%(len(alphabet))].upper()
            else :
                cipher +=c
        return cipher

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            worker_list.append(threadName)
            crypte_siralamasi.append(threadName)
            data2=encrypt(data)
            finalList.append(data2)
            
            
        else:
            queueLock.release()
        time.sleep(0.1)





while j < int(len(dataList)):
    wordList.append(dataList[j:j+l])
    j+=l


queueLock = threading.Lock()
workQueue = Queue.Queue()
threads = []
threadID = 1

# Create new threads
for r in xrange(n):
    tName="Thread-{}".format(r + 1)
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()

for word in wordList:
    workQueue.put(word)
queueLock.release()



# Wait for queue to empty
while not workQueue.empty():
    pass
# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
    
output_text=open("crypted_%s_%s_%s.txt" %(s,n,l),"w")

crypted_text= ''.join(finalList)
output_text.write(crypted_text)


print "Exiting Main Thread"