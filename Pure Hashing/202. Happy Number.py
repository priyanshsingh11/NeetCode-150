class Solution(object):
    def sumofsquare(self,n):
        output=0

        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        
        return output

    def isHappy(self, n):
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.sumofsquare(n)

            if n==1: return True

        return False
