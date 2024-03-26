# 1차시도. 10분. 15ms. 44.7% beats.
# 중간에 메모리 초과가 났었다. 
# array를 정의해주지 않고, 그냥 바로 하면 된다. 어차피 index+1이니까.

class Solution(object):
    def firstBadVersion(self, n):
        #n은 array이고
        #isBadVersion을 call해서 찾으라는 것 같다.
        l = 0 
        r = (n-1)
        while l<=r:
            mid = (l+r) // 2
            if isBadVersion(mid+1):
                r = mid - 1
            else:
                l = mid + 1
        
        return l+1