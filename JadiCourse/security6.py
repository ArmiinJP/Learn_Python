
"""
HOW TO SOLVE :
اول رمز را دادم به معکوس تابع زیکزاکی که پیاده سازی کردم
سپس دادمش به معکوس تابع جابه جایی بر اساس شماره ستون که پیاده سازی کرده بودم
و در نهایت هم دادم به معکوس تابع جمعی 

در این میان برای حالت های مختلف ۲ و ۳ و ۵ و ۷ 
تست کردم که خب برای جابه جایی به کلید ۵ و برای جمعی به کلید ۳ رسیدم

COPYRIGHT : ArminJP
"""
import time
import math

#cypher = "dulpjfopuhoiszfbpduvpvcemsfbp" #2 jami
#cypher = "ctkoienotgnhryeaoctuoubdlreao" #3 jami
#cypher = "arimgclmrelfpwcymarsmszbjpcym" #5 jami
#cypher = "ypgkeajkpcjdnuawkypqkqxzhnawk" #7 jami

#cypher = "fdwrnfrwlxhrqxrewgjoqukhudbrh" #2 perimit
#cypher = "fqrwkxnuerbglhohduqrhrfdwwrjx" #3 perimit
#cypher = "fquwowrbxunwhrhrjdxdlqrerhkfg" #5 perimit
#cypher = "fhjbfxuwqqhwehnrkdxgdrwurrorl" #7 perimit

#cypher = "tqnxvloxqdomyjlbxtqzxzkcwylbx" #3 zarbi
#cypher = "buntxrytuhycevrltbuptpgwierlt" #5 zarbi
#cypher = "xsnvjbgvsfguopbtvxshvhimcobtv" #7 zarbi
#cypher = "ponzhvwzobweidvjzporzrmsqivjz" #9 zarbi
#cypher = "jynpzxipyliskhxvpjyfpfcqukxvp" #15 zarbi
#cypher = "zgnhdjchgtcywfjphzglhlueswjph" #21 zarbi

#cypher = "fedwwgrjnofqruwklhxuhdrbqrxhr" #2 perimit - zikzak
#cypher = "fhqdruwqkrxhnrufedrwbwgrljhxo" #3 perimit - zikzak
cypher = "frqjudwxodwlrqbrxeurnhwkhfrgh" #5 perimit - zikzak
#cypher = "ffxxguddrhrjkbwwreohrrlqwquhn" #7 perimit - zikzak

#cypher = "fdwrnfrwlxhrqxrewgjoqukhudbrh" #after zikzak
#cypher = "fwnrlhqrwjqkubhdrfwxrxegouhdr"

def test_shift_cypher(key ,round):
    tmp_cypher = cypher
    tmp_plain = ""
    for i in range(round):
        for char in tmp_cypher:
            new_char = chr((ord(char)-97-key)%26+97)
            #print(new_char)
            if new_char >= "a" :
                tmp_plain+=new_char
            else :
                return "Invalid" 
        tmp_cypher = tmp_plain
        tmp_plain = ""
    plain = tmp_cypher
    return plain


def test_mult_cypher(key ,round):
    tmp_cypher = cypher
    tmp_plain = ""
    for i in range(round):
        for char in tmp_cypher:
            new_char = chr(((ord(char)-97)*key)%26+97)
            #print(new_char)
            if new_char >= "a" :
                tmp_plain+=new_char
            else :
                return "Invalid" 
        tmp_cypher = tmp_plain
        tmp_plain = ""
    plain = tmp_cypher
    return plain


def test_permit_cypher(key):
    column = key
    cypher_len = len(cypher)
    mod = cypher_len % key
    row = cypher_len // key
    
    if mod != 0 :
        row += 1
    
    board = []
    for i in range(row):
        board.append([])

    row_number = 0
    test_max = 0
    for i in cypher:
        board[row_number].append(i)
        row_number += 1
        if row_number == row-1 :
            test_max += 1
            if test_max > mod :
                row_number += 1
        if row_number == row :
            row_number = 0
    #print(board)
    
    tmp_plain = ""
    for row_list in board:
        for char in row_list :
            tmp_plain += char

    return tmp_plain


def test_zikzak():
    part1_len = math.ceil(len(cypher)/2)
    part2_len = len(cypher) - part1_len

    part1=""
    part2=""
    counter = 0
    for char in cypher:
        if counter < part1_len :
            part1+=char
        else :
            part2+=char
        counter+=1

    tmp_plain = ""
    if part1_len == part2_len :
        for i in range(part1_len):
            tmp_plain+=part1[i]
            tmp_plain+=part2[i]
    else :
        for i in range(part1_len):
            if i == part1_len-1:
                tmp_plain+=part1[i]
            else:
                tmp_plain+=part1[i]
                tmp_plain+=part2[i]
    
    return tmp_plain


def chand_bar_shift(round):
    print(f"---------------------------------------------------------------------{round} round")
    for i in range(26):
        if i in [2 ,3 ,5 ,7] :
            print(f"with key : {i} and {round} round, the result is : {test_shift_cypher(i,round)}")
            #time.sleep(2)


def chand_bar_mult(round):
    invalid_key=[1 ,3 ,5 ,7 ,9 ,11 ,15 ,17 ,19 ,21 ,23 ,25]
    print(f"---------------------------------------------------------------------{round} round")
    for i in invalid_key:
        if i == 1 : # i^-1 == 1
            print(f"with key : {1} and {round} round, the result is : {test_mult_cypher(1,round)}")
        elif i == 3 : # i^-1 == 9
            print(f"with key : {3} and {round} round, the result is : {test_mult_cypher(9,round)}")
        elif i == 5 : # i^-1 == 21
            print(f"with key : {5} and {round} round, the result is : {test_mult_cypher(21,round)}")
        elif i == 7 : # i^-1 == 15
            print(f"with key : {7} and {round} round, the result is : {test_mult_cypher(15,round)}")
        elif i == 9 : # i^-1 == 3
            print(f"with key : {9} and {round} round, the result is : {test_mult_cypher(3,round)}")                        
        elif i == 11 : # i^-1 == 19
            print(f"with key : {11} and {round} round, the result is : {test_mult_cypher(19,round)}")        
        elif i == 15 : # i^-1 == 7
            print(f"with key : {15} and {round} round, the result is : {test_mult_cypher(7,round)}")
        elif i == 17 : # i^-1 == 23
            print(f"with key : {17} and {round} round, the result is : {test_mult_cypher(23,round)}")
        elif i == 19 : # i^-1 == 11
            print(f"with key : {19} and {round} round, the result is : {test_mult_cypher(11,round)}")                    
        elif i == 21 : # i^-1 == 5
            print(f"with key : {21} and {round} round, the result is : {test_mult_cypher(5,round)}")            
        elif i == 23 : # i^-1 == 17
            print(f"with key : {23} and {round} round, the result is : {test_mult_cypher(17,round)}")  
        elif i == 25 : # i^-1 == 25
            print(f"with key : {25} and {round} round, the result is : {test_mult_cypher(25,round)}")            
        else :
            print("error")    


def print_permit(round):
    print(f"---------------------------------------------------------------------{round} round")
    for i in [2 ,3 ,5 ,7]:
        print(f"with key : {i} and {round} round, the result is : {test_permit_cypher(i)}")
        #time.sleep(2)



print(chand_bar_shift(1))
# print(chand_bar_shift(3))
# print(chand_bar_shift(5))
# print(chand_bar_shift(7))

#print(chand_bar_mult(1))
# print(chand_bar_mult(3))
# print(chand_bar_mult(5))
# print(chand_bar_mult(2))

#print(print_permit(1))

#print(test_zikzak())
