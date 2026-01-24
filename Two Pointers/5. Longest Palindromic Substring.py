
class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        ans=s[0]

        for i in range(n):

            # if (n%2!=0):
                low=i
                high=i
                while(low>=0 and high<n and s[low]==s[high]):
                    length=s[low:high+1]
                    if (len(length)>len(ans)):
                        ans=length
                    low-=1
                    high+=1
            
            # else:
                low=i-1
                high=i
                while(low>=0 and high<n and s[low]==s[high]):
                    length=s[low:high+1]
                    if (len(length)>len(ans)):
                        ans=length
                    low-=1
                    high+=1
            
        
        return ans


