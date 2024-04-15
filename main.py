
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

#inputting each process
for i in range(processNum):
    arrival_time = int(input("Indicate arrival time of process "+str(i+1)+" (ns): "))
    turnaround_time = int(input("Indicate Turnaround time of process "+str(i+1)+" (ns): "))
    p = process(turnaround_time, arrival_time)
    processList.append(p)
    print("===========================================")

print("Processes")
for i in range(processNum):
    print("Process "+str(i+1)+" A_t: "+ str(processList[i].arrivalTime)+" T_t: "+str(processList[i].turnaroundTime))
print("======================================")
algorithm = (input("Which Scheduling algorithm would you like to simulate,type \n either SJF, Preemptive, or Round Robin only."))
algorithm.lower

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
    pass

if algorithm == "sjf":
    algorithm = "do something"
elif algorithm == "preemptive":
    algorithm = "do something"
elif (algorithm == "round robin" or algorithm == "roundrobin"):
    t_quant = int(input("Indicate the time quantum "+str(i+1)+" (ns): "))
    roundRobin(processList, t_quant)
    
