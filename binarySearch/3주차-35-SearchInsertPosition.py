#3주차. 20분. 풀이 참고함.

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        # 같을때도 고려해주어야 함.
        while l <= r:
            #여기서 반내림이나 반올림이나 크게 상관없음.
            mid = (l+r) // 2
            #l = mid 이렇게 하면, 2개 있는 상황에서, 계속 같은 값이 나오면 무한루프에 빠짐.
            if nums[mid] < target:
                l = mid + 1
            # r = mid 이렇게 하면, 값이 같은 상황에서, nums[mid]가 target보다 작으면, r이 왼쪽으로 가야하는데, 가지를 못함.
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l