class Solution:
    def intersect(self, nums1, nums2):
        # write your code here 
        intersection = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            if nums1[i] in nums2:
                intersection.append(nums1[i])
                nums2.remove(nums1[i])
        intersection.sort() 
        return intersection
        