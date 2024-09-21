# 10:40. 10분 소요. 1271ms. 13.90% beats.

# a <- e
# e <- a,i
# i <- a,e,o,u
# o <- i,u
# u <- a

# [a,e,i,o,u]
# a,5를 넣음 -> 그러면 a에 해당하는 e를 찾고 -> e로 시작하는 길이 4짜리 length가 있나? 있음 return 없음 계산.

chr_dict = {
    "a": ["e"],
    "e": ["a","i"],
    "i": ["a","e","o","u"],
    "o": ["i","u"],
    "u": ["a"]
}

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [{} for i in range(n+1)]

        def DFS(chr,lend):
            if lend == 1:
                dp[lend][chr] = 1
                return dp[lend][chr]

            if chr in dp[lend]:
                return dp[lend][chr]
            
            val = 0
            for cand in chr_dict[chr]:
                val += DFS(cand, lend-1)
            dp[lend][chr] = val

            return dp[lend][chr]
        
        res = 0
        for i in ["a","e","i","o","u"]:
            res += DFS(i,n)
            
        return res % (10**9 + 7)