for ramz in range(0,100000):
    if ramz // 10 == 0 :
        n="0000" + str(ramz)
    elif ramz // 100 == 0 :
        n="000" + str(ramz)
    elif ramz // 1000 == 0 :
        n="00" + str(ramz)
    elif ramz // 10000 == 0 :
        n="0" + str(ramz)
    elif ramz // 100000 == 0 :
        n= str(ramz)                
    else :
        print("Error")
    
    if (int(n[2])+int(n[4]) == 14 \
        and int(n[0]) + 1 == 2*int(n[1]) \
        and int(n[1]) + 1 == int(n[3]) \
        and int(n[1]) + int(n[2]) == 10 
        and int(n[0])+int(n[1])+int(n[2])+int(n[3])+int(n[4]) == 30):
        print(n)
