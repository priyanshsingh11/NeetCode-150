class Solution(object):
    def uniquePaths(self, m, n):
        dp={}

        def travel(i,j):
            if i==1 and j==1: return 1
            if i==0 or j==0: return 0
            if (i,j) in dp:
                return dp[(i, j)]

            dp[(i,j)]=travel(i-1,j)+travel(i,j-1)
            return dp[(i,j)]

        return travel(m,n)
