#4주차. 다른사람의 풀이 연구.

# 연산자가 나오면, 일단 계산해야 하는 상황이다. 다만 그 연산자가 아니라, 그 이전것까지를.
# 그리고 똑똑하게 생각히보면, 숫자가 처음 나왔을때도, 그냥 0 + 숫자로 생각하면 따로 예외케이스를 만들 필요가 없다.

def calculate(self, s):
    if not s:
        return "0"
    stack, num, sign = [], 0, "+"
    for i in xrange(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i])-ord("0")
        # 원래는 그 다음 연산자가 나왔을때 a ? b 를 계산하지만, index가 마지막이면 그 다음 연산자가 없으므로 or 도 붙여줘야 한다.
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                #이건 머지>???
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0
    return sum(stack)



#4주차. 실패.
#2차시도. 실패. 이게 빼는 순서도 상관이 있는것같은데. 정확히 어떻게 되는건지.
#일단 나의 풀이.

class Solution(object):
    def calc(self, a,b, op):
        res = 0
        if op == "+":
            res = a+b
        elif op == "-":
            res = a-b
        elif op == "*":
            res = a*b
        elif op == "/":
            res = a//b
        return res

    def makeItArr(self,s):
        curr = 0
        res = []
        for char in s:
            try:
                next = int(char)
                curr = curr * 10 + next
            except:
                res.append(curr)
                curr = 0
                res.append(char)
        res.append(curr)
        return res

    def calculate(self, s):
        s = s.replace(" ","")
        arr = self.makeItArr(s)
        cur_a = 0
        cur_op = None
        queue = []
        for idx in range(len(arr)):
            char = arr[idx]
            print(cur_a)
            if char == " ":
                continue
            try: 
                next = int(char)
                if not cur_op:
                    cur_a = next
                else:
                    if (idx == len(arr) - 1) or not (( cur_op == '+' or cur_op == '-') and (arr[idx+1] == '*' or arr[idx+1] == '/')): 
                        cur_a = self.calc(cur_a,next,cur_op)
                        cur_op = None
                    else:
                        queue.append([cur_a, cur_op])
                        cur_a = next
            except:
                cur_op = char

        for q in queue:
            cur_a = self.calc(q[0],cur_a, q[1])
        
        return cur_a