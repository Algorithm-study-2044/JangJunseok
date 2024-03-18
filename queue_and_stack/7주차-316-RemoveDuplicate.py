#2차시도. 다른 사람의 풀이 연구. 근데 잘 이해가 안된다,...

class Solution(object):
    def removeDuplicateLetters(self, s): 
        freq = [0] * 26
        visited = [0] * 26
        
        # 각 문자의 빈도수를 계산한다.
        for ch in s:
            #왜 dict가 아니라, 굳이 list를 사용하는거지?
            freq[ord(ch) - ord('a')] += 1

        unique_letters = ""
        n = len(s)        
        for i in range(n):
            #ord(s[i]) - ord('a') 하는 이유는. 더 보기 쉽게 하려고 인듯하다.
            freq[ord(s[i]) - ord('a')] -= 1
 
            # 이 부분이 잘 이해가 되지 않는다. 한번 어떤애가 나왔으면 뒤에 애는 기회가 없나??
            # 아니다. 어떤 애가 visited로 찍혀도, 그 다음 애가 판단했을때 얘가 쓸모없다 싶으면, 그러면 얘를 제거하고 visited를 다시 reset한다.
            # 그런데 visited가 reset되지 않는 경우는? 먼저 들어간 애가 있는데, 그 애가 그 이전애보다 크다. 그러면 걔는 
            if not visited[ord(s[i]) - ord('a')]:
                
                #unique_letters의 이전글자가 s[i]보다 크면서, 그리고 그 이전글자가 뒤에 또 나온다면, 그 이전글자를 빼준다.
                #왜? 이전글자의 중복의 경우 선택해야 하는데, 이전글자가 뒤에 또 나온다면, 그 이전글자를 빼줘야 한다.
                
                #즉 이렇게 생각한다. 지금 글자보고, 이전글자를 뺄지 말지를 판닪나다. 
                #이렇게 하면 이전글자는 freq가 여러개라도. 항상 하나만 남게 된다.
                #마음만 같아서는 3번째 조건 없이 하고싶지만, 그렇게 하면 
                while unique_letters and unique_letters[-1] > s[i] and freq[ord(unique_letters[-1]) - ord('a')] > 0:
                    visited[ord(unique_letters[-1]) - ord('a')] = 0
                    unique_letters = unique_letters[:-1]

                unique_letters += s[i]
                visited[ord(s[i]) - ord('a')] = 1
        
        return unique_letters