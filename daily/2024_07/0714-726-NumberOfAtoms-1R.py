# 11:20, isUpper

# 숫자가 여러자리수인경우를 배제해서 생각해서 못풀었음.
# 그런데 그거 넣으면 복잡해지지 않나.

# 이것도 stack문제. 
# 대문자 들어오고, 그 다음에 소문자? 합친다.
# 대문자 들어오고, 그 다음에 대문자? 그러면 분리
# 대문자 들어오고, 숫자? 그러면 곱한다.

# 소문자 뒤에 소문자? 합친다
# 소문자 뒤에 숫자? 곱한다
# 소문자 뒤에 대문자? 빈도수1로 분리한다.

# ( 나오면 스택에 집어넣고, )가 나오면 이제 다음 숫자만큼 안의 빈도를 따블 한담에 이전 스택에 집어넣는다.
# [[[H,2],[]],[[O,2],[K,4]]] 이렇게 한다음에, 하나씩 뽑아서 두번째 요소만 *2 해준다.
# 마지막에는 dictionary에 다 넣어준다? 굳이 그럴 필요 있나 마지막 stack만 가지고.

class Solution:


    def countOfAtoms(self, formula: str) -> str:

        stack = [[]]
        curr = ""
        curr_cnt = 1
        flag = False

        for c in formula:
            if c == "(" or c == ")":
                if c == "(":
                    if curr != "":
                        stack[-1].append([curr,curr_cnt])
                    curr = ""
                    curr_cnt = 1
                    stack.append([])
                else:
                    flag = True
                    if curr != "":
                        stack[-1].append([curr,curr_cnt])
                    curr = ""
                    curr_cnt = 1      
            else:
                try:
                    # 그리고 숫자가 여러숫자일 수 있다.                        
                    if flag:
                        dd = int(c)
                        popped = stack.pop()
                        for item in popped:
                            # 여기서 *= 실수함.
                            item[1] = item[1] * dd
                        stack[-1].extend(popped)
                        flag = False
                    else:
                        curr_cnt = int(c)
                except:
                    # 이럼 문자임.
                    if c.isupper():
                        if curr != "":
                            stack[-1].append([curr,curr_cnt])
                        curr = c
                        curr_cnt = 1
                    else:
                        # 소문자가 들어온다? 
                        curr += c
        
        if curr != "":
            stack[-1].append([curr,curr_cnt])

        res = defaultdict(int)
        for item in stack[-1]:
            res[item[0]] += item[1]
        
        ans = ""
        for chr,num in sorted(res.items(),key=lambda x:x[0]):
            ans += chr
            if num > 1:
                ans += str(num)
        
        return ans
    

# 그래서 이렇게 idx로 하는 방법이 있기는 한데..

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [[]]
        curr = ""
        curr_cnt = 1
        flag = False
        num = 0

        i = 0
        n = len(formula)

        while i < n:
            c = formula[i]

            if flag and not c.isdigit():
                popped = stack.pop()
                for item in popped:
                    item[1] *= num
                stack[-1].extend(popped)
                num = 0
                flag = False

            if c == "(" or c == ")":
                if c == "(":
                    if curr != "":
                        stack[-1].append([curr, curr_cnt])
                    curr = ""
                    curr_cnt = 1
                    stack.append([])
                else:
                    print("yea flag")
                    flag = True
                    if curr != "":
                        stack[-1].append([curr, curr_cnt])
                    curr = ""
                    curr_cnt = 1
                i += 1
            elif c.isdigit():
                num_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                num = int(formula[num_start:i])
                # 이거는 )뒤에 숫자가 나오고 나서의 이야기였음,
                # 그런데 그 숫자가 끝나는게. 
                curr_cnt = num
            else:
                if c.isupper():
                    if curr != "":
                        stack[-1].append([curr, curr_cnt])
                    curr = c
                    curr_cnt = 1
                else:
                    curr += c
                i += 1

        if curr != "":
            stack[-1].append([curr, curr_cnt])

        res = defaultdict(int)
        print(stack)
        for item in stack[-1]:
            print(item[0])
            res[item[0]] += item[1]

        ans = ""
        for chr, num in sorted(res.items(), key=lambda x: x[0]):
            ans += chr
            if num > 1:
                ans += str(num)

        return ans