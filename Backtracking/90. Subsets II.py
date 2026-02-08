class Solution(object):
    def subsetsWithDup(self, nums):
        result=[]
        nums.sort()

        def backtrack(index, path):
            result.append(path[:])

            for i in range(index, len(nums)):
                if (i>index and nums[i]==nums[i-1]):
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
        backtrack(0,[])
        return result
