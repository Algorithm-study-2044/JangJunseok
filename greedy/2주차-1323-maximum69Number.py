#2주차. pass. 9ms. 90% beats.

class Solution(object):
    def maximum69Number (self, num):
        num2 = str(num)
        idx = num2.find("6")
        if idx == -1:
            return num
        string = num2[0:idx] + "9" + num2[idx+1:]
        return int(string)
    

