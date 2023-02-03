class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1,p2 = 0,0
        
        while p2 <= len(nums)-1:
            if nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            elif nums[p2] != 0:
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p1 +=1
                p2 = p1