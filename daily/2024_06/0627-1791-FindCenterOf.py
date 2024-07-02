# 3:30 시작. 5분 소요. 654ms. 52.79% beats. 
# easy 문제였음.

# 모든 노드와 연결되어 있다.
# 즉 처음에 노드를 보고, 후보 둘 있다고 할때,
# 그 다음을 보고 버리면 되는거다.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
    