# 6:22 15분 소요. 109ms. 64% beats. easy문제,

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]: 
        cols = set()
        res = []
        for row in range(len(matrix)):
            min_val = float("inf")
            min_idx = -1
            for col in range(len(matrix[row])):
                if matrix[row][col] < min_val:
                    min_val = matrix[row][col]
                    min_idx = col

            if min_idx not in cols:
                flag = True
                for tr in range(len(matrix)):
                    if matrix[tr][min_idx] > matrix[row][min_idx]:
                        flag = False
                if flag:
                    cols.add(min_idx)
                    res.append(matrix[row][min_idx])
        return res
