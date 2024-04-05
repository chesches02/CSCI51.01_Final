
class process():
    def __init__(self, turnaroundTime, arrivalTime):
        self.turnaroundTime = turnaroundTime
        self.arrivalTime = arrivalTime

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
if algorithm == "sjf":
    algorithm = "do something"
elif algorithm == "preemptive":
    algorithm = "do something"
elif (algorithm == "round robin" or algorithm == "roundrobin"):
    algorithm = "do something"
