# 2차시도. 다른 사람의 풀이 참고.

# 즉 현재 요소가 뒤집혔는지? 안뒤집혔는지? 를 판단하기 위해서,
# 그 시작점이 뒤집힌채로 시작 -> 그런데 지금도 뒤집혀있다 -> 그러면 이건 안뒤집힌거
# 그 시작점이 안뒤집힘 -> 근데 지금 뒤집어짐 -> 그럼 이건 뒤집힌거.
#             if i >= k: # is_flipped = is_flipped ^ arr[i-k]
# 이 부분이 조금 어려웠던 것 같다. o(n)만큼의 시간복잡도를 위해서, 
# 현재 뒤집혀있나 안뒤집혀있나?를 생각하고. 그리고 그 시작점 i-k를 기준으로.

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        is_flipped = 0
        res = 0
        arr = [0]*n
        
        for i in range(n):
            if i >= k:
                is_flipped = is_flipped ^ arr[i-k]

            if is_flipped == nums[i]:
                # 뒤집어야 하는데, 최대 가능한 저거는 n-k까지
                if i > n-k:
                    return -1
                res += 1
                is_flipped ^= 1
                arr[i] = 1
            
        return res


# 8:53 시작. 1차시도. 시간초과.

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        i = next = 0
        while next <= len(nums) -1:
            i = next
            if i <= len(nums) - k:
                if nums[i] == 0:
                    nums[i] = 1
                    res += 1
                    for plus in range(1,k):
                        if nums[i+plus] == 0:
                            nums[i+plus] = 1
                        else:
                            nums[i+plus] = 0
                            if i == next:
                                next = i + plus
                    if i == next:
                        next += 1
                else:
                    next += 1
            if i > len(nums) - k:
                if nums[i] == 0:
                    return -1
                next += 1
                
        return res 