class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def product(nums):
            p = 1
            for n in nums:
                p *= n
            return p
        if 0 in nums:
            if nums.count(0) > 1:
                return [0] * len(nums)
            else:
                i = nums.index(0)
                return [0] * i + [product(nums[:i] + nums[i+1:])] + [0] * (len(nums) - i - 1)
        else:
            p = product(nums)
            return [p / n for n in nums]