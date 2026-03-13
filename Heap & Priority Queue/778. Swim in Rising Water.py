import heapq

class Solution(object):
    def swimInWater(self, grid):
        n=len(grid)
        m=len(grid[0])

        heap=[(grid[0][0],0,0)]

        visited={(0,0)}

        res=0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            val,r,c=heapq.heappop(heap)

            res = max(res,val)
            
            if r==n-1 and c==m-1: return res

            for row,col in directions:
                newr=row+r
                newc=col+c

                if 0 <= newr < n and 0 <= newc < n and (newr,newc) not in visited:
                    visited.add((newr,newc))
                    heapq.heappush(heap,(grid[newr][newc],newr,newc))
