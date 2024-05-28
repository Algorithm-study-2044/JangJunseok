#1차시도 시간초과 실패.
# 역시나 그냥 하면 시간초과가 난다. 더하는게 문제임.

# 새로 더해지는 것의 크기가 중요할듯.
# 만약 맨 마지막에 더해진다면? 기존것들 가지고 계산하면 되고,

# 아니면 heap을 사용해서?

# 아니면 새로 들어온것보다 작은거는 다 pop한다음에,
# len에 따라서 하나를 pop하던지 아니면 두개를 pop하던지? 

# 1 넣고, 2 넣는 경우에,

# pop한애들은 근데, 나중에 다시 넣어줘야 한다.

# 2차시도. 다른사람의 풀이 참고.

class MedianFinder:
    def __init__(self):
        """
        """
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, -1*num)
        # if self.large and num > self.large[0]:
        #     heapq.heappush(self.large, num)
        # else:
        #     heapq.heappush(self.small, -1 * num)

        # 이 밑에 있는거는 두 친구의 밸런스 조정.
        # 이렇게 하면 self.small과 large의 차이는, 항상 1 아니면 같을것이다.

        # 그럼 그냥 작은데다가 넣어놓고, 2이상 차이날때 large로 옮기는 방식은 어떤가?

        # a b 있고 c가 있을때, c가 들어왔을때 그 자리가 중요하다.
        # 그런데 지금 a c b 이렇게 되는거랑. a b c 이렇게 되는거랑은 다르다.
        # 그러니까 findMedian 메서드에 영향을 주기 때문에, 넣을때 제대로 넣어야 한다는 것이다. 
        

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    # 그림으로 따지만, ssss' 'llll 이렇게 있을때, ' 자리에 들어갈 두개를 heap으로 구하는 것 같다.
    # s' 'l 에서 하나를 s자리에 넣는거랑, large[0]랑 비교해서 넣는거랑 차이는.
    # num이 large[0]보다 크면, s자리에 무조건 넣는것같으면 s에 들어가지만, 

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2.0