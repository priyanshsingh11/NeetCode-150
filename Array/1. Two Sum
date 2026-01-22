class Solution(object):
    def twoSum(self, nums, target):
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()
        n=len(nums)
        
        left=0
        right=n-1

        while (right<=n):
            val=arr[left][0]+arr[right][0]

            if val==target:
                return arr[left][1],arr[right][1]

            elif val<target:
                left+=1
            
            else:
                right-=1

            
