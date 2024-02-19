#4주차. 실패. 이렇게 하니까 여러 숫자의 경우 해답이 안됨. re.split같은걸로 분리가 되나?

class Solution(object):

    def calc(self, a,b, op):
        res = 0
        print("calc",a,b,op)
        if op == "+":
            res = a+b
        elif op == "-":
            res = a-b
        elif op == "*":
            res = a*b
        elif op == "/":
            res = a//b
        return res

    def calculate(self, s):
        s = s.replace(" ","")
        arr = list(s)
        cur_a = 0
        cur_op = None
        queue = []
        for idx in range(len(arr)):
            char = arr[idx]
            if char == " ":
                continue
            try: 
                next = int(char)
                print("next",next)
                if not cur_op:
                    cur_a = next
                else:
                    if idx == len(arr) - 1 or not (( cur_op == "+" or cur_op == "-") and arr[idx+1] == "*" or arr[idx+1] == "/"):
                        # 이 경우에는 그냥 계산.
                        cur_a = self.calc(cur_a,next,cur_op)
                        cur_op = None
                    else:
                        queue.append([cur_a, cur_op])
                        cur_a = next
            except:
                cur_op = char
                print("cur_op",char)


        for q in queue:
            cur_a = self.calc(cur_a, q[0], q[1])
        
        return cur_a