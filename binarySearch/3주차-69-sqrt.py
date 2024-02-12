#3주차. 15분. 21ms. 48% beats. 헷갈린다 이게....

class Solution(object):
    def mySqrt(self, x):
        
        low = 0
        high = x+1 
        def fn1(number, target):
            return number * number > target

        while low + 1 < high:
            mid = (low+high) // 2
            if(fn1(mid,x)):
                high = mid
            else:
                low = mid

        return low