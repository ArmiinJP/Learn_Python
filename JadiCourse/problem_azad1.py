import random
def beshkan(n):
    for i in range(len(status)):
        if(status[i]=="NULL"):
            continue
        kandid = random.choice(range(n))
        while(kandid == i or status[kandid]=="NULL"):
            kandid = random.choice(range(n))
        status[kandid]+=1
        status[i]-=1
        if(status[i]==0):
            status[i]="NULL"

n=10
pul = 100
status = []
for i in range(n):
    status.append(pul)

for i in range(10000):
    beshkan(n)

print(status)
print(status.count("NULL"))
