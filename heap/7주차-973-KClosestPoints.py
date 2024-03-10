#1차시도. 1분 소요. 524ms. 95% beats. 이게 왜 medium?

import math

class Solution(object):
    def kClosest(self, points, k):
        def calcDistance(x,y):
            return math.sqrt(x**2+y**2)
        
        return sorted(points,key=lambda item:calcDistance(item[0],item[1]))[:k]