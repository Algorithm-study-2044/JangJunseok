from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        queue = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):

            if not queue:
                queue.appendleft(i)
                
            else:
                while queue and temperatures[queue[0]] <= temperatures[i]:
                    queue.popleft()

                if not queue:
                    #이러면
                    res[i] = 0
                else:
                    res[i] = queue[0] - i

                queue.appendleft(i)
            
        return res