num1=1
num2=2
sum=0
while(num1<4000000 or num2<4000000):
    if (num1%2==0):
        sum+=num1
    if (num2%2==0):
        sum+=num2
    print(f"num1 is : {num1} , num2 is : {num2}")
    num1 = num1+num2 #3,8,21
    num2 = num1+num2 #5,13


print(sum)