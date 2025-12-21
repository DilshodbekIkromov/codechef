class Solution: 
    def findLeaders(self, nums):
        n = len(nums)
        leaders = []
        max = nums[-1]
        leaders.append(nums[-1])

        for i in range(n-2, -1 , -1):
            if nums[i]>max:
                leaders.append(nums[i])
                max = nums[i]
        leaders.reverse()
        return leaders
    
