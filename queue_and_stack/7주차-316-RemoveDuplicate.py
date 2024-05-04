#2차시도. 다른 사람의 풀이 연구. 근데 잘 이해가 안된다,...

class Solution(object):
    def removeDuplicateLetters(self, s): 
        freq = [0] * 26
        visited = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        unique_letters = ""
        n = len(s)        

        for i in range(n):
            freq[ord(s[i]) - ord('a')] -= 1

            # 만약 target을 아직 안넣었다면, 어디에 넣을까? 게속 끝에 글자랑 비교해본다.
            # b가 두개 있을때, 두번째 b의 입장에서는 앞에 b가 포함이 안되었을수도 있다.
            # visited는 거의 확정인거다. visited가 1이면, 뒤에거를 더이상 고려하지 않는다.

            # 순서를 고려할때 뒤에 요소를 가지고 고려하는게 아니라, 일단 넣어봤을때, 


            # freq[ord(unique_letters[-1]) - ord('a')] > 0 이 조건은, 뒤에 더 나올때만 빼줄 수 있다는 것이다.   
            # 그러니까 하나 넣었을때. 뒤에 또 나온다면, 그 이전글자를 빼줘야 한다.

            if not visited[ord(s[i]) - ord('a')]:
                while unique_letters and unique_letters[-1] > s[i] and freq[ord(unique_letters[-1]) - ord('a')] > 0:
                    visited[ord(unique_letters[-1]) - ord('a')] = 0
                    unique_letters = unique_letters[:-1]

                unique_letters += s[i]
                visited[ord(s[i]) - ord('a')] = 1
        
        return unique_letters