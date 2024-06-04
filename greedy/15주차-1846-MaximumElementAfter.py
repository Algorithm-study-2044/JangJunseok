# 9:06 시작. 15분 소요. 365ms. 76.50% beats.

# cond = [1,2]
# sortedArr = [1,1,2,2,2]
# res = [1,]

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        cond = [1] * len(arr)
        arr.sort()
        res = [1] * len(arr)

        for i in range(1,len(arr)):
            cond[i] = res[i-1] + 1

            if arr[i] <= cond[i]:
                res[i] = arr[i]    
            else:
                res[i] = cond[i]
        
        return res[-1]