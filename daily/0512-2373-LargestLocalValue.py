#10:33. 125ms. 71.67ms. 10분 소요.

import math

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        size = n-2
        res = [[0]*size for _ in range(size)]
        
        for sr in range(size):
            for sc in range(size):
                arr = []
                for br in range(sr,sr+3):
                    for bc in range(sc,sc+3):
                        arr.append(grid[br][bc])
                res[sr][sc] = max(arr)
        
        return res