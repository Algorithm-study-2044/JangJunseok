# 11:58 -> 12:13

class Solution(object):
    def minDeletions(self, s):
        freq_dict = Counter(s)
        freq = set()
        res = 0

        for c in set(s):
            while freq_dict[c] in freq:
                freq_dict[c] -= 1
                res += 1
            if freq_dict[c] != 0:
                freq.add(freq_dict[c])
        
        return res