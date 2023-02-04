class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_of_arr = sum(nums)
        l = 0
        for n in range(len(nums)):
            r = sum_of_arr - l - nums[n]
            if l == r:
                return n
            l = l + nums[n]
        return -1