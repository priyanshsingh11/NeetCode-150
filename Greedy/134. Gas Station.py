class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        start=0
        remaining_tank=0
        total_tank=0

        for i in range(n):
            total_tank+=gas[i]-cost[i]
            remaining_tank+=gas[i]-cost[i]

            if remaining_tank<0:
                start=i+1
                remaining_tank=0

        if total_tank>=0: return start
        else: return -1      

            
