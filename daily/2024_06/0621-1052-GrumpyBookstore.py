# 2차시도. 217ms. 49.31 beats.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        arr = [0] * n
        origin = 0
        res = 0

        for i in range(n):
            if grumpy[i] == 1:
                arr[i] = customers[i]
            else:
                origin += customers[i]
        
        curr = sum(arr[0:minutes])

        for i in range(n):
            if i >= 1 and i <= n-minutes:
                curr = curr - arr[i-1] + arr[i+minutes-1]
            elif i >= n-minutes +1:
                curr = curr - arr[i-1]
            res = max(curr,res)

        return res + origin


# 1차시도. 브루트포스. 시간초과 실패.
# 아무래도..각 position마다 고객을 세버리면 오바가 나는 듯 하다.    
# 그래서 밑에처럼 1 있는것들로만 했는데도, 오류가 남. 그 이유는..

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        origin = 0
        res = 0
        hok = set()
        for i in range(n):
            if grumpy[i] == 0:
                origin += customers[i]
            else:
                hok.add(i)
        
        for idx in hok:
            curr = 0
            for i in range(minutes):
                if idx+i in hok:
                    curr += customers[idx+i]
            res = max(res, curr)
        
        return origin + res