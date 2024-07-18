# 2차시도. 다른 사람의 풀이 참고.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = l + (r-l) // 2
            last_pos, balls = position[0], 1
            for i in range(1,len(position)):
                if position[i] - last_pos >= mid:
                    last_pos = position[i]
                    balls += 1
            if balls >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return ans

# 즉 최적의 간격 개수를 찾아야 할때.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            last_position, balls = position[0], 1
            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    last_position = position[i]
                    balls += 1
            
            # 일단 간격 되는대로 넣어본다음에 그게 조건에 맞는지 확인하는 아이디어.
            if balls >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans



#그니까 최대한 떨어져 있어라..이런건데.
# 각 거리상 가장 멀리 떨어질 수 있는곳부터 배치하면 안될까?
# 그걸 계산하려면. nC2 니까 n^^2만큼 비용이 들긴 한다.
# 게다가 71 하면 6이지만, 그 사이에 또 뭐가 들어가버리니까.

# 6일때 최대 거리는. 일단 3이다.
# (max - min) // (m-1) 이렇게 해서 구한다.
# 그러면 1부터 넣어놓고, 그 다음에 1+res가 있나? ㄴㄴ 그러면 그거보다 조금 작은거 넣고
# 이 그거보다 조금 작은거를 어떻게 찾아줄 건가? 예를 들어 1다음 4인데, 4가 없어서 3을 대신 했다..라는것을.
# 게다가 이 방식대로라면, 2에서 시작하는게 어떻게 보면 더 나을 수도 있는데 그거는 어떻게 해결?

# 조합을 구해서 한다면? 조합 구하고 -> 그다음 n만큼.
# 그런데 조합이 비효율적인 이유는? 123보다는 124가 더 우위이다. 
# 123보다 134가 우위라 할 수 있나?

# 그럼 시작과 끝을 정하고 -> n^2
# 최대거리 구한다음에
# 최대거리 근처에 있는 있는 값을 찾아준다?
# 문제는 ceil이나 floor가 아니라, 근처라는 게 문제임.

# 그럼..

