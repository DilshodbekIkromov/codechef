def bouble_sort(arr):
    n = len(arr)
    for i in len(n-1):
        for j in len(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

