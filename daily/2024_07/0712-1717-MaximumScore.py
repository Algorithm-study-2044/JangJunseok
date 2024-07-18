# 5:14. 1차시도. 시간초과. 54/76에서 걸림.
# 왜? 이거는 지운다음에, 다시 그 문자열 처음부터 재귀돌면서 계산하기 때문에.

# 그러면 그건 어떻게 하는데?

# 접근 자체는 좋았는데, 시간 복잡도를 줄여야 한다.

# baba 일케 있으면? 혹은 abab 이렇게 있으면?
# 어떤 경우에도 큰놈을 먼저 지워버리는게 좋다.
# 그러면, ba지워버리고, 합친다음에, 점수와 나머지 retur한다음에,

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def get_rest(s,curr,matcher,point):
            if len(s) < 2:
                return (s,curr)

            for i in range(len(s)):
                if s[i:i+2] == matcher:
                    return get_rest(s[:i]+s[i+2:],curr+point,matcher,point)
            
            return (s,curr)
        
        if x >= y:
            # 이러면 재귀 돌면서, ab를 다 지워버린다. 
            rest,point = get_rest(s,0,"ab",x)
            # 그 다음에, ba 를 해본다.
            rest,point = get_rest(rest,point,"ba",y)
        else:
            # 이러면 ba를 다 지워버린다.
            rest,point = get_rest(s,0,"ba",y)
            rest,point = get_rest(rest,point,"ab",x)
        
        return point
    

# 다른 사람의 풀이.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        # 아 그러니까, 일단 넣어둔다음에, 일치한다? 그러면 빼는 식으로 하면 되는거구나.
        # 결국 관심사는 새롭게 들어오는 놈이 stack처럼 쌓이는 구조니까.
        # abababa
        # bbaa

        # removing first top substrings cause they give more points
        stack: list[str] = []
        for char in s:
            if char == top[1] and stack and stack[-1] == top[0]:
                res += top_score
                stack.pop()  # delete first char of this substring
            else:
                stack.append(char)

        # removing bot substrings cause they give less or equal amount of scores
        new_stack: list[str] = []
        for char in stack:
            if char == bot[1] and new_stack and new_stack[-1] == bot[0]:
                res += bot_score
                new_stack.pop()
            else:
                new_stack.append(char)

        return res
    

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(string: str, target: str) -> tuple[str, int]:
            # We convert string to list because in this language strings are immutable and so complexity is still O(n) but in languages where strings are mutable this will be O(1)
            string = list(string)
            write_ind = 0
            counting = 0

            for char in string:
                string[write_ind] = char
                write_ind += 1

                if write_ind >= 2:
                    if string[write_ind - 1] == target[1] and string[write_ind - 2] == target[0]:
                        counting += 1
                        write_ind -= 2

            return ("".join(string[:write_ind]), counting)

        res = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

        remainder, c = remove_pairs(s, top)
        res += c * top_score
        _, c = remove_pairs(remainder, bot)
        res += c * bot_score

        return res