# 6:22. 10분 소요. 165ms. 13.74% beats.
# 1차시도. 시간초과. -> set으로 바꿔서 성공.
# in list를 쓰면 len(list)만큼의 시간복잡도가 걸린다는 점에 유의.
    
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cnt = 0
        card = set()
        while cnt ** 2 <= c:
            card.add(cnt**2)
            cnt += 1

        for item in card:
            if c - item in card:
                return True
        return False
    

# 다른 풀이. 투포인터.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False