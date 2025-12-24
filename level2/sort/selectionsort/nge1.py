def next_greater_elements(arr):
    n = len(arr)
    nge = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break

    print(" ".join(map(str, nge)))


n = int(input())
arr = list(map(int, input().split()))

next_greater_elements(arr)
