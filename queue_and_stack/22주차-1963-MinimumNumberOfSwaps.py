# 일단 정상적인거는 다 빼주고, 그럼에도 남는 [의 경우에는 바꿔줘야 하니까
# [[[ 가 나왔을때, 왜 len(stk) + 1 // 2가 정답이 되냐면.
# 2개라고 하면, 하나만 바꿔주면 될거고.
# 3개면. 두개
# 4개면. -> 두개
# 5개면. 3개.
# 이거에 맞추려고

class Solution:
    def minSwaps(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and c == ']':
                stk.pop()
            elif c == '[':
                stk.append(c)
