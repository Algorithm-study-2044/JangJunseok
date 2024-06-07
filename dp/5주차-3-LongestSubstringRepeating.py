#10:31 시작. 48ms. 88% beats.

# a,b,c 간 다음에는, 굳이 b에서 다시 계산할 필요 없지 않나? 싶지만.
# 그러면 two pointer식으로. 중복 발견시 해당 index까지 left +1해주고,

# 중복 발견시 중복 없을때까지 pop해주고,.
# 그럴려면, queue로 만들어서, pop시키는 방안이 있을 것임.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = s.replace(" ","가")        

        seen = set()
        queue = deque([])
        cnt = 0
        maxVal = 0

        for i in range(len(s)):
            curr = s[i]
            if curr in seen:
                maxVal = max(maxVal, cnt)
                while curr in seen:
                    delt = queue.popleft()
                    seen.remove(delt)
                    cnt -= 1
                seen.add(curr)
                queue.append(curr)
                cnt += 1

            else:
                seen.add(curr)
                queue.append(curr)
                cnt += 1

        maxVal = max(maxVal, cnt)
        return maxVal


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
    

