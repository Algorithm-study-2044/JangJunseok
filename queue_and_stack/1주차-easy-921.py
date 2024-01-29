#921 10분 소요. pass.

class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        cnt = 0
        for char in s:
            if char == ")" and len(stack) == 0:
                cnt += 1
            elif char == ")":
                stack.pop()
            elif char == "(":
                stack.append("(")
        cnt += len(stack)

        return cnt