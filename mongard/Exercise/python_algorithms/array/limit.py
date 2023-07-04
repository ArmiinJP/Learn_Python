# def limit(array, min=None, max=None):
#     result = []
       
#     for num in array:
#         if (min is None) or (num >= min):
#             pass
#         else:
#             continue

#         if (max is None) or (num <= max):
#             result.append(num)
#         else:
#             continue

#     return result

# print(limit([1,2,3,4], 2, 3))


def limit(array, min=None, max=None):
    maxCheck = lambda val: True if max is None else val <= max
    minCheck = lambda val: True if min is None else val >= min

    return([val for val in array if minCheck(val) and maxCheck(val)])


print(limit([1,2,3,4], min=2, max=3))