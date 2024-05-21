# 03:15 시작. 15분. 53ms. 46.48% beats. (난이도 58%)

# 같은 표를 받은 사람이 있으면, 그 다음 등급 몇표 받았는지를 체크해서 계산한다.
# (A,(-5,-3,-2)) 이렇게 하면 안되나?
# 그러면 key=lambda x:x[1] 이렇게 해서, 딱 나열이 되지 않나

# 그러면 문제는, 이 배열 자체를 구하는 것이 되겠네.
# A: [-5,-3,-2] 이렇게 해줘도 뭐.

class Solution(object):
    def rankTeams(self, votes):

        dic = {}
        total = len(votes[0])

        for vote in votes:
            for rank in range(len(vote)):
                char = vote[rank]
                if char not in dic:
                    dic[char] = [0] * total
                dic[char][rank] -= 1
        
        return "".join([item[0] for item in sorted(dic.items(),key=lambda x:(x[1],x[0]))])

