process = int(input("how many processes would you like to simulate"))

arrival_time = []

TurnaroundTime = []

for i in process:
    arrival_time[i] = int(input("Indicate arrival time of process"+i+":"))
for i in process:
    TurnaroundTime[i] = int(input("Indicate Turnaround time of process"+i+":"))
algorithm = (input("Which Scheduling algorithm would you like to simulate,type \
          either SJF, Preemptive, or Round Robin only. It's case sensitive"))
if algorithm == "SJF":
    algorithm = "do something"
elif algorithm == "Preemptive":
    algorithm = "do something"
elif algorithm == "RoundRobin":
    algorithm = "do something"