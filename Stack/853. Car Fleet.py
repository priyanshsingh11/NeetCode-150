class Solution(object):
    def carFleet(self, target, position, speed):
        cars=sorted(zip(position,speed),reverse=True)
        stack=[]

        for pos,spe in cars:
            time=(target-pos)/float(spe)

            stack.append(time)

            if len(stack)>=2 and stack[-1]<=stack[-2]: stack.pop()

        return len(stack)
