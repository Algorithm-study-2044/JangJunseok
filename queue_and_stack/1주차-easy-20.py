class Solution(object):
    def isValid(self, s):
        stack = []
        for item in s:
            if item == "(" or item == "{" or item == "[":
                stack.append(item)
            elif len(stack) == 0:
                return False
            elif item == ")":
                if stack.pop() != "(":
                    return False
            elif item == "}":
                if stack.pop() != "{":
                    return False
            elif item == "]":
                if stack.pop() != "[":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False