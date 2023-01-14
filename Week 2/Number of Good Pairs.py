class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        for x in range(len(nums)):
            for y in range(len(nums)-1):
                if y == x:
                    break
                elif nums[y] == nums[x]:
                    i +=1
        return i