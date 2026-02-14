class Solution(object):
    def numDistinct(self, s, t):
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

        # important step to initialise the dp laste element as 1 in the j section else the answer is always as 0
        for i in range(len(s)+1):
            dp[i][len(t)]=1     

        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j]=dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j]

        return dp[0][0]
