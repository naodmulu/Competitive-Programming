class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window_start = 0
        max_length = 0
        max_zero_count = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                max_zero_count += 1
            if max_zero_count > 1:
                if nums[window_start] == 0:
                    max_zero_count -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start)
        return max_length