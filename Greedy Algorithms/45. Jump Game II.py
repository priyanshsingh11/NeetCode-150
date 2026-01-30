class Solution(object):
    def jump(self, nums):
        n=len(nums)
        ans=0
        end=0
        far=0

        for i in range(n-1):
            far=max(far,nums[i]+i)

            if i==end: #this gives the jump as we count the jump after its iteration
                ans+=1

                end=far

        return ans
