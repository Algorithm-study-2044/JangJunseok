# 1차시도. 43ms. 43.51%

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i in range(len(arr2)):
            order[arr2[i]] = (i,0)
        
        cnt = len(order)
        for num in arr1:
            if num not in order:
                order[num] = (cnt,num)

        return sorted(arr1,key=lambda x:order[x])
        
# 다른 사람의 풀이.
# 일단 len-1 집어넣고, 
# 있으면 그럼 인덱스 집어넣는 식으로.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n2 = len(arr2)
        a2i=[n2]*1001

        for i, x in enumerate(arr2):
            a2i[x]=i
        
        arr1.sort(key=lambda x: (a2i[x], x))

        return arr1
        
        