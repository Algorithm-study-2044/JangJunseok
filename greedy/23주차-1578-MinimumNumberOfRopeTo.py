# 3:19 시작. 15분 소요. 46.99% beats. 792ms. 

# 생각한 과정.

# 한 세트에서 없앴을때 그게 다른 세트에 도움을 주는 경우가 있을까?
# 그냥 ppppp 이렇게 나열되어 있다면,
# 코스트 제일 큰 거 빼고 다 없애버리면 그만 아닌가.
# 그로 인해서 다른 갈라져있던 부분이 합쳐질 가능성은? 없다.

# 현재 문자 저장.
# 현재 cost를 다 더해주고,
# max_cost만 가지고 있다가,
# color 바뀌었는데 combo가 2 이상이다?
# 1. 더한거에서 min빼고 나머지 다 res에 더하기
# 2. 더한거 reset.

# 마지막 부분에서는 어떻게 되나? 문자가 바뀌지 않은 경우도 해결해줘야 하는데.
# combo가 2 인지 아닌지 부분을 마찬가지로 적용해주면 된다.

# 근데 문제는, 여러개 겹치는 경우만 있어야 한다는 거
# 하나만 있을때는 삭제하면 안되니까.
# 그래서 combo라는 변수도 같이 만들어줬음.

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        combo = 0
        curr_chr = ""
        curr_sum = 0
        curr_max = 0
        res = 0

        for i in range(len(colors)):
            if curr_chr != colors[i]:
                if combo >= 2:
                    res += (curr_sum - curr_max)
                curr_max = 0
                curr_sum = 0
                combo = 0
                
            curr_chr = colors[i]    
            combo += 1
            curr_max = max(curr_max, neededTime[i])
            curr_sum += neededTime[i]
        
        if combo >= 2:
            res += (curr_sum - curr_max)
        
        return res