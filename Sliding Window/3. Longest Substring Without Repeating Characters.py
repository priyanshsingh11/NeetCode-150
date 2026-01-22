class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        mapping= set()
        ans=0

        while (right<len(s)):
            if s[right] not in mapping:
                mapping.add(s[right])

                ans=max(ans,right-left+1)
                right+=1
            
            else:
                mapping.remove(s[left])
                left+=1
        return ans
