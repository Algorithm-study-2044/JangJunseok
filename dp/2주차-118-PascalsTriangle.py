#2주차. 10분소요. pass. 11ms. 93% beats.

class Solution(object):
    def generate(self, numRows):
        result = [0] * numRows
        for i in range(numRows):
            result[i] = [1] * (i+1)
            if i >= 2:
                for j in range(1,i):
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result
                    