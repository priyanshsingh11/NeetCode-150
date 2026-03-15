class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[1]*n

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        
        return max(dp)
