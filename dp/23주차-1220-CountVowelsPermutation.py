# 25분. 2701ms. 5% beats.

# ae, ea ei, oi ou, ua, ia ie io iu
# a2개 e1개 i2개,o1개, u2개

# aeiou 그리고 n개의 matrix를 구성한다.
# a로 시작해서, 구성한다. 

# a -> ae -> aea, aei -> aeae, aeia aeie aeio aeiu

rank = {
    "a":0,
    "e":1,
    "i":2,
    "o":3,
    "u":4
}

vow_map = {
    "a": ["e"],
    "e": ["a","i"],
    "i": ["a","e","o","u"],
    "o": ["i",'u'],
    "u": ["a"]
}

# a -> ae -> aea, aei -> aeae, aeia aeie aeio aeiu
# a. a에서 시작하는 5를 찾는다, 없으면, a다음 가능한거를 찾는다.

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        matrix = [[0]*(n+1) for _ in range(5)]

        def DFS(strs):
            #해당 strs의 끝에 오는 길이가 이미 계산되어있으면 그거 사용.
            if matrix[rank[strs[-1]]][n-len(strs)+1]:
                return matrix[rank[strs[-1]]][n-len(strs)+1]
            
            if len(strs) == n:
                return 1

            cnt = 0
            # 없으면 가능한 애를 다 만들어준다.
            for child in vow_map[strs[-1]]:
                cnt += DFS(strs+child)
            # matrix에 저장한다.
            matrix[rank[strs[-1]]][n-len(strs)+1] = cnt
            return cnt
        res = 0
        for vow in ["a","e","i","o","u"]:
            res += DFS(vow)
        return res % (10**9 + 7)