# 1차시도. 32분 소요. 371ms. 30.77% beats.

from collections import defaultdict

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        
        self.hm = defaultdict(list)
        self.dp = defaultdict(int)
        arr.sort()
        for index,item in enumerate(arr):
            self.hm[item].append((None,None))
            for i in range(index):
                if item % arr[i] == 0:
                    self.hm[item].append((arr[i],item // arr[i]))

        myCount = 0
        for item in arr:
            myCount += self.getAllCount(item)

        return myCount % (10**9 + 7)

            

    def getAllCount(self,node):
        if not node:
            return 1
        
        #만약에 이미 해당 node의 조합이 계산되어 있다면 그걸 반환한다.
        if self.dp[node]:
            return self.dp[node]

        cnt = 0
        for left,right in self.hm[node]:
            lm = self.getAllCount(left)
            rm = self.getAllCount(right)
            cnt += lm * rm
        
        self.dp[node] = cnt

        return cnt