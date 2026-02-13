class Solution(object):
    def leastInterval(self, tasks, n):
        freq={}

        for task in tasks:
            freq[task]=freq.get(task,0)+1

        maxFreq=max(freq.values())

        maxi=0
        for value in freq.values():
            if value==maxFreq:
                maxi+=1

        result=(maxFreq-1)*(n+1)+maxi

        return max(len(tasks),result)
