# 다른 사람의 풀이 참고

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result

# 나의 사고에서 보완할 점은. 그래서 각 start 지점에서, 팰린드롬이면 넣고,
# 아니 이러면 이 다음 팰린드롬을 못하잖아요! 라고 생각할 수 있는데, 그거를 이제 for문을 통해서,
# 각 start 지점마다 또 end 지점을 계산해서, 팰린드롬이면 넣고, 아니면 넘어가는 방식으로 해결했다.



# 나의 사고

# 그 글자에서 expand한 후에 나머지를 다시 dfs
# 그 글자에서 expand안하고, 다음 idx에서 expand,
# 그런데 이렇게 하면 겹쳐버린다. c a b에서.

# c a b 에서,

# a,a,a aa,a aaa

# 한글자씩 자를 수 있다. 왜? 그것도 펠린드롬이니까
# c a c a c a 이렇게 있으면?

# c에서 자르고 갈 수도 있고, -> 자른 다음 DFS
# c에서 안자르면 -> 이게 제일 문제임. 
# 근데 그러면 걔는 무조건 팰린드롬에 포함되어 있어야 함.

# 아 그러니까, 팰린드롬 햇을때 왼쪽을 고려할 필요가 없다. 왜? 왼쪽은 팰린드롬 안된것들, 즉 어차피 잘려야 하는.