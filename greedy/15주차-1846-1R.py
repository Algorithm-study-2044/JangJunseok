# 3분 소요. 409ms. 17.40% beats.

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(len(arr)):
            if i >= 1:
                arr[i] = min(arr[i-1]+1,arr[i])
        return arr[-1]