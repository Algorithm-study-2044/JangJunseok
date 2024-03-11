#6시 30분. 
#그리디하게 접근하려면. 일단은 가장 빈도수가 적은 친구부터 지운다.
#실수한 부분은. 같은 cnt의 친구였을때 같은 요소이면 나란히 정렬되어야 했다.
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        
        cnt = Counter(arr)
        return len(set(sorted(arr,key=lambda x:(cnt[x],x))[k:]))