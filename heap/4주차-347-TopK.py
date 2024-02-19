#4주차. 72ms. 74% beats.

class Solution(object):
    def topKFrequent(self, nums, k):
        self.hm = {}
        for i in nums:
            if i not in self.hm:
                self.hm[i] = 1
            else:
                self.hm[i] += 1
        
        return [item[0] for item in sorted(self.hm.items(), key=lambda x:-x[1],)[0:k]]
