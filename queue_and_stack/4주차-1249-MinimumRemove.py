#4주차. 2634ms. 5% beats. 다른 풀이로 풀어볼것.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        # 1. 필요없는 )를 버리는 작업.
        # 2. 필요없는 (를 버리는 작업.
    
        leftCount = 0
        rightCount = 0
        temp = ""
        res = ""
        for char in s:
            if char == ")":
                if leftCount >= 1:
                    leftCount -= 1
                    rightCount += 1
                    temp += char
            elif char == "(":
                leftCount += 1
                temp += char
            else:
                temp += char
        
        for char in temp:
            if char == "(":
                if rightCount >= 1:
                    rightCount -= 1
                    res += char
            else:
                res += char
        
        return res