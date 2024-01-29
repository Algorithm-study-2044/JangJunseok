# 1차시도. timeout.
# 2차시도. 20분 소요. pass.
# 이런게 은근히 헷갈린다. 그 숫자에 해당하는 2진수의 1의 갯수를 세는데,
# max값을 구할때,
class Solution(object):
    def calcBinaryOne(self,number):
        max = 0
        cnt = 0
        while (number // 2**(max+1)) >= 1:
            max += 1
        while max >= 0:
            if number >= 2**(max):
                number -= 2**(max)
                cnt += 1
            max -= 1
        return cnt 
        
    def sortByBits(self, arr):
        arr.sort(key=lambda x:(self.calcBinaryOne(x), x))
        return arr
    

# 이런 망할. 2진수로 변환하는 함수가 있었다니.
class Solution(object):
    def sortByBits(self, arr):
        dror1 = list(arr)
        dror1.sort(key=lambda x: (bin(x).count('1'), x))
        return dror1