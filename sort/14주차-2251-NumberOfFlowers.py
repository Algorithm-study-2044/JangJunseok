# 2251. Numbers of Flowers in Full Bloom
## 3:50 시작. 30분 소요. 1차시도. 메모리 초과. 실패.

# 그러니까 해당 사람 입장에서는, 나보다 이전에 핀 것들이 얼마나 있는지? 그리고
# 그것들이 내가 있는 시간보다 늦게까지 피는지? 이런것들이 궁금한 것이다.

# 아니 근데 그냥 하면, n * k가 나온다. 그러면 늦을지도.
# 아예 나보다 시작시간 늦어버리면? 그럼 굳이 평가할 이유가 없다.

# 그리고 한 사람의 계산은, 시간이 똑같지 않다면 다른 계산에 쓰이기가 힘들지 않나.

# 1부터 시작해서, 최대 max(end) 까지 해서,
# start와 end를 flat 하게 만들면 되지 않을까.

class Solution(object):
    def fullBloomFlowers(self, flowers, people):

        start_times = defaultdict(int)
        end_times = defaultdict(int)

        for i in flowers:
            start_times[i[0]] += 1
            end_times[i[1]] += 1
        
        endTime = max(people)
        bloom = 0
        bdic = {}

        for i in range(1,endTime+1):
            if i in start_times:
                bloom += start_times[i]
            if i-1 in end_times:
                bloom -= end_times[i-1]
            # 왜 메모리초과가 날까. bdic에는 지금 endTime만큼 저장이 된다. 
            # 그래서 그런듯.
            bdic[i] = bloom        
        
        return [bdic[p] for p in people]
    


# 2차시도. gpt의 풀이.

from collections import defaultdict
import bisect

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        start_times = []
        end_times = []
        
        for start, end in flowers:
            start_times.append(start)
            end_times.append(end)
        
        start_times.sort()
        end_times.sort()
        
        def count_blooms_at_time(t):
            # 왜 bisect_right를 쓰는가? 만약 내 시간보다 작거나 같다면, 그건 피는걸로 카운트 해야하는거고
            
            blooms_started = bisect.bisect_right(start_times, t)

            # 지는것도 마찬가지로, i-1보다 작거나 같은것들을 다 카운트 해야.
            blooms_ended = bisect.bisect_right(end_times, t - 1)
            return blooms_started - blooms_ended
        
        result = []
        for p in people:
            result.append(count_blooms_at_time(p))
        
        return result
