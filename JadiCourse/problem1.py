
def mult():
    sum = 0 
    for i in range(1,10000000):
        if (i%3==0 or i%5==0):
            #print(i,end=" , ")
            sum+=i
    
    return sum
print(mult())

# real	0m1.266s
# user	0m1.255s
# sys	0m0.010s

#-------------------------------------

# def zarib(n):
#     if n % 3 == 0 or n % 5 ==0 :
#         return True
#     else :
#         return False

# sum =0
# for i in range (1,10000000):
#     if zarib(i):
#         sum += i

# print(sum)

# real	0m2.846s
# user	0m2 .835s
# sys	0m0.007s