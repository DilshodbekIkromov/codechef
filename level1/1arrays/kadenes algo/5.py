class Solution:
    def maxSubarray(self, nums):
        maxsum = currsum = 0
        start = end = temp_start = 0

        for i in range(1, len(nums)):
            if currsum + nums[i] < nums[i]:
                currsum = nums[i]
                temp_start =i
            else: 
                currsum += nums[i]
            if currsum > maxsum:
                maxsum = currsum
                start = temp_start
                end =i
        return nums[start:end+1]


