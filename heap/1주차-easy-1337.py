# 힙으로 푸는 방법도 생각해보기.
# 11분 소요. pass.

class Solution(object):

    def kWeakestRows(self, mat, k):
        arr = []
        for index, row in enumerate(mat):
            arr.append((sum(row),index))
        arr.sort(key=lambda x:(x[0],x[1]))

        return [item[1] for item in arr[0:k]]


