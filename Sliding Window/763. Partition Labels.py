class Solution(object):
    def partitionLabels(self, s):
        # n=len(s)
        left=0
        right=0
        ans=[]

        last={c:i for i,c in enumerate(s)}

        for i,c in enumerate(s):
            right=max(right,last[c])

            if i==right:
                ans.append(i-left+1)
                left=right+1
        
        return ans



