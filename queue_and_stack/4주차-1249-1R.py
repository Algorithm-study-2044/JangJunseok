#8:33 다른 사람의 풀이를 참고함.
# stack에 ) 먼저 들어가면 안된다.
# 무조건 (가 있어야지 가능.
# 그러면 stack에 (만 넣는다? 
# 문제는 뭐냐하면. )는 괜찮은데, 먼저 넣은 (는 어떻게 하냐는 것.
# 넣었는데 나중에 짝이 없어버리면 안되잖아.

# 이것까지는 괜찮았는데, 결국 남아있는 (를 어떻게 처리할지가 막혔었음.
# 다른 사람의 풀이를 참고했는데, 결국 남아있는 stack의 경우 idx가 있을거니까.
# 그 idx들을 제거해주면 된다.

# 나는 전에 엥? 문자열에서 제거해줄 수 있나? 했었는데, 가능하다.
# 그냥 list로 바꿔서, idx를 찾아서 제거해주면 된다.
# 그리고 join으로 다시 문자열로 바꿔주면 된다.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        arr = list(s)
        for idx,c in enumerate(s):
            if c == "(":
                stack.append(idx)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    #이러면 )가 먼저 들어간거니까.
                    #없어지는게 맞음.
                    arr[idx] = ""
        
        for idx in stack:
            arr[idx] = ""

        return "".join(arr)