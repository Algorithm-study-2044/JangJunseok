# 3:33 시작. 10분 소요. 18ms. 27.38ms.

class Solution(object):
    def customSortString(self, order, s):
        dic = {}
        last = len(order)

        for i, val in enumerate(order):
            dic[val] = i

        for i in s:
            if i not in dic:
                dic[i] = last
                last += 1
                
        return "".join(sorted(list(s),key=lambda x:dic[x]))