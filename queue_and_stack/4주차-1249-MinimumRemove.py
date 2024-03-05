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
    


#4주차. 다른 사람의 풀이 연구.
    
# 이렇게 하면 s를 두번 iterate하는게 아니라, 없애야 하는 부분의 idx만 찾은다음에,
# 그것들을 없애고 join해주면 된다.
    
class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        arr = list(s)
        for idx,char in enumerate(arr):
            if char == "(":
               stack.append(idx)
            elif char == ")":
                if len(stack) == 0:
                    arr[idx] = ""
                else:
                    stack.pop() 
        for i in stack:
            arr[i] = ""
        
        return "".join(arr)