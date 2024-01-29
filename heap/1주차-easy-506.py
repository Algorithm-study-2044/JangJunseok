#1차시도
# 시간 복잡도는 O(nlogn)
class Solution(object):
    def findRelativeRanks(self, score):
        heap = []
        result = []
        heap = sorted(score, reverse=True)

        for num in score:
            whos = heap.index(num)
            if whos == 0:
                result.append("Gold Medal")
            elif whos == 1:
                result.append("Silver Medal")
            elif whos == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(whos+1))
        
        return result
    

#2차시도
class Solution(object):
    def findRelativeRanks(self, score):
        result = []
        heap = sorted(score, reverse=True)
        mapped_heap = {number: i for i,number in enumerate(heap)}

        for num in score:
            whos = mapped_heap[num]
            if whos == 0:
                result.append("Gold Medal")
            elif whos == 1:
                result.append("Silver Medal")
            elif whos == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(whos+1))
        
        return result