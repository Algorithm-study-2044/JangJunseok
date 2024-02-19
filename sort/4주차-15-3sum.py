#4주차. 2차시도. 성공. 621ms. 94% beats.
# 어디서 막혔었나? 메모리가 막힘. 일단 기본적으로 idx + 1 해준다음에, 그게 이전과 같으면 한번 더 더해준다는 개념이 있어야 함.
# 그 이외에는 투포인터의 개념과 동일함. 

class Solution(object):
    def threeSum(self, nums):
        arr = sorted(nums)
        res = []

        def findTwoSum(target,arrs):
            if arrs[0] + arrs[1] > target or arrs[-1] + arrs[-2] < target:
                return
            
            left = 0
            right = len(arrs) - 1
            while left < right:
                if arrs[left] + arrs[right] > target:
                    right -= 1
                elif arrs[left] + arrs[right] < target:
                    left += 1
                else:
                    res.append([-target,arrs[left],arrs[right]])
                    left += 1
                    while left <= len(arrs) - 1 and arrs[left-1] == arrs[left]:
                        left += 1

        start = 0
        
        while start < len(arr) - 2:
            findTwoSum(-arr[start],arr[start+1:])
            start += 1
            while start <= len(arr) - 1 and arr[start] == arr[start-1]:
                start += 1

        return res