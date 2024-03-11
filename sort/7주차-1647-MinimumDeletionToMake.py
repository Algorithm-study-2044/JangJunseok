#7:55분 start. 14분 소요. 285ms. 33% beats.

class Solution(object):
    def minDeletions(self, s):
        cnt = Counter(s)
        res = 0
        freq_set = set()
        
        for key in cnt.keys():
            while cnt[key] in freq_set:
                res += 1
                cnt[key] -= 1
            if cnt[key] != 0:
                freq_set.add(cnt[key])
        
        return res