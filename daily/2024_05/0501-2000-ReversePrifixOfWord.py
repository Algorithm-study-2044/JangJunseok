# 11:14. 6분 소요.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        wdr = list(word)
        for i,v in enumerate(wdr):
            if v == ch:
                wdr[:i+1] = wdr[:i+1][::-1]
                break
        
        return "".join(wdr)