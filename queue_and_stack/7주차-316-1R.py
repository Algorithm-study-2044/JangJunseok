#9:15

class Solution(object):
    def removeDuplicateLetters(self, s):
        unique_letters = ""
        freq = [0] * 26
        visited = [False] * 26

        for i in s:
            freq[ord(i)-ord("a")] += 1
        
        for i in range(len(s)):
            target = s[i]
            print(target,visited[ord(target)-ord("a")],unique_letters)
            # 앞에 겹치는 친구가 없을때.
            if not visited[ord(target)-ord("a")]:
                # 즉 뒤에 똑같은게 있어서, 바로 끝에 있는 친구를 뺄 수 있으면 빼준다.
                while unique_letters and unique_letters[-1] > target and freq[ord(unique_letters[-1])-ord("a")] > 0:
                    print(unique_letters[-1])
                    visited[ord(unique_letters[-1])-ord("a")] = False
                    unique_letters = unique_letters[:-1]
            
                unique_letters += target
                visited[ord(target)-ord("a")] = True
            
            freq[ord(target)-ord("a")] -= 1

        
        return unique_letters