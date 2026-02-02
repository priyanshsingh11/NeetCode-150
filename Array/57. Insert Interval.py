class Solution(object):
    def insert(self, intervals, newInterval):
        
        ans=[]

        for i in intervals:
            if i[1]<newInterval[0]:
                ans.append(i)

            elif i[0]>newInterval[1]:
                ans.append(newInterval)
                newInterval=i

            else:
                newInterval[0]=min(i[0],newInterval[0])
                newInterval[1]=max(i[1],newInterval[1])
                
        ans.append(newInterval)

        return ans
