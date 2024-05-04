# 반복.그 안에서 반복의 형태라면, 재귀를 사용한다. 
# 여전히 헷갈려하는듯 하다. 무엇이 반복되는가>? 그것을 재귀로 풀어내는 것이다.

# [[[1,1],2,[1,1]]]

from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        
        def unpack(nl):
            res = []
            for item in nl:
                if item.isInteger():
                    res.append(item.getInteger())
                else:
                    #그럼 이거는 리스트이다. 어떤? nestedList.
                    res.extend(unpack(item.getList()))
            return res
        
        self.d = deque(unpack(nestedList))

    def next(self):
        return self.d.popleft()

    def hasNext(self):
        return self.d