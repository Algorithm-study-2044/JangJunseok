# 4:07 시작. 2분 소요. 39ms. 97.74% beats.

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        depth = 0
        for c in logs:
            if c == "../":
                depth = max(1, depth)
                depth -= 1
            elif c != "./":
                depth += 1
        
        return depth