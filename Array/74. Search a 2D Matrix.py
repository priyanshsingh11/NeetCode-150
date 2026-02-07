class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])

        start=0
        end=n-1

        while(start<m and end>=0):
            if (matrix[start][end]==target): return True
            elif (matrix[start][end]>target):
                end-=1
            else:
                start+=1
        
        return False
        
