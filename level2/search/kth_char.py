s1, c1, k = input().split()
k = int(k)
count = 0
result = -1

for i in range(len(s1)):
    if s1[i] == c1:
        count += 1
        if count == k:
            result = i
            break

print(result)