from collections import Counter

nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9]

def create_dict_frequent(array):
    frequent = {}

    for num in array:
        if frequent.get(num):
            frequent[num] += 1
        else:
            frequent[num] = 1
    
    return frequent


def topOne(array):

    # i have implementiation
    frequent = create_dict_frequent(array)
    # or user std library
    # frequent = Counter(array)

    result = []
    max_frequent = 0
    for key, value in frequent.items():
        if value > max_frequent:  
            result.clear()
            result.append(key)
            max_frequent = value
        elif value == max_frequent:
            result.append(key)
        else:
            pass
    
    return result, max_frequent

print(topOne(nums))


