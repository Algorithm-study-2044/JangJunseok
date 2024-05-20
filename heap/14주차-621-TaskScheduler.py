# 11:53 시작. 1차시도. 30분 소요. 실패.

# 전에 풀었던 것처럼 그리디하게 접근하면 좋지 않을까 싶다.
# 그 다음 우선순위를 pop했을때, 어? 그런데 똑같은거야..그러면 idle을 넣어주는 식으로.
# 빈도수를 파악해서, 그 순서대로 넣어준다.
# 예를 들어 A2개 B3개라고 한다면, ('A',2) ('B',3) 이런식으로.

# 그런데 문제는, 단순히 붙어있는게 문제가 되는게 아니라, n만큼 interval이 있어야 한다는 것.
# 게다가 단순히 빈도수가 작은 것부터 넣어준다고 해서 맞는걸까>?

# 예를 들어 a2번 b4번이라고 할때,
# aabbbb 이렇게 있을때, aba 이렇게 하면 되지만, 나 대로면 aiabibibibi 이렇게 되어버리니까.

# 그럼 빈도수가 적은걸 두개 pop하는건 어떨까?
# 왜 굳이 두개? 그러면 interval만큼 pop하는건?
# 그러면 interval보다 작은 경우는? idle을 집어넣으면 될지도.

# 그런데 이렇게 했을때 문제는 ["A","A","A","A","A","A","B","C","D","E","F","G"] n=1일때,
# ABCDEFGAiAiAiAiA 이렇게 나오는데, 
# 이러면 i가 너무 많이 나온다.

from collections import Counter, deque
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):  
        hp = []
        freq = Counter(tasks)
        res = 0
        rest = ""

        for chr,num in freq.items():
            heapq.heappush(hp,[chr,num])

        while hp:
            if len(hp) >= n+1:
            # 이러면 n개만큼 pop한다음에, freq-1해서 다시 heapq에 넣어주면 될것.
            # 근데 또 고민되는것은, interval = 2인경우에,
            # 3번 만큼 쉬어야 한다면, n+1을 꺼내야 한다느 것.
                d = deque([])
                for i in range(n):
                    target = heapq.heappop(hp)
                    res += 1
                    rest += target[0]
                    if target[1] >= 2:
                        d.append([target[0],target[1]-1])
            
            # 그 다음에 deque에 있는것들을 다시 heappush 해줘야 함.
                for i in d:
                    heapq.heappush(hp,(i[0],i[1]))

            else:
                # 이러면 hp 다 꺼낸 다음에, (n+1) - len(hp) 만큼 i를 더해주어야 함.
                # 왜? 서로 다른 것들을 넣어도, 다시 원래 것으로 돌아올 가능성이 있기 때문
                # (이 부분이 최선인가는 좀 모호하기는 한다ㅔ,)
                d = deque([])
                orig = (n+1) - len(hp)
                # 이 부분도 그렇다, 만약에 마지막이면 i를 다 지워줘야 하는데, 그거 어떻게??

                for i in range(len(hp)):
                    target = heapq.heappop(hp)
                    res += 1
                    rest += target[0]
                    if target[1] >= 2:
                        d.append([target[0],target[1]-1])

                for i in d:
                    heapq.heappush(hp,(i[0],i[1]))

                if hp:
                    res += orig
                    for i in range(orig):
                        rest += "i"

        print(rest)
                
        return res
    


# 2차시도. 다른 사람의 풀이 참고.

# ["A","A","A","B","B","B"], n = 2

# 근데 근본적으로 궁금한것은, 왜 최대 빈도수인 친구 기준으로 생각하는 것인지.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
                
        chunk = freq[25] - 1
        idle = chunk * n
        
        # 있어야 하는 최대의 idle을 구해준 것.
        # 예를 들어 3번 나오는게 가장 많았다고 하고, 그리고 interval이 2라고 한다면, A _ _ A _ _ A 이렇게 되어야 한다.
        # 즉 idle의 개수는, (빈도수 -1) <- 왜냐하면 사이에 있는거니까. 그 사이 * interval 해준것. 그게 최대 idle의 개수.
        
        # chunk는 뭐하는거야? 최대빈도수 사이 공간의 숫자.

        # 그 다음으로 큰 빈도수부터 차례대로 빼주면서, 최소로 필요한 idle을 구해준다.

        # 만약 freq[i]가 사이 개수보다 작다면? 그 빈도수만큼만 빠질 수 있음. 나머지는 i로 채워야 함.
        # 만약 freq[i]가 사이 개수보다 크다면? 사이 개수만큼 빼주면 됨. 
        
        # 그럼 나머지는 어디로 가는가? 이게 문제인데.

        # 근데 생각해보면, chunk는 max freq -1 이고, 
        # 만약 freq[i] = max freq이라고 한다면, 어차피 크다고 해도 범위는 0~ chunk +1이니가.
        # 그러면, freq[i] - chunk 만큼은 어디로 가는가? 즉 1개는 어디로 가는가?

        # AAABBB 일때, 3개씩 나오는게 가장 많다고 하면,
        # A _ _ A _ _ A 여기에 B를 넣는데, 생각해보면 그냥 자동으로 마지막 A 옆에 붙이면 되지 않나 싶음.

        # A __ A 가 간격이 n이기 때문에, A옆에 순서대로 붙이면 interval은 무조건 n이 보장이 됨.

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        # idle이 음수라면? 
        return len(tasks) + idle if idle >= 0 else len(tasks)