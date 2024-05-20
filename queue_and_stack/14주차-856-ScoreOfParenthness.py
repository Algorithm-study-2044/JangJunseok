#12:15. 1차시도 성공. 7ms. 94% beats.
# "(()(()))"
# ( -> level 1 
# ( level 2 
# ) -> level 1 
# ( level 2
# ( level 3
# ) level 3
# ) level 2
# ) level 1

from collections import defaultdict

class Solution(object):
    def scoreOfParentheses(self, s):
        before = None
        lv = defaultdict(int)
        level = 0

        for c in s:
            if c == ")":
                if before == "(":
                    lv[level] += 1
                elif before == ")":
                    lv[level] += lv[level+1] * 2 
                    lv[level+1] = 0
                level -= 1
            else:
                level +=1 
            before = c

        return lv[1]