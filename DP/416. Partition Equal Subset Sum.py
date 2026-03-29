class Solution(object):
    def canPartition(self, nums):
        total=sum(nums)
        dp=[False]*(total+1)
        target=total//2

        if total%2!=0: return False

        dp[0]=True

        for num in nums:
            for curr in range(target,num-1,-1):
                # check for the number smaller than that in the array if found then it can make it happen or not if yes then true else false .. a bit memo type
                dp[curr]=dp[curr] or dp[curr-num]   


        return dp[target]    
