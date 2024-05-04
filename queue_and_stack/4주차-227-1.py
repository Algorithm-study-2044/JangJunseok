# 465ms. 5% beats. 어떻게 풀기는 했다만...
# 일단은 곱,나눗셈의 경우는 바로 계산해서 넣어주고, +이나 -의 경우에는, 나중에 한꺼번에 계산하는 식으로 풀었다.

import math
from collections import deque

class Solution(object):
    def calculate(self, s):
        back = ""
        stack = []
        before_calc = None
        s = s.strip()
        for i in range(0,len(s)):
            target = s[i]
            try:
                int(target)
                back += target
            except:
                if target == " ": 
                    continue
                    
                stack.append(int(back))

                if before_calc == "*":
                    front = stack.pop()
                    stack.pop()
                    back = stack.pop()
                    stack.append(front*back)
                elif before_calc == "/":
                    front = stack.pop()
                    stack.pop()
                    back = stack.pop()
                    stack.append(int(math.floor(back/front)))

                before_calc = target
                stack.append(target)
                back = ""
            
            if i == len(s) - 1:
                stack.append(int(back))
                if before_calc == "*":
                    front = stack.pop()
                    stack.pop()
                    back = stack.pop()
                    stack.append(front*back)
                elif before_calc == "/":
                    front = stack.pop()
                    stack.pop()
                    back = stack.pop()
                    stack.append(int(math.floor(back/front)))
            
        queue = deque(stack)
        while len(queue) > 1:
            back = queue.popleft()
            cur = queue.popleft()
            front = queue.popleft()
            if cur == "+":
                queue.appendleft(back+front)                    
            elif cur == "-":
                queue.appendleft(back-front)

        return queue[0]
    

# 다른사람의 풀이. 원리는 비슷하다. 그러나 나는 숫자를 만들어서 넣어주는 방식으로 풀었는데, 이 사람은 연산자를 만나면 바로 계산해서 넣어주는 방식으로 풀었다.

class Solution:
    def calculate(self, s: str) -> int:

        # Initialize the stack
        stack = []

        # Append an operand onto the stack based on an operator
        def append(operator, operand):
            if operator == "+":
                stack.append(operand)
            elif operator == "-":
                stack.append(-operand)
            elif operator == "*":
                stack.append(stack.pop() * operand)
            else:
                stack.append(int(stack.pop() / operand))

        # Initialize the current operator and operand
        operator, operand = "+", 0

        # Iterate through all characters in s
        for c in s:

            # If the current character is a digit,
            if c in "0123456789":

                # Append it to the current operand
                operand = operand * 10 + int(c)

            # Elif the current character is a operator,
            elif c in "+-*/":

                # Append the current operand onto the stack
                append(operator, operand)

                # Update the current operand and operator
                operator, operand = c, 0

        # Add the last operand onto the stack
        append(operator, operand)

        # Return the sum of all operands as the result
        return sum(stack)
    




import math
from collections import deque

class Solution(object):
    def calculate(self, s):
        back = ""
        stack = []
        before_calc = None
        s = s.strip()
        for i in range(0,len(s)):
            target = s[i]
            try:
                int(target)
                back += target
            except:
                if target == " ": 
                    continue
                    
                if before_calc == "*":
                    front = stack.pop()
                    stack.append(front*back)
                elif before_calc == "/":
                    front = stack.pop()
                    stack.append(int(math.floor(front/back)))
                elif before_calc == "-":
                    stack.append(-back)
                else:
                    stack.append(back)

                before_calc = target
                back = ""
            
            if i == len(s) - 1:
                if before_calc == "*":
                    front = stack.pop()
                    stack.append(front*back)
                elif before_calc == "/":
                    front = stack.pop()
                    stack.append(int(math.floor(back/front)))
                elif before_calc == "-":
                    stack.append(-back)
                else:
                    stack.append(back)
            
        return sum(stack)