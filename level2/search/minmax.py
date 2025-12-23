a = int(input())
nums = list(map(int, input().split()))
smallest = nums[0]
largest = nums[0]

for i in range(len(nums)):
    if smallest>=nums[i]:
        smallest = nums[i]
    if nums[i]>=largest: 
        largest = nums[i]
        
print(smallest,largest)