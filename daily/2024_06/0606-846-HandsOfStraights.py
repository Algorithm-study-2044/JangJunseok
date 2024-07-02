# 2차시도. 1236ms. 8% beats.
# 나는 그냥 하나하나 채우는 느낌을 생각함.

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        size = len(hand) // groupSize
        queue = [[] for _ in range(size)]
        hand.sort()
        
        for c in hand:
            flag = True
            for i in range(len(queue)):
                if len(queue[i]) == 0 or queue[i][-1] + 1 == c:
                    queue[i].append(c)
                    if len(queue[i]) == groupSize:
                        queue.pop(i)
                    flag = False
                    break
            if flag:
                return False
        return True


# chatGPT의 풀이. 157ms. 75% beats.
# 어떻게? 1이 있다. 그러면 groupSize만큼. 123 이렇게 갈테니가.
# 그렇게 해서 다 없앤 다음에, 그 다음 선두에 오는 애들.. 이렇게 해서 다 없애주는 거다.

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in sorted(hand):
            if count[num] > 0:
                for i in range(groupSize):
                    if count[num + i] > 0:
                        count[num + i] -= 1
                    else:
                        return False
        return True