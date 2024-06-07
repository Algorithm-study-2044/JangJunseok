# 1차시도. 이렇게 하면 시간초과. n**2

class Solution:
    def candy(self, ratings: List[int]) -> int:
        cand = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                diff = max(0,cand[i-1] - cand[i] + 1)
                cand[i] += diff
                
            for j in range(i,0,-1):
                if ratings[j] < ratings[j-1]:
                    diff = max(0,cand[j] - cand[j-1]+1)
                    cand[j-1] += diff
                else:
                    break
    
        return sum(cand)
    

# 2차시도. 132ms. 25.38% beats.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        cand = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                cand[i] += max(0,cand[i-1] - cand[i] + 1)
        
        # 왜 한번 더 반복해야 하는지? 
        # 왼쪽꺼보다는 레벨이 낮아서 낮게 했는데,
        # 그런데 오른쪽꺼보다는 큰 경우에는 그거보다는 커야 할테니까.
                
        for j in range(len(ratings)-1,0,-1):
            if ratings[j] < ratings[j-1]:
                cand[j-1] += max(0,cand[j] - cand[j-1]+1)
                
        return sum(cand)
        
    

# 3차시도. 다른 풀이. 다른 사람의 풀이 참고.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            # prev > curr
            # 다운 다운 일 경우, 다운은 두개. 그래서. 그 이전의 두개에다가 사탕을 더해줘야 함.
            
            # int(peak >= down)의 의미는 잘 모르겠는데, 

            else:
                up, down = 0, down + 1
                # down의 개수만큼 더해주는거는 이해가 되었음. 

                # 0 1 0 이렇게 되면?
                # 1 2 1 이렇게 된다. 총 4개가 필요.
                # 1 1+(1+1) (1+1) 이렇게 될 것이기 때문이다. peak에서 하나 중복이 됨.
                # 위로 올라갈때 하나 더해주는거 하고, 내려갈때 하나 더해주는거하고 중복이 된다.

                # 그게 왜 그런가 하면. 그 이전꺼에다가 더해줘야 하는것은 맞는데, 

                # 꼭대기에서 내려가는 경우하고
                # 평지에서 내려가는 경우하고 다르다는 것이다.
                # 둘다 1+down해줘야 하는건 맞다.   
                # 그래야지 이전 단계에 있었던 애들 가오를 살려주지.
                # 그런데 이전 단계에서 꼭대기에 있었던 놈들이 있었다면, 그놈들은 이미 꼭대기인데 굳이 가오 안살려줘도 됨.

                # 그런데 down이 2이고 peak가 1인 경우에는? 
                # 이때는 보정을 안하는 이유가 뭘까. 아 첫번째 down에서 한번 보정하고, 그 다음부터는 할 필요가 없나?
                # peak 1 down 2일때 보정을 안하는 이유는.
                # 이때는 봉우리 자체가 높아져야 한다는 것이다. 왜냐하면 그렇게 안하면 오른쪽에 있는 애보다 작아질 수 있으니까.
                
                ret += 1 + down - int(peak >= down)
        
        return ret