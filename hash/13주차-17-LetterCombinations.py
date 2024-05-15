
# 2차시도. 다른 사람의 풀이 참고.
# 역시 DFS+ 백트래킹으로 푸는 것은 맞다.
# 근데 어떤 조건도 없고. 그냥 DFS 아닌가. 그래도 종료가 있다고 하니 이걸 백트링이라고 보는 듯 함.
# 근데 DP로 풀 여지는 없을까. 2323의 경우.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return res


# 17번. 10:37 시작. 1차시도. 실패. 다른 사람의 풀이 참고.

phone = {
    2: ["a","b","c"],
    3: ["d","e","f"],
    4: ["g","h","i"],
    5: ["j","k","l"],
    6: ["m","n","o"],
    7: ["p","q","r","s"],
    8: ["t","u","v"],
    9: ["v","x","y","z"]
}

class Solution(object):
    def letterCombinations(self, digits):
        def DFS(next_num,stack):
            # 일단 넣고, defaultdict에 그 결과를 넣어준다. stack에는 이전, 
                stack.append(phone[next_num]) 
                idx = "".join(stack)
                phone[idx].append()
            

# 2가 있고 그 다음이 3이다.
# 그러면 23번 인덱스에다가, 
# 예를 들어서 2323 이렇게 나왔다고 치면, 
# 원래대로라고 한다면 3**4 이겠지만.
# 23까지 계산한다음에 그걸 hashtable에 넣어놓고 보면, 뒤에꺼는 계산 ㄴㄴ해. 그러니까 3**2만큼. 
# 2345 이렇게 있으면, 23 저장. 234 저장. 2345 저장 이렇게 되어야 하지 않겠나.
# 아니 근데 34 도 저장해야하고, 345도 저장해야할거고. 그래야
# 2345345 이렇게 있을때 뒤에거를 계산 안하지.

# 234545 도 마찬가지일테고.
# 어떻게 하면 234545를 23 45 45 로 분리할 수 있을까.
