class Solution(object):
    def longestConsecutive(self, nums):
        setofNums=set(nums)
        ans=0

        for num in setofNums:
            if num-1 not in setofNums:
                curr=num
                length=1

                while (curr+1) in setofNums:
                    curr=curr+1
                    length+=1
                
                ans=max(ans,length)

        return ans

# "Start of sequence = no left neighbor"
