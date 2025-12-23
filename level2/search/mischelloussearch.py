n = int(input())
a = []

for i in range(n+1):
    a.append(list(map(int, input().split())))
value = False
for i in range(n):
    if a[n][0] in a[i] and a[n][1] in a[i]:
        value = True
        break
    
if value:
    print("Yes")
else:
    print("No")
