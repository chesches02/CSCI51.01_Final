import time
class process():
    waitingTime = 0
    def __init__(self, id, turnaroundTime, arrivalTime):
        self.id = id
        self.turnaroundTime = turnaroundTime
        self.arrivalTime = arrivalTime
    def __str__(self):
        return self.id

processNum = int(input("how many processes would you like to simulate?: "))
processList = []
processDict = {}

def mergeSort_arrivalTime(proc):
    if len(proc) > 1:
 
         # Finding the mid of the array
        mid = len(proc)//2
 
        # Dividing the array elements
        L = proc[:mid]
 
        # Into 2 halves
        R = proc[mid:]
 
        # Sorting the first half
        mergeSort_arrivalTime(L)
 
        # Sorting the second half
        mergeSort_arrivalTime(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].arrivalTime <= R[j].arrivalTime:
                proc[k] = L[i]
                i += 1
            else:
                proc[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            proc[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            proc[k] = R[j]
            j += 1
            k += 1
    return proc




#inputting each process
for i in range(processNum):
    arrival_time = int(input("Indicate arrival time of process "+str(i+1)+" (ns): "))
    turnaround_time = int(input("Indicate Turnaround time of process "+str(i+1)+" (ns): "))
    p = process(i, turnaround_time, arrival_time)
    processList.append(p)
    processDict[str(p.id)] = p
    print("===========================================")

print("Processes")
for i in range(processNum):
    print("Process "+str(processList[i].id)+" A_t: "+ str(processList[i].arrivalTime)+" T_t: "+str(processList[i].turnaroundTime))
print("======================================")

def BST_Insert(obj, li5t):

    timeLeft = obj.turnaroundTime

    list_len = len(li5t)
    skip = list_len//2
    pointerIndex = 0

    if (list_len == 0):
        li5t.append(obj)
    elif (timeLeft >= li5t[list_len-1].turnaroundTime):
        li5t.append(obj)
    elif (timeLeft < li5t[list_len-1].turnaroundTime):
        li5t.insert(0, obj)
    else:
        while (not (timeLeft >= li5t[pointerIndex].turnaroundTime and timeLeft < li5t[pointerIndex+1].turnaroundTime)):
        
            if (timeLeft <= li5t[pointerIndex].turnaroundTime):
                pointerIndex += skip
            else:
                pointerIndex -= skip
            skip = (skip // 2) + 1
            

def sjf(pList):
    ns = 0
    #processArrivalQueue = mergeSort_arrivalTime(pList)
    
    print("Processes sorted by arrival time")
    for i in range(processNum):
        print("Process "+str(processList[i].id)+" A_t: "+ str(pList[i].arrivalTime)+" T_t: "+str(pList[i].turnaroundTime))
    print("======================================")
    
    processIndex = 0
    processesLeft = len(pList)
    SJFqueue = []
    isRunning = False
    currentProcess = None
    currentTaskEndsAt = 0
    while (processesLeft > 0):
        try:
            print("ns: " + str(ns) + " nextArrival:" + str(pList[processIndex].arrivalTime) + " currentProcessEnds: " + str(currentTaskEndsAt))
        except:
            print("ns: " + str(ns) + " currentProcessEnds: " + str(currentTaskEndsAt))

        if(len(SJFqueue)>0):
            for p in SJFqueue:
                print("     Process "+str(p.id)+ " is ready")
                p.waitingTime += 1
        try:
            #take all processes that arrive at this nanosecond and add them to the process queue
            while(pList[processIndex].arrivalTime == ns):
                arrivingProc = pList[processIndex]
                print("     Process "+str(arrivingProc.id)+ " has arrived")
                BST_Insert(arrivingProc, SJFqueue)
                print("     Process SJF Queue: " + str([p.id for p in SJFqueue if len(SJFqueue) > 0]))
                processIndex += 1
        except:
            pass
        
        if currentTaskEndsAt == ns and currentProcess != None:
            print("     Process "+str(currentProcess.id)+" has terminated")
            print("     Process SJF Queue: " + str([p.id for p in SJFqueue if len(SJFqueue) > 0]))
            processesLeft -= 1
            isRunning = False

        if not isRunning and len(SJFqueue) > 0:
            currentProcess = SJFqueue.pop(0)
            print("     Process "+str(currentProcess.id)+" is running")
            currentTaskEndsAt = currentProcess.turnaroundTime + ns
            isRunning = True

        ns+=1
        #time.sleep(1)

algorithm = (input("Which Scheduling algorithm would you like to simulate,type \n either SJF, Preemptive, or Round Robin only."))
algorithm.lower
if algorithm == "sjf":
    mergeSort_arrivalTime(processList)
    sjf(processList)
elif algorithm == "preemptive":
    algorithm = "do something"
elif (algorithm == "round robin" or algorithm == "roundrobin"):
    algorithm = "do something"

print("========================================================")
print("SIMULATION TERMINATED. Here are the stats of each process")
for i in range(len(processList)):
    proc = processDict[str(i)]
    print("     Process " + str(i) + " A_t: " + str(proc.arrivalTime) + " T_t: " + str(proc.turnaroundTime) + " W_t: " + str(proc.waitingTime))
print("Here's some stats across all processes")
total_T_t = 0
total_W_t = 0

for p in processList:
    total_T_t += p.turnaroundTime
    total_W_t += p.waitingTime

print("     Total turnaround time: " + str(total_T_t) + " ns")
print("     Total waiting time: " + str(total_T_t) + " ns")
print("")
print("     Average turnaround time: " + str(total_T_t/len(processList)) + " ns")
print("     Average waiting time: " + str(total_T_t/len(processList)) + " ns")
print("========================================================")