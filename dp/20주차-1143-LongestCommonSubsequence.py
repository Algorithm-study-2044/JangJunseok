
# 1차시도 실패. 여러 문자열의 경우를 고려하지 않았다.

# 즉 c를 발견했을때, c보다 뒤에 있는 애들 중에서 숫자가 하나라도 있으면 cnt += 1 해준다.
# 중복의 경우에는 어떻게 하나? c가 두번 나오는 경우. acec 이렇게 되면.
# ace => 000 같은 문자의 경우 고려하지 않는다. 왜냐하면 먼저 나올수록 좋으니까.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) >= len(text2):
            lt = text1
            st = text2
        else:
            lt = text2
            st = text1

        dic = {}
        dp = [0] * len(st)
        for i in range(len(st)):
            if st[i] not in dic:
                dic[st[i]] = i
        for c in lt:
            if c in dic:
                idx = dic[c]
                if dp[:idx]:
                    dp[idx] = max(dp[:idx]) + 1
                else:
                    dp[idx] = 1
        return max(dp)