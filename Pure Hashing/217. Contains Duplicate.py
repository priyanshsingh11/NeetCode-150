class Solution(object):
    def containsDuplicate(self, nums):
        mapping={}

        for i in range(len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]]+=1
            else:
                mapping[nums[i]]=1

        for num in mapping:
            if mapping[num]>1: return True

        return False

        
