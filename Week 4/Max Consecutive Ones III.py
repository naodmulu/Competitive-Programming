class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        window_start = 0
        max_length = 0
        max_ones_count = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                max_ones_count += 1
            if window_end - window_start + 1 - max_ones_count > k:
                if nums[window_start] == 1:
                    max_ones_count -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
