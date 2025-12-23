n, k = map(int, input().split())
a =[]
for i in range(n):
    a.append(list(map(int, input().split())))
    
for i in range(n):
    if (a[i][0] + a[i][1]) % k ==0:
        print(f"({a[i][0]}, {a[i][1]})")
        
