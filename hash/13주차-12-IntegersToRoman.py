# 1차시도. 59ms. 5% beats. 다른 방법이 있나?

class Solution(object):
    def intToRoman(self, num):
        table = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }

        items = sorted(table.items(),key=lambda x:x[0])
        def substract():
            op = None
            for i in range(len(items)-1,-1,-1):
                if num[0] >= items[i][0]:
                    num[0] -= items[i][0]
                    op = items[i][1]
                    break
            return op

        res = ""    
        num = [num]
        while num[0] != 0:
            res += substract()
        
        return res
        

# 다른 사람의 풀이 바탕으로 수정. sorted가 없어서. 조금.

class Solution(object):
    def intToRoman(self, num):
        items = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

        def substract():
            op = None
            for i in range(len(items)):
                if num[0] >= items[i][0]:
                    num[0] -= items[i][0]
                    op = items[i][1]
                    break
            return op

        res = ""    
        num = [num]
        while num[0] != 0:
            res += substract()
        
        return res