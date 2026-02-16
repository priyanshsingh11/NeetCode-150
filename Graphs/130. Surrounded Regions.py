class Solution(object):
    def solve(self, board):
        m=len(board)
        n=len(board[0])

        vis=[[0]* n for _ in range(m)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or vis[i][j] or board[i][j] != 'O':
                return
            vis[i][j]=1
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+ 1)
            dfs(i,j-1)

        for i in range(m):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][n-1]=='O':
                dfs(i,n-1)

        for j in range(n):
            if board[0][j]=='O':
                dfs(0,j)
            if board[m-1][j]=='O':
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and not vis[i][j]:
                    board[i][j]='X'
            

