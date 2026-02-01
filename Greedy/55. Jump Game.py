class Solution(object):
    def canJump(self, nums):
        n=len(nums)
        
        ending=n-1

        for i in range(n-2,-1,-1):
            if nums[i]+i>=ending:
                ending=i


        return ending==0
