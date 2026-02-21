class Solution(object):
    def checkValidString(self, s):
        left_stack=[]
        star_stack=[]

        for i in range(len(s)):
            if s[i]=='(':
                left_stack.append(i)
            elif s[i]=='*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            
        while left_stack and star_stack:
            if left_stack[-1]<star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                return False
                

        return len(left_stack)==0

# Logic:
# 1. First pass:
#    - If ')', try to match with '(' first.
#    - If no '(', use '*' as '('.
#    - If neither available → return False.
#
# 2. After traversal:
#    - Match remaining '(' with '*' acting as ')'.
#    - '*' must come AFTER '(' → check index order.
#
# 3. If any '(' still remains → invalid.
