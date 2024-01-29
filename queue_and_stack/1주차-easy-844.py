
class Solution(object):

    def return_string(self,s):
        stack = []
        for ch in s:
            if ch == "#":
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

    def backspaceCompare(self, s, t):
        str1 = self.return_string(s)
        str2 = self.return_string(t)
        return str1 == str2