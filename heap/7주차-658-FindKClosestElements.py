#1차시도. 8분 소요. 320ms. 16% beats.

import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        my_heap = []

        for item in arr:
            #굳이 이렇게 안하고 그냥 다 넣은다음에 k index slicing하면 된다.
            heapq.heappush(my_heap,(-abs(item-x),-item, item))
        
        return sorted([item[2] for item in my_heap[:k]])
    
#2차시도. 242ms. 34% beats.

#힙을 쓸 이유도.    

class Solution(object):
    def findClosestElements(self, arr, k, x):
        return sorted(sorted(arr,key=lambda item: (abs(item-x),item))[:k])