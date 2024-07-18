# 4:11. 146ms. 15.94% beats.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = deque([i for i in range(1,n+1)])

        while len(arr) >= 2:
            for _ in range(k):
                t = arr.popleft()
                arr.append(t)
            arr.pop()

        return arr[0]
    

# 다른 풀이로 다시 볼 것.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1:
                return 0
            return (recursion(n - 1, k) + k) % n

        return recursion(n, k) + 1
