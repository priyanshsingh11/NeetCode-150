class Solution(object):
    def hammingWeight(self, n):
        count=0
        num=bin(n)[2:]
        
        for i in range(len(num)):
            if num[i]=='1':
                count+=1

        return count
        
