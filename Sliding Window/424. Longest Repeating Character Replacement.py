class Solution(object):
    def characterReplacement(self, s, k):
        n=len(s)
        start=0
        ans=0
        end=0
        count=0
        char_count={}

        while end<n:
            char_count[s[end]]=char_count.get(s[end],0)+1

            count=max(count,char_count[s[end]])

            length=end-start+1
            if (length-count<=k):
                ans=max(ans,length)
            
            else:
                char_count[s[start]]-=1
                start+=1
            
            end+=1
        
        return ans 

            
            
