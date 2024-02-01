#2주차. 15분소요. pass. 98ms. 89% beats.

class Solution(object):
    def makeSmallestPalindrome(self, s):
        lan = len(s) // 2    
        result = ""
        for i in range(lan):
            if ord(s[i]) <= ord(s[-i-1]):
                result += s[i]
            else:
                result += s[-i-1]
            
        result += "".join(reversed(result))
        if len(s) % 2 != 0:
            result = result[:lan] + s[lan] + result[lan:]
        return result