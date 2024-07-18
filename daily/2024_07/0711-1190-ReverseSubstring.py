# 4:53 30분 소요.
# 42ms. 14.70% beats.

class Solution:
    def reverseParentheses(self, s: str) -> str:

        total = 0
        for c in s:
            if c == "(":
                total += 1
        
        u_stack = [""] * (total+1)
        level = 0

        for c in s:
            if c == "(":
                level += 1
            elif c == ")":
                dropped = u_stack[level]
                u_stack[level-1] += dropped[::-1]
                u_stack[level] = ""
                level -= 1
            else:
                u_stack[level] += c
        
        return u_stack[0]
            