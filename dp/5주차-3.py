# 1차시도 실패.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = -1
        curr_dict = defaultdict(list)
        current = 0
        res = 0
        
        while start <= len(s) -1 and end <= len(s) -2:
            end += 1
            if s[end] in curr_dict:
                res = max(current,res)
                idx = curr_dict[s[end]]

                while start <= idx and start <= len(s) -1:
                    if curr_dict[s[start]]:
                        curr_dict[s[start]].pop(0)
                    start += 1
                    current -= 1
                
            else:
                curr_dict[s[end]].append(end)
                current += 1
        
        res = max(res, current)

        return res