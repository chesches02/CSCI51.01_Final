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

        

algorithm = (input("Which Scheduling algorithm would you like to simulate,type \n either SJF, Preemptive, or Round Robin only."))
algorithm.lower

if algorithm == "sjf":
    algorithm = "do something"
elif algorithm == "preemptive":
    algorithm = "do something"
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