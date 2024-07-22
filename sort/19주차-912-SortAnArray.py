# 6:46. 버블정렬. 시간초과.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:   
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
# 힙으로 푸는 풀이. ======================================================================================

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heapify(nums)
        for _ in range(len(nums)):
            res.append(heappop(nums))

        return res

# RADIX sort ======================================================================================

from functools import reduce
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        l2=[]
        for x in nums:
            if x <0:
                l.append(x)
            else:
                l2.append(x)
        A=Solution.neg(l2)
        c=Solution.neg(l)
        d=[-x for x in c][::-1]
        return d+A
    
    def neg(nums):
        if nums==[]:return []
        nums=[abs(x) for x in nums]
        a=max(nums)
        b=len(str(a))
        # 아 그러니까 처음에는 1의자리수로 정렬한다음에,
        # 그걸 다시 두번째 자리로 정렬해서 넣으면, 자리수가 다르면 다르겠지만, 자리수가 같을때는, 더 뒤에 들어가게 된다.
        # 그래서 이걸 반복하면, 자리수가 다른애들은 먼저 정렬되고, 그 다음에는 자리수가 같은애들이 정렬된다.
        for x in range(0,b):
            B=[[] for x in range(10)]
            for y in range(len(nums)):
                num=nums[y]//10**(x) % 10
                B[num].append(nums[y])
            nums=reduce(lambda x,y:x+y,B)
        return [int(x) for x in nums]
        
        