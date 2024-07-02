#5:43 시작.

#5:43 시작. 6:07분. 24분 소요. 53ms. 86.44% beats.

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        curr_idx = 0
        for item in s:
            if curr_idx <= len(t) -1 and item == t[curr_idx]:
                curr_idx += 1
        
        return len(t) - curr_idx

#1차시도. 이거는 연속되었다고 가정하지만..
#문제를 잘못 이해했다.

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        res = [0]

        def DFS(curr,idx,sliced):
            if idx > len(t) -1 or sliced[0] != t[idx]:
                res[0] = max(res[0],curr)
                return
            DFS(curr+1,idx+1,sliced[1:])
            
        for i in range(len(s)):
            DFS(0,0,s[i:])

        return len(t) - res[0]



