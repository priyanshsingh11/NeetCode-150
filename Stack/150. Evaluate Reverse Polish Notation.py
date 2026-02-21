class Solution(object):
    def evalRPN(self, tokens):
        stack=[]

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
            
            else:
                b=stack.pop()
                a=stack.pop()

                if token=="+":
                    stack.append(int(a+b))
                elif token=="-":
                    stack.append(int(a - b))
                elif token=="*":
                    stack.append(int(a * b))
                else: 
                    stack.append(int(float(a)/b))

        return stack[0] 
        
