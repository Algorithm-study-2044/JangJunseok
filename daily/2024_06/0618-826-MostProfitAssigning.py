# 11:09 시작. 23분 소요. 788ms. 7% beats.
# 다른 사람의 풀이도 살펴볼 것.

from bisect import bisect_left

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        indexed_list = list(enumerate(difficulty))
        indexed_list.sort(key=lambda x:-profit[x[0]])
        worker.sort()
        res = 0

        for idx, level in indexed_list:
            insert_idx = bisect_left(worker,level)
            res += (len(worker) - insert_idx) * profit[idx]
            worker = worker[:insert_idx]
            if not worker:
                break
        return res


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res, j, best, temp = 0, 0, 0, []
        
        for i in range(len(difficulty)):
            temp.append((difficulty[i], profit[i]))
        
        temp.sort()
        worker.sort()
        
        for work in worker:
            while j < len(worker) and work >= temp[j][0]:
                best = max(best, temp[j][1])
                j += 1
            
            res += best
        
        return res