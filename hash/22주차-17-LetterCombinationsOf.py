# 8:45. 38ms. 37% beats.

# 예를 들어, 23이면
# abc, def 이렇게 나올텐데,

# 3개면? 조합이 더 많아질거고.
# 그러면 combination or DFS로 해결하면 될듯.

keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stored = []
        for d in digits:
            stored.append(keyboard[d])
        res = []
        if digits == "":
            return res

        def DFS(curr,level):
            if level > len(stored) -1:
                res.append(curr)
                return
                
            for i in range(len(stored[level])):
                DFS(curr+stored[level][i],level + 1)
            
        DFS("",0)
        return res