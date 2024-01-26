class Solution(object):
    def firstUniqChar(self, s):
        stack = []
        for_dict = {}
        for char in s:
            if char not in for_dict:
                stack.append(char)
                for_dict[char] = True
            else:
                stack = [item for item in stack if item != char]
        if len(stack) == 0:
            return -1
        else:
            return s.find(stack[0])