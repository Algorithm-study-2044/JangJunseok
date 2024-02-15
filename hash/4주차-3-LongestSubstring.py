#4주차. 31ms. 81% beats. 투포인터를 활용해서 풀었음.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        startIndex = 0
        endIndex = 0
        currentString = ""

        for char in s:
            if char not in currentString:
                endIndex += 1
            else:
                idx = currentString.find(char)
                for _ in range(idx+1):
                    startIndex += 1
                endIndex += 1
            currentString = s[startIndex:endIndex]
            maxLength = max(maxLength, len(currentString))
        
        return maxLength