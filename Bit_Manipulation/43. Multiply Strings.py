class Solution(object):
    def multiply(self, num1, num2):
        if num1=="0" or num2=="0": return "0"

        res=[0]*(len(num1)+len(num2))

        num1, num2=num1[::-1],num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1=int(num1[i])
                digit2=int(num2[j])

                res[i+j]+=digit1*digit2
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10

        while res[-1]==0:
            res.pop()

        res=res[::-1]
        return "".join(map(str, res))
