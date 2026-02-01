class Solution(object):
    def maxSubArray(self, nums):
        sum=0
        ans=nums[0]

        for i in range(len(nums)):
            sum=max(nums[i],sum+nums[i])
            ans=max(ans,sum)

        return ans
            
