class Solution(object):
    def dfs(self,board,word,i,j,k):
        if k==len(word):
            return True

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[k]:
            return False
        
        temp=board[i][j]
        board[i][j]='#'

        found=( self.dfs(board,word,i+1,j,k+1) or
                  self.dfs(board,word,i-1,j,k+1) or
                  self.dfs(board,word,i,j+1,k+1) or
                  self.dfs(board,word,i,j-1,k+1)
        )

        board[i][j]=temp

        return found


    def findWords(self, board, words):
        ans=[]
        m=len(board)
        n=len(board[0])

        for word in words:
            found=False

            for i in range(m):
                for j in range(n):
                    if board[i][j]==word[0]:
                        if self.dfs(board,word,i,j,0):
                            ans.append(word)
                            found=True
                            break
                    
                if found:
                    break

        return ans
