#4:34. 1차시도. 실패. 언제 1개를 사고, 언제 하나를 팔고 두개를 사면 좋을지.
# 지금 이렇게 하면 둘 중에 하나만 우선시되어버린다.

from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        queue = deque(sorted(tokens))
        score = 0
        print(queue)
        if not tokens or queue[0] > power:
            return 0
        
        tq = queue.popleft()
        score += 1
        power -= tq

        def DFS(arr,power):
            nonlocal score

            print(arr,power,score)
            
            # 만약 살 수 있으면, 산다.
            if arr and power >= arr[0]:
                curr = arr.popleft()
                power -= curr
                score += 1

                DFS(arr,power)
                return

            if len(arr) < 3:
                return 

            if power + arr[-1] >= arr[0] + arr[1]:
                big = arr.pop()
                left1, left2 = arr.popleft(), arr.popleft()
                score += 1
                power += big - left1 -left2
                DFS(arr,power)
        
        DFS(queue,power)

        return score