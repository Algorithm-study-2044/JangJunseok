#2분 소요. pass
class Solution(object):
    def isAnagram(self, s, t):
        str1 = "".join(sorted(s))
        str2 = "".join(sorted(t))
        return str1 == str2