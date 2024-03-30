#1차시도. 브루트포스로 풀었음. 시간초과. 

class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = []

        # 최소 minOfStack보다는, 큰 값이 들어올때까지 기다려야 하지 않나.
        for idx in range(len(temperatures)):
            target = temperatures[idx]
            start = 1
            flag = False
            for j in range(idx+1,len(temperatures)):
                if not flag and temperatures[j] > target:
                    flag = True
                    res.append(start)
                start += 1
            if not flag:
                res.append(0)
            
                
        return res
    

# 2차시도. 다른 사람의 풀이 참고.
    
# 끝에서부터 시작해서, 그 끝에 친구 입장에서, 그 다음으로 큰 친구가 언제 나오는지를.
# 왜 마지막부터 시작할까. 생각해보자. 뒤엣놈 입장에서 후보군을 지울때. a,b,c에서 c가 만약 b보다 작았다고 한다면,
# a 입장에서는 b만 고려해도 된다는 것이다.

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        deq = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not deq:
                res[i] = 0
                deq.appendleft(i)
            else:
                target = temperatures[i]

                while deq and target >= temperatures[deq[0]]:
                    deq.popleft()
                
                if not deq:
                    res[i] = 0
                else:
                    # 이러면 후보군이 있다는 의미.
                    # 그럼 가장 가까운 친구가 deq[0]일테니까.
                    res[i] = deq[0] - i
                
                deq.appendleft(i)
 
        return res