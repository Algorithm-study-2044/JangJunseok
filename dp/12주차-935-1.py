# 5:10 -> 5:27. 880ms. 56.58% beats.

# 예를 들어 n=3 이고 3이 나왔다.
# 그러면. 3간다음에, 그다음 4,8에 대해서,
# 4와 8로 만들 수 있는 두자리수 배열에 관해서는, 
# 그러면 n개의 배열 만들고, 그 안에서,

dial = {
    1: [6,8],
    2: [7,9],
    3: [4,8],
    4: [3,9,0],
    5: [],
    6: [1,7,0],
    7: [2,6],
    8: [1,3],
    9: [2,4],
    0: [4,6]
}

class Solution:
    def knightDialer(self, n: int) -> int:

        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1] * 10

        # n=2이면 한번만 하면 됨.
        for i in range(1,n):
            for j in range(10):
                for neighbor in dial[j]:
                    dp[i][j] += dp[i-1][neighbor]
        
        return sum(dp[n-1]) % (10**9+7)