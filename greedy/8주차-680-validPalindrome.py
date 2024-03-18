#1차시도. 실패. 이렇게 하면 문제점은. 어느쪽을 먼저 옮기느냐에 따라서 답이 달라질 수 있다.

class Solution(object):
    def validPalindrome(self, s):

        valid = True
        deletedOnce = False
        start = 0
        end = -1

        for i in range(len(s)//2):
            print(s[start], s[end], i)
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            if not deletedOnce and s[start] == s[end-1]:
                deletedOnce = True
                end -= 1
                continue
            if not deletedOnce and s[start+1] == s[end]:
                deletedOnce = True
                start += 1
                continue


            valid = False
            
        
        return valid
    

# 2차. 다른 사람의 풀이 연구. 
    
# 아이디어는. 일단 일치하지 않으면. 둘 중 하나를 뺐을때, 그거는 palendrome이 되어야 함. 
# 두개가 같다면 계속 비교를 하되.

class Solution:
    def validPalindrome(self, s: str) -> bool:
            p1=0
            p2=len(s)-1
            while p1<=p2:
                if s[p1]!=s[p2]:
                    string1=s[:p1]+s[p1+1:]
                    string2=s[:p2]+s[p2+1:]
                    return string1==string1[::-1] or string2==string2[::-1]
                p1+=1
                p2-=1
            return True