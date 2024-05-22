# 12:27분 시작. 39분 성공. 181ms. 73.68% beats.

class Solution(object):
    def winnerOfGame(self, colors):
        a = 0
        b = 0

        for i in range(0,len(colors)-2):
            chunk = colors[i:i+3]
            if chunk == "AAA":
                a += 1
            elif chunk == "BBB":
                b += 1
        
        # 이기는 조건이, a와 b가 2이상 차이가 나 버리면, 그러면 둘 중 하나는 이긴다.

        # 1 1 -> false
        # 2 1 -> true
        # 0 0 -> false
        # 1 0 -> true
        
        # 그럼 간단하게 그냥 a가 b보다 1이상 크면 이기는건가?
        
        return True if a>=b+1 else False