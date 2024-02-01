class Solution(object):
    def balancedStringSplit(self, s):
        firstLat = ""
        latcnt = 0
        result = 0
        for char in s:
            if latcnt == 0:
                firstLat = char
            if char == firstLat:
                latcnt += 1
            else:
                latcnt -= 1
            if latcnt == 0:
                result += 1
        return result