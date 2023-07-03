#link: https://www.mongard.ir/one_part/1/python-lambda/

def add1(x, y): return x + y

add2 = lambda x, y: x + y   #automatic return

print(add1(2, 5))
print(add2(2, 5))

#-----------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]

def multi(i):
    return i * i

print(list(map(multi, nums)))


print(list(map(lambda x: x*x, nums))) #use lambda
#-----------------------------------------------------------------
# در این نمونه ترجیح بر استفاده از :
# list comperhension هست

def even(i):
    if i % 2 == 0:
        return True
    return False

print(list(filter(even, nums)))


print(list(filter(lambda x: True if x % 2 == 0 else False, nums))) #use lambda
print(list(filter(lambda x: x % 2 == 0, nums))) #use lambda


# link: list comperhension: https://www.mongard.ir/one_part/14/list-comprehension-python/
print([i for i in nums if i % 2 == 0]) # use list comperhension

#-----------------------------------------------------------------

li = [(4, 'b'), (2, 'a'), (5, 'c'), (1, 'e'), (3, 'd')]
 
print(sorted(li)) #sort with number
print(sorted(li, key=lambda x: x[0])) #sort with number
print(sorted(li, key=lambda x: x[1])) #sort with alphabetic