import time
import math

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

def roundRobin(pList, t_q):

    print("Processes sorted by arrival time")
    for i in range(processNum):
        print("Process "+str(processList[i].id)+" A_t: "+ str(pList[i].arrivalTime)+" T_t: "+str(pList[i].turnaroundTime))
    print("======================================")

    processesLeft = len(pList)
    processIndex = 0
    timeLeft_all = []
    timeLeft_currentProc = None
    currentProcess = None
    rrq = []
    ns = 0
    runningFor = 0

    while(processesLeft > 0):
        print("ns: " + str(ns))

        try:
            #take all processes that arrive at this nanosecond and add them to the process queue
            while(pList[processIndex].arrivalTime == ns):
                arrivingProc = pList[processIndex]
                rrq.append(arrivingProc)
                timeLeft_all.append(arrivingProc.turnaroundTime)
                print("     Process "+ str(arrivingProc.id) + " has arrived")
                processIndex += 1
        except:
            pass

        #context switching
        if runningFor >= t_q:
            runningFor = 0
            # back to the end of the queue
            rrq.append(currentProcess)
            timeLeft_all.append(timeLeft_currentProc)
            # clear values
            currentProcess = None
            timeLeft_currentProc = None
        
        # get a new process
        if currentProcess == None and len(rrq) > 0:
            currentProcess = rrq.pop(0)
            timeLeft_currentProc = timeLeft_all.pop(0)
            print(f"     Switched to process {currentProcess.id}")

        # run current process
        if currentProcess != None and runningFor < t_q:
            if timeLeft_currentProc == 1:
                #run it one last time and context switch immediately
                print(f"       Process {currentProcess.id} has ran its last nanosecond and will now terminate.")
                currentProcess = None
                timeLeft_currentProc = None
                processesLeft -= 1
                # early context switch agad, get a new process and run it
                if len(rrq) > 0:
                    currentProcess = rrq.pop(0)
                    timeLeft_currentProc = timeLeft_all.pop(0)
                    print(f"     Switched to process {currentProcess.id}")
                    print(f"     Process {currentProcess.id} waited for 1 ns")
                    currentProcess.waitingTime += 1
                runningFor = 0

            else:
                print(f"       Process {currentProcess.id} ran for 1 ns")
                timeLeft_currentProc -= 1
                runningFor += 1

        

        # make all processes in the ready queue wait 1 ns
        for p in rrq:
            print(f"     Process {p.id} waited for 1 ns")
            p.waitingTime += 1
        
        print("process queue: " + str([p.id for p in rrq if len(rrq) > 0]))
        print("Time left: " + str(timeLeft_all))

        ns += 1
        print("============================================")
        #time.sleep(0.5)

        


def BST_Insert(obj, li5t):

    timeLeft = obj.turnaroundTime

    list_len = len(li5t)
    pointerIndex = list_len//2
    skip = pointerIndex // 2

    if skip < 1: 
        skip = 1

    if (list_len == 0):
        li5t.append(obj)
    elif (timeLeft >= li5t[list_len-1].turnaroundTime):
        li5t.append(obj)
    elif (timeLeft <= li5t[0].turnaroundTime):
        pointerIndex = 0

        #honor fcfs
        while (timeLeft == li5t[pointerIndex].turnaroundTime and pointerIndex < list_len):
            pointerIndex += 1
        li5t.insert(pointerIndex, obj)

    else:
        while (not (timeLeft <= li5t[pointerIndex].turnaroundTime and timeLeft > li5t[pointerIndex-1].turnaroundTime)):
        
            if (timeLeft > li5t[pointerIndex].turnaroundTime):
                pointerIndex += skip
            else:
                pointerIndex -= skip
            skip = math.ceil(skip/2)
        
        #honor fcfs
        while (timeLeft == li5t[pointerIndex].turnaroundTime and pointerIndex < list_len):
            pointerIndex += 1

        li5t.insert(pointerIndex, obj)

            
def BST_Insert_2(obj_tl, li5t):

    # li5t contains tuples (obj, timeLeft)
    timeLeft = obj_tl[1]

    list_len = len(li5t)
    pointerIndex = list_len//2
    skip = (pointerIndex // 2) - 1

    if skip < 1:
        skip = 1

    if (list_len == 0):
        li5t.append(obj_tl)
    elif (timeLeft >= li5t[list_len-1][1]):
        li5t.append(obj_tl)
    elif (timeLeft <= li5t[0][1]):
        pointerIndex = 0

        # honor fcfs
        while (li5t[pointerIndex][1] == timeLeft and pointerIndex < list_len):
            pointerIndex += 1

        li5t.insert(pointerIndex, obj_tl)
    else:
        while (not (timeLeft <= li5t[pointerIndex][1] and timeLeft > li5t[pointerIndex-1][1])):
        
            if (timeLeft > li5t[pointerIndex][1]):
                pointerIndex += skip
            else:
                pointerIndex -= skip

            skip = math.ceil(skip/2)

        # honor fcfs
        while (li5t[pointerIndex][1] == timeLeft and pointerIndex < list_len):
            pointerIndex += 1
        
        li5t.insert(pointerIndex, obj_tl)

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

def sjf_preemptive_2(pList):
    ns = 0
    #processArrivalQueue = mergeSort_arrivalTime(pList)
    
    print("Processes sorted by arrival time")
    for i in range(processNum):
        print("Process "+str(processList[i].id)+" A_t: "+ str(pList[i].arrivalTime)+" T_t: "+str(pList[i].turnaroundTime))
    print("======================================")
    
    processIndex = 0
    processesLeft = len(pList)
    SJFpreemptiveQueue = []
    currentProcess = None #formatted as [currentProcess, remainingTime]
    while (processesLeft > 0):
        try:
            print("ns: " + str(ns) + " nextArrival:" + str(pList[processIndex].arrivalTime))
        except:
            print("ns: " + str(ns))

        try:
            #take all processes that arrive at this nanosecond and add them to the process queue
            while(pList[processIndex].arrivalTime == ns):
                arrivingProc = pList[processIndex]
                print("     Process "+str(arrivingProc.id)+ " has arrived")

                #check if it can preempt current process, if it exists
                if currentProcess != None:
                    if arrivingProc.turnaroundTime < currentProcess[1]:
                        print("     Process "+str(arrivingProc.id)+ " is shorter. Proceed to preemption")
                        BST_Insert_2(currentProcess, SJFpreemptiveQueue)
                        print("     BST_insert_2 successful")
                        currentProcess = [arrivingProc, arrivingProc.turnaroundTime]
                    else:
                        print("     No preemption")
                        BST_Insert_2([arrivingProc, arrivingProc.turnaroundTime], SJFpreemptiveQueue)
                        print("     BST_insert_2 successful non preepmtive")
                else:
                    print("     No running process")
                    currentProcess = [arrivingProc, arrivingProc.turnaroundTime]

                print("     Process SJF preemptive Queue: " + str([p[0].id for p in SJFpreemptiveQueue if len(SJFpreemptiveQueue) > 0]))
                print("     Remaining time for each process: " + str([p[1] for p in SJFpreemptiveQueue if len(SJFpreemptiveQueue) > 0]))
                processIndex += 1
        except:
            pass

        # get new process
        if currentProcess == None and len(SJFpreemptiveQueue) > 0:
            currentProcess = SJFpreemptiveQueue.pop(0)
            print("     Process "+str(currentProcess[0].id)+" is running")
        
        #run or terminating processes
        if currentProcess != None:
            currentProcess[1] -= 1
            print("     Process "+str(currentProcess[0].id)+" ran for 1 ns")

            if currentProcess[1] == 0:
                print("     Process "+str(currentProcess[0].id)+" has terminated")
                print("     Process SJF preemptive Queue: " + str([p[0].id for p in SJFpreemptiveQueue if len(SJFpreemptiveQueue) > 0]))
                print("     Remaining time for each process: " + str([p[1] for p in SJFpreemptiveQueue if len(SJFpreemptiveQueue) > 0]))
                currentProcess = None
                processesLeft -= 1

        if(len(SJFpreemptiveQueue)>0):
            for p in SJFpreemptiveQueue:
                print("     Process "+str(p[0].id)+ " is ready")
                p[0].waitingTime += 1


        ns+=1
        #time.sleep(0.5)

algorithm = (input("Which Scheduling algorithm would you like to simulate,type \n either SJF, Preemptive, or Round Robin only."))
algorithm.lower

if algorithm == "sjf":
    mergeSort_arrivalTime(processList)
    sjf(processList)
elif algorithm == "preemptive":
    mergeSort_arrivalTime(processList)
    sjf_preemptive_2(processList)
elif (algorithm == "round robin" or algorithm == "roundrobin"):
    t_quant = int(input("Indicate the time quantum (ns): "))
    mergeSort_arrivalTime(processList)
    roundRobin(processList, t_quant)

print("========================================================")
print("SIMULATION TERMINATED. Here are the stats of each process")
for i in range(len(processList)):
    proc = processDict[str(i)]
    print("     Process " + str(i) + " A_t: " + str(proc.arrivalTime) + " T_t: " + str(proc.turnaroundTime) + " W_t: " + str(proc.waitingTime))
print("\nHere's some stats across all processes")
total_T_t = 0
total_W_t = 0

for p in processList:
    total_T_t += p.turnaroundTime
    total_W_t += p.waitingTime

print("     Total turnaround time: " + str(total_T_t) + " ns")
print("     Total waiting time: " + str(total_W_t) + " ns")
print("")
print("     Average turnaround time: " + str(total_T_t/len(processList)) + " ns")
print("     Average waiting time: " + str(total_W_t/len(processList)) + " ns")
print("========================================================")