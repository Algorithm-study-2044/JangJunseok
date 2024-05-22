# 11:14분. 1차시도 성공. 9ms. 83.85% beats. 

# ] 으로 닫았을때, stack.pop해서, 그 반복횟수만큼 곱해서 res에 더해준다.
# 그런데 문제는, 그 중간 상태같은것도 저장되어야 한다는 것이다.
# 3[a2[c]] 의 사례를 보자.

# 일단 [가 시작되면, 그 stack 안에 문자는 다 집어넣고,
# ]가 나오면, stack에서 pop해서, 숫자만큼 곱해서 res에 더하는 식.

# (3,string), (2,string)
# if ] appears, then pop and multiply string,
# but if stack left, should not added to res
# but to added to the last stack item[1]

# contents를 dfs해서 넣는다?
# [] 안에 있는 내용을 넣어주고, 그 return 값을 multiply해서 return 하는 식으로.
# 근데 이렇게 하면 문제가 됨.

class Solution(object):
    def decodeString(self, s):
        stack = []
        res = ""
        curr_num = 0

        for c in s:
            # 문자인 경우.
            if not c.isdigit():
                if c == "[":
                    stack.append([int(curr_num),""])
                    curr_num = 0
                elif c == "]":
                    n, s = stack.pop()
                    if stack:
                        stack[-1][1] += s * n
                    else:
                        res += s * n
                else:
                    if stack:
                        stack[-1][1] += c
                    else:
                        res += c

            # 숫자인 경우.
            else:
                c = int(c)
                if curr_num:
                    curr_num = curr_num * 10 + c
                else:
                    curr_num = c

        return res