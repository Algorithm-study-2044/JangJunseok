# 30분 소요. 1030ms. 44.96% beats.
# 스택을 활용한 풀이.

# RLRRLL 이렇게 되어있으면

# 1. R스택이 없는데 L이 나오면 그건 버림. R스택이 있으면 R[-1]과 충돌
# 2. R은 스택에 넣음. 
# 3. RL 충돌. 결과 계산해서 만약 L이 살앗다? Rpop하고 또 다음 R[-1]과. 만약 R스택이 없다? 그러면 그 L은 살은거임.
# 만약 R이 살았다? R은 생명 업데이트한다음에 keep going.

# 끝까지 iterate한다음에 남은 R들은 다 saved한걸로.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        idxs = list(range(1,len(positions)+1))
        zipped = sorted([list(item) for item in zip(idxs,positions,healths,directions)],key=lambda x:x[1])
        right_stack = []
        saved = []
        for item in zipped:
            if item[3] == "L":
                if not right_stack:
                    saved.append(item)
                    continue
                while right_stack:
                    # 왼쪽 오른쪽 충돌시킴
                    curr = right_stack[-1]
                    if curr[2] < item[2]:
                        item[2] -= 1
                        right_stack.pop()
                    elif curr[2] == item[2]:
                        right_stack.pop()
                        item[2] = 0
                        break
                    else:
                        right_stack[-1][2] -= 1
                        item[2] = 0
                        break
                if item[2] > 0:
                    saved.append(item)
            else:
                right_stack.append(item)
        
        for right in right_stack:
            saved.append(right)
        
        return [x[2] for x in sorted(saved,key=lambda x:x[0])]