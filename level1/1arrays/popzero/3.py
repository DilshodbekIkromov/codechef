def moveZeros(self, nums):
    count = 0 
    i = 0
    while i < len(nums):
        if nums[i]==0:
            count +=1 
            nums.pop(i)
        else: 
            i += 1
        nums += [0]*count 
        return nums 