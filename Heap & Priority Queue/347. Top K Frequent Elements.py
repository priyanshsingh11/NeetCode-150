import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq=Counter(nums)

        max_heap=[]
        ans=[]

        for num,count in freq.items():
            heapq.heappush(max_heap,(-count,num))

        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        
        return ans
