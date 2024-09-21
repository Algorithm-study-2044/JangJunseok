# 10:56 시작. 1차시도 실패. 짝수일때를 고려 안함. abba 이렇게 되면. 중간에 있는 두개가 같아도 되는건데. 

# 4니까, 일단은 b부터 시작할 수 있는지? 즉 idx//2 -1 에서 시작. 왼쪽으로 쭉 간다.
# 근데 만약에 맨 왼쪽에 도달했다? 그러면 그냥 오른쪽에 있는거 다 갖다붙이면 된다.

# 그래서 사실은, 그렇게 한 요소마다 iterate를 하면 되겠지만,, 이러면 n**2니까.
# 일단 그렇게라도 해볼까?

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""

        def make_palin(pivot_idx,s):
            left = pivot_idx -1
            right = pivot_idx + 1

            pivot = s[pivot_idx]
            while left >= 0 and right <= len(s) -1:
                if s[left] != s[right]:
                    return None
                left -= 1
                right += 1

            return "".join(reversed(s[pivot_idx+1:])) + pivot + s[pivot_idx+1:]
        
        start_idx = len(s) // 2 -1 if len(s) % 2 == 0 else len(s) //2

        while start_idx >= 0:
            res = make_palin(start_idx,s)
            if res:
                return res
            start_idx -= 1

        return ""
        

# 다른 사람의 풀이.ㄴ

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        count = self.kmp(s[::-1], s)
        return s[count:][::-1] + s
    def kmp(self, txt: str, patt: str) -> int:
        new_string = patt + '#' + txt
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]