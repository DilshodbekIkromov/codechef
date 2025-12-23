n, k = map(int, input().split())
nums = list(map(int, input().split()))
smallest = abs(k-nums[0])
result=0
for i in range(n):
    if abs(k-nums[i])<smallest:
        smallest=abs(k-nums[i])
        result=i
print(nums[result])
        