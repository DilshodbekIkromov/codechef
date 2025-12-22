class Solution:
    def maxSubarray(self, nums):
        max_sum = current_sum = 0
        start = end = temp_start = 0

        for i in range(1, len(nums)):
            if current_sum + nums[i] < nums[i]:
                current_sum = nums[i]
                temp_start = i
            else: 
                current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
                start =temp_start
                end=i
        return nums[start:end+1]
    