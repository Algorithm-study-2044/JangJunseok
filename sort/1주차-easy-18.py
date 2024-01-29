#1차시도. 시간초과.
from itertools import combinations

class Solution(object):
    def fourSum(self, nums, target):
        result = []
        lists = list(combinations(nums,4))
        for item in lists:
            if sum(item) == target:
                result.append(list(item))
        
        return result
    
#정답코드. pass. two pointer, recursion, backtracking 을 활용한 문제.

class Solution(object):
    def fourSum(self, nums, target):
        result = []
        self.findSums(sorted(nums),target,4,[],result)
        return result

    def findSums(self,arr,target,N,current,result):
        # two pointers
        if N<2 or len(arr) < 2 or target < arr[0] * N or target > arr[-1] * N:
            return
        if N == 2:
            l,r = 0,len(arr)-1
            while l < r:
                val = arr[l] + arr[r]
                if val == target:
                    result.append(current + [arr[l], arr[r]])
                    l += 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1 
                elif val < target:
                    l += 1
                    # while l > 0 and arr[l] == arr[l-1]:
                    #     l += 1
                else:
                    r -= 1
        else:
            for i in range(0,len(arr)-N+1):
                if i == 0 or (i>0 and arr[i] != arr[i-1]):
                    self.findSums(arr[i+1:],target-arr[i],N-1,current+[arr[i]],result)
			