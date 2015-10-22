#!/usr/bin/python
from multiprocessing import Process, Queue, Lock, Array
import sys



if (len(sys.argv) != 4):
        sys.exit('Usage: sub.py <s> <n> <l> ')

alphabet = list('abcdefghijklmnopqrstuvwxyz')
s,n,l= int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
i,j,wordList,finalList=0,0,[],[]

try:
    output_text=open("crypted_%s_%s_%s.txt" %(s,n,l),"w")
    input_txt=open("metin.txt")
except:
    print "failed ." 


dataList =((input_txt.read()).lower()) 


def encrypt(text_to_encrypt):
        cipher = ''
            
        for c in text_to_encrypt:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)-s)%(len(alphabet))].upper()
            else :
                cipher +=c
        return cipher

def process_data( data):
    while not exitFlag:
        inputqueueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            thread.order = myThread.workorder
            myThread.workorder+=1
            inputqueueLock.release()
            data2=encrypt(data)
            outputqueueLock.acquire()
            output_text.seek(thread.order*l)
            output_text.write(data2)
            outputqueueLock.release()
            
            
            
        else:
            inputqueueLock.release()
        time.sleep(0.1)





while j < int(len(dataList)):
    wordList.append(dataList[j:j+l])
    j+=l


inputqueueLock = threading.Lock()
outputqueueLock = threading.Lock()
workQueue = Queue.Queue()
finalQueue = Queue.Queue()
threads = []
threadID = 1

# Create new threads
for r in xrange(n):
    
    thread = myThread(r, 0, workQueue)
    thread.start()
    threads.append(thread)
    

# Fill the queue
inputqueueLock.acquire()
for word in wordList:
    workQueue.put(word)
inputqueueLock.release()




# Wait for queue to empty
while not workQueue.empty():
    pass
# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
    


#crypted_text= ''.join(finalList)
#output_text.write(crypted_text)
output_text.close()
input_txt.close()


print "Exiting Main Thread"