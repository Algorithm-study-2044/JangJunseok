# 11:21 -> 44분. 1차시도. 실패.

# 기본적으로 두개를 고르면, 그 사이에 있는 막대는 고려하는 의미가 없다.
# 그럼 그냥 높이 제일 큰거 고르면 되지않아? 라고 하지만, 그 사이 거리도 중요하다는 것이다.
# dp로 접근해야 하나?

# current 입장에서, 오른쪽에 있는 자기보다 낮은 애들중 가장 거리가 긴 애들이 max값이 되나?
# 이것도 정확히는 알 수 없다. 왜냐하면 높이가 더 영향을 많이 줄 수도 있기 때문.

# 한번 쭉 돌면서 index를 나열하고,
# 해당 index끼리? 아니다. 이것도 안된다.

# 그러면 가로 길이 1부터 n-1까지 쟤어볼까? 그럼 그것도 시간복잡도 n**으로 수렴.

# 오른쪽에 있는 자기보다 낮은 애들만 가져와서, 계산한다?

# class Solution(object):
    # def maxArea(self, height):


# 2차시도. 다른 사람의 풀이 참고.

class Solution(object):
    def maxArea(self, height): 
        left = 0
        right = len(height) -1
        maxArea = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)

            # 아마 이 부분이 중요한것 같다. 일단 높이가 낮은 쪽을 옮겨야지, 넓이가 커질 수 있으니까.
            # 그런데 궁금한 것은, 반대 케이스는 없냐는 것이다. 낮고 높을때, 높은거를 옮겨서 넓이가 커질 수는 없는걸까>?
            # 어차피 높이 자체는, 낮은쪽으로 결정이 된다. 그러니까 어찌됐건 낮은 쪽을 옮겨야 변한다는 말이다.

            # 높은 쪽을 옮기면 높이가 더 높아지든 낮아지든, 원래 높이보다는 높아질 수 없다.
            # 이러한 통찰을 바탕으로 낮은쪽만 옮긴 다음에, 넓이를 계산해서 max값을 갱신하는 것이다.
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
