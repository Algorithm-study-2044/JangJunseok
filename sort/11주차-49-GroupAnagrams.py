# 5:45. 5분 소요. 68ms. 99.61% beats.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for st in strs:
            my_dict["".join(sorted(st))].append(st)
        
        return my_dict.values()