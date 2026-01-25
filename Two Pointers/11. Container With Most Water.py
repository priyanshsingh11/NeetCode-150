class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        ans=0
        n=len(height)

        while (left<right):
            width=right-left
            water=min(height[left],height[right])*(width)
            ans=max(ans,water)

            if (height[right]>height[left]):
                left+=1
            
            else:
                right-=1
            
        return ans

        
