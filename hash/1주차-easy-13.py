# while 문에서 index out of range 실수로 시간을 좀 잡아먹었다. 
#index+=1 연산은 항상 마지막에 해줄것.
#그리고 마지막거 더하는거는 굳이 while문에 없어도.

class Solution(object):
    def romanToInt(self, s):
        hash_table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        index = 0
        while index != (len(s)):
            char = s[index]
            if index == len(s)-1:
                result += hash_table[char]
                break
            elif (char == "I" and (s[index+1] == "V" or s[index+1] == "X")) or \
     (char == "X" and (s[index+1] == "L" or s[index+1] == "C")) or \
     (char == "C" and (s[index+1] == "D" or s[index+1] == "M")):
                result += (hash_table[s[index+1]] - hash_table[char])
                index += 1
            else:
                result += hash_table[char]
            index += 1

        return result
    

# 다른 사람이 푼 답.
# IV일때, 굳이 뒤에꺼까지 고려하지말고 그냥 I를 빼주면 된다. 
# 예전에 그리디할때 비슷한 유형을 봤던것같은데. 뭐 하튼 그렇다. 
    
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                answer -= dic[s[i]]
            else:
                answer += dic[s[i]]
        return answer+dic[s[-1]]