class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n % 2)
        count = collections.Counter()
        res = 0
        for p in prefix:
            res += count[p]
            count[p + k] += 1
        return res