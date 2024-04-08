# 1차시도. 실패. 다른 사람의 풀이 참고.

class Solution:
    def minOperations(self, n: int) -> int:
        q =  deque([n])
        seen = set([n])
        res = -1
        
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur == 0:
                    return res
                
                for i in range(17):
                    t = 1 << i
                    
                    if cur + t <= 2 ** 17 and cur + t not in seen:
                        q.append(cur + t)
                        seen.add(cur + t)
                    if cur - t >= -(2 ** 17) and cur - t not in seen:
                        q.append(cur - t)
                        seen.add(cur - t)