def moveZeros(self, nums):
    write = 0 
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write]=nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums 

