class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index = 0
        output = []
        for i in nums:
            if i == target:
                output.append(index)
            index +=1
        return output 