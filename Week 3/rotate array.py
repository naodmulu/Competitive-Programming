class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = k % len(nums)
        def rotate(start,end,rlist):
            while start < end:
                rlist[start],rlist[end] = rlist[end],rlist[start]
                end -=1
                start +=1
        rotate(0,len(nums)-1,nums)
        
        rotate (0,i-1,nums)
        
        rotate (i,len(nums)-1,nums)
        