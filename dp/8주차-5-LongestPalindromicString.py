# babad

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                # i-j가 2이하면 그냥 똑같을 테니까.
                # 아니면? 이전에 저장된걸 사용한다. 
                # cbabc 이렇게 있을때
                # 이건 양 끝만 비교를 한거다. 그 경우에, j+1과 i-1을 양끝으로 가지는 애가 있으면.
                # 그러면 그 친구도 palindrome이 된다는 것이다.
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str    


# #1차시도. 실패. 다른사람의 풀이 참고.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            #return the palin string.
            if right > len(s)-1 or s[left] != s[right]:
                return s[left]

            while left >= 1 and right <= len(s) -2 and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            return s[left:right+1]

        res = ""
        maxA = 0

        for i in range(0,len(s)):
            s1 = expand(i,i)
            s2 = expand(i,i+1)

            if len(s1) >= maxA:
                res = s1
                maxA = len(s1)
            
            if len(s2) >= maxA:
                res = s2
                maxA = len(s2)
        
        return res