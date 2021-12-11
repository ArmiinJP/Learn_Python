import random
def beshkan(n):
    for i in list(status.keys()):
        print(f"alan {i} entekhab shode")
        kandid = random.choice(list(status.keys()))
        while(kandid == i):
            kandid = random.choice(list(status.keys()))
        status[kandid]+=1
        status[i]-=1
        if(status[i]==0):
            status.pop(i)
n=10
pul = 100
status = {}
for i in range(n):
    status[i]=100

for i in range(1000000):
    beshkan(n)

print(status)
