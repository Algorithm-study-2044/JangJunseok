# 106ms. 52.59% beats.

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipper = zip(names,heights)
        return [x[0] for x in sorted(zipper, key=lambda x:(-x[1]))]