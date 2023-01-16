class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        how_many_number = [0] * len(nums)
        for x in range(len(nums)):
            for y in range(len(nums)):
                if y == x:
                    continue
                elif nums[x]>nums[y]:
                    how_many_number[x] +=1
        return how_many_number