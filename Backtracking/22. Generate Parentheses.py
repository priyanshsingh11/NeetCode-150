class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        
        def backtrack(path, open_bracket, close_bracket):
            if len(path)==2*n:
                res.append(path)
                return

            if open_bracket<n:
                backtrack(path+"(",open_bracket+1,close_bracket)
            
            if close_bracket<open_bracket:
                backtrack(path+")",open_bracket,close_bracket+1)

        backtrack("",0,0)
        return res         
        

# ======================= DRY RUN (n = 3) =======================

# Start:
# backtrack("", 0, 0)

# Add '(' → backtrack("(", 1, 0)
#   Add '(' → backtrack("((", 2, 0)
#       Add '(' → backtrack("(((", 3, 0)
#           Add ')' → backtrack("((()", 3, 1)
#               Add ')' → backtrack("((())", 3, 2)
#                   Add ')' → backtrack("((()))", 3, 3)
#                   ✔ length = 6 → append "((()))"

#       From "((" add ')' → backtrack("(()", 2, 1)
#           Add '(' → backtrack("(()(", 3, 1)
#               Add ')' → backtrack("(()()", 3, 2)
#                   Add ')' → backtrack("(()())", 3, 3)
#                   ✔ append "(()())"

#           From "(()" add ')' → backtrack("(())", 2, 2)
#               Add '(' → backtrack("(())(", 3, 2)
#                   Add ')' → backtrack("(())()", 3, 3)
#                   ✔ append "(())()"

# From "(" add ')' → backtrack("()", 1, 1)
#   Add '(' → backtrack("()(", 2, 1)
#       Add '(' → backtrack("()((", 3, 1)
#           Add ')' → backtrack("()(()", 3, 2)
#               Add ')' → backtrack("()(())", 3, 3)
#               ✔ append "()(())"

#       From "()(" add ')' → backtrack("()()", 2, 2)
#           Add '(' → backtrack("()()(", 3, 2)
#               Add ')' → backtrack("()()()", 3, 3)
#               ✔ append "()()()"

# FINAL RESULT:
# res = ["((()))", "(()())", "(())()", "()(())", "()()()"]
