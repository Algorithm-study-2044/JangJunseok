# 7:19. 8:00. 41분 소요. 155ms. 49.87% beats.

# 생각한 방법.

# on은 안되고, on2인데, 뒤에꺼를 같이 계산하기 보다는,
# words에다가 한 글자만 삽입하려면, 글자수대로 정렬하는게.
# 각 요소에서, 연결할 수 있는 이전 요소 + 
# 어차피 한개짜리, 두개짜리, 세개짜리 이렇게 계층을 이룬다.

# 1: a b
# 2: ba
# 3: bca bda 
# 4: bdca

# bdca 입장에서, bca bda만 보면 됨. 이 둘 중에서 가능한 조합을 찾고, 
# 그 중에서 가장 큰 놈을 찾으면 되는 거임.

from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        len_dict = defaultdict(list)
        cnt_dict = defaultdict(int)

        for w in words:
            len_dict[len(w)].append(w)

        def is_predecessors(sm,big):
            if len(sm) + 1 != len(big):
                return False
            i,j = 0,0
            shift = False
            while i <= len(sm) -1:
                if sm[i] != big[j]:
                    if not shift:
                        shift = True
                        j += 1
                        continue
                    else:
                        return False
                i += 1
                j += 1
            
            return True
            
        # df = [[a,b],[ba],[bca,bda],[bdca]]
        df = [item[1] for item in sorted(len_dict.items(),key=lambda x:x[0])]
        for idx, items in enumerate(df):
            for i in range(len(items)):
                if idx == 0:
                    cnt_dict[items[i]] = 1
                    continue
                best_length = 0
                for prev_item in df[idx-1]:
                    if is_predecessors(prev_item, items[i]):
                        best_length = max(best_length, cnt_dict[prev_item])
                # 이 부분에서 실수했다. best_length를 구하는거는 모든 item에 대해서 해줘야 하는데, 각 아이템마다 덮어씌워버렸다.
                # 디버깅할때 빨리 찾아주자.
                cnt_dict[items[i]] = best_length + 1
        return max(cnt_dict.values())   