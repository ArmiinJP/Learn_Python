def limit(array, min=None, max=None):
    result = []
       
    for num in array:
        if (min is None) or (num >= min):
            pass
        else:
            continue

        if (max is None) or (num <= max):
            result.append(num)
        else:
            continue

    return result

print(limit([1,2,3,4], 2, 3))