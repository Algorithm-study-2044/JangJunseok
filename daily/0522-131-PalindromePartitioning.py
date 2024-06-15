# 10:20 시작. 1차시도 성공. 507ms. 12.59% beats.
# 다른 사람의 풀이도 한번 참고할 것.

# a ? -> yes. then split. the next. DFS
# aa ? -> yes. then split. the next. DFS.
# aab ? -> yes. then split. no left? -> then append to output

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(arr):
            n = len(arr)
            if n % 2 == 1:
                l,r = n//2, n//2
            else:
                l,r = n//2-1, n//2
            
            while l >= 0 and r <= n-1:
                if arr[l] != arr[r]:
                    return False
                l -= 1
                r += 1
            return True

        def DFS(current,arr):
            if len(arr) == 0:
                res.append(current)
                return
            
            for i in range(len(arr)):
                if isPalindrome(arr[:i+1]):
                    DFS(current+["".join(arr[:i+1])],arr[i+1:])
        
        DFS([],list(s))

        return res


# 다른 사람의 풀이.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self._backtrack(s, 0, [], result)
        return result

    def _backtrack(self, s: str, start: int, path: List[str], result: List[List[str]]):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if self._is_palindrome(s, start, end):
                path.append(s[start:end+1])
                self._backtrack(s, end+1, path, result)
                path.pop()

    def _is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True