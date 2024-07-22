# 6:30 시작. ~6:50
# 546ms. 67.87% beats.

# 브루트포스 문제인가?
# 아니, 그리디하게 접근함. 그래도 되잖아?

# 5 0 0  (3,6,8)
# 3,4,0  (0,2,8)
# 0,2,8

# 그러니까 각 row별로. 각 col의 한계 내에서 최대를 주면 되는 것이다.

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))] 

        for i in range(len(matrix)):
            saved = rowSum[i]
            for j in range(len(matrix[i])):
                val = min(colSum[j],saved)
                matrix[i][j] = val
                colSum[j] -= val
                saved -= val
        
        return matrix