class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        m=len(matrix[0])

        def transpose(n,m):
            for i in range(n):
                for j in range(i+1,m):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        transpose(n,m)

        for i in range(n):
            matrix[i].reverse()

        
