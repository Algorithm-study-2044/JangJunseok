# 20.45% beats. 23ms.

import heapq
class Solution(object):
    def reorganizeString(self, s):
        cnt = Counter(s)
        my_list = []
        for key in cnt.keys():
            heapq.heappush(my_list,(-cnt[key],key))

        res = ""
        while len(res) != len(s) and my_list:
            if len(my_list) == 1:
                if len(res) < len(s)-1:
                    return ""
                else:
                    return res + my_list[0][1]
            
            a = heapq.heappop(my_list)[1]
            b = heapq.heappop(my_list)[1]
            res += a
            res += b
            cnt[a] -= 1
            cnt[b] -= 1
            if cnt[a]:
                heapq.heappush(my_list,(-cnt[a],a))
            if cnt[b]:
                heapq.heappush(my_list, (-cnt[b],b))
            
        
        return res