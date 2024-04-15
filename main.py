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
    timeLeft = []
    processIndex = 0
    currentProcessPointer = 0
    rrq = []
    hasZero = False
    ns = 0
    runningFor = 0

    while(processesLeft > 0):
        print(ns)

        try:
            #take all processes that arrive at this nanosecond and add them to the process queue
            while(pList[processIndex].arrivalTime == ns):
                arrivingProc = pList[processIndex]
                print("     Process "+ str(arrivingProc.id) + " has arrived")
                rrq.append(arrivingProc)
                timeLeft.append(arrivingProc.turnaroundTime)
                processIndex += 1
        except:
            pass

        #handles the process queue
        if len(rrq) > 0:
            #print("runningfor: " + str(runningFor))
            # handle processpointer
            if runningFor == (t_q):
                print("     context switch")
                currentProcessPointer += 1
                currentProcessPointer %= len(rrq)
                runningFor = 1
            else:
                runningFor += 1

            hasZero = False
            # Iterates through every process and either deducts its turnaroundTime or adds its waitingTime
            for i in range(len(rrq)):
                if i == currentProcessPointer:
                    timeLeft[i] -= 1
                    print("     Process "+ str(rrq[i].id) + " ran for 1 ns with " + str(timeLeft[i]) + " ns left")
                    if timeLeft[i] == 0:
                        hasZero = True
                else:
                    print("     Process "+ str(rrq[i].id) + " waited for 1 ns")
                    pList[currentProcessPointer].waitingTime += 1
            
            # find where the zero is when detected
            if hasZero:
                i = 0
                while i < len(rrq):
                    if timeLeft[i] == 0:
                        rrq.pop(i)
                        timeLeft.pop(i)
                        print("     context switch early finish")
                        processesLeft -= 1
                        runningFor = 1
                    else:
                        i += 1

        ns += 1
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