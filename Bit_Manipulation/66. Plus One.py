class Solution(object):
    def plusOne(self, digits):
        extra=1
        n=len(digits)

        for i in range(n-1,-1,-1):
            num=digits[i]+extra
            digits[i]=num%10
            extra=num//10

        if extra:
            digits.insert(0,extra)

        return digits
