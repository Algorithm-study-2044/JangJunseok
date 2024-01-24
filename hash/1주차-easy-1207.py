class Solution(object):
    def uniqueOccurrences(self, arr):
        hash = {}
        for i in arr:
            if i not in hash:
                hash[i] = 0
            else:
                hash[i] += 1
        
        return len(hash.keys()) == len(set(hash.values()))