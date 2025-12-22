def find_dishes(arr, n):
    threshold = n // 3 
    result = []

    for dish in set(arr):
        if arr.count(dish) > threshold:
            result.append(dish)
    result.sort()
    return result