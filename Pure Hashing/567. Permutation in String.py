from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        n1=len(s1)
        n2=len(s2)

        if n1>n2: return False

        s1_map=Counter(s1)

        for i in range(n2-n1+1):
            s2_map=Counter(s2[i:i+n1])

            if s1_map==s2_map: return True

        return False

