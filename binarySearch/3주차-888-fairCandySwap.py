# 3주차. 20분 소요. 이진탐색은 sort를 해야한다는걸 잊지말자.
class Solution(object):
    def binarySearch(self,arr,target):
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r) // 2
            if arr[mid] == target:
                return target
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return None

    def fairCandySwap(self, aliceSizes, bobSizes):
        bobSizes.sort()
        diff = sum(bobSizes) - sum(aliceSizes)
        a = diff // 2
        result = []
        for item in aliceSizes:
            if self.binarySearch(bobSizes,item+a):
                result.append(item)
                result.append(item+a)
                break
        return result