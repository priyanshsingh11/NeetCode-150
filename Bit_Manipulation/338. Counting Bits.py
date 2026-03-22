class Solution(object):
    def countBits(self, n):
        ans=[0]*(n+1)

        for i in range(1,n+1):
            ans[i]=ans[i>>1]+(i&1)
            # take the same type smaller number and add the last bit of the current number 
        return ans
        
