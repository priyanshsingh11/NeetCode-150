class Solution(object):
    def countSubstrings(self, s):
        n=len(s)
        count=0

        for start in range(n):
            for end in range(start,n):
                sub=s[start:end+1]
                if sub==sub[::-1]: count+=1

        return count
