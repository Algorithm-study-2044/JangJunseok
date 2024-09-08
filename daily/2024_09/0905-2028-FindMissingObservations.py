# 11분 소요.
# 그러니까 (len(rolls)+n) * (sum(rolls) + sum(output)) = mean이 되도록 해야한다는

# n개의 합이 --가 되도록.
# 단 각 요소가 1이상 6 이내에서.

# 그럼 각 요소당 1씩 주고,
# 첫요소에 6 준다음에, 
# 이런식으로 하면 되지 않나.

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean * (len(rolls) + n) - sum(rolls)
        # 일단 1씩 넣어주고,
        target -= n

        if target < 0:
            return []

        output = [1] * n
    
        for i in range(len(output)):
            if target == 0:
                return output
            val = min(target, 5)
            output[i] += val
            target -= val
        
        # 그래도 target이 남았다? 그러면 배분이 안되는거고,
        if target > 0:
            return []
        return output