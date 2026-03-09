class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[0]*n

        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-2],dp[i-1])

        return min(dp[n-2],dp[n-1])

        
