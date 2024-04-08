# 1차시도. 시간초과. 318/322 passed. 
# 시간복잡도는 


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        def calc_stack(arr):
            stack = []
            total = 0
            for index, item in enumerate(arr):
                if item == 0:
                    continue
                if stack:
                    total += (index - stack.pop() -1)
                    stack.append(index)
                else:
                    stack.append(index)

            return total

        maxHeight = max(height)

        for i in range(maxHeight):
            newArr = [1 if item-i > 0 else 0 for item in height]
            res += calc_stack(newArr)
        
        return res
    
# 2차시도. 다른 사람의 풀이 참고.
# dp를 활용.
    
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        right_max[size-1] = height[size-1]
        for i in range(1,size-1):
            left_max[i] = max(left_max[i-1],height[i])

        for i in range(size-2,0,-1):
            right_max[i] = max(right_max[i+1],height[i])

        for i in range(1,size-1):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans
    
# 3차시도. 다른 사람의 풀이 참고.
    
class Solution {
public:
    int trap(vector<int>& height)
    {
        int ans = 0, current = 0;
        stack<int> st;
        while (current < height.size()) {
            # 현재 높이가 스택의 top보다 크다면, 스택의 top을 pop한다.
            while (!st.empty() && height[current] > height[st.top()]) {
                int top = st.top();
                st.pop();
                if (st.empty())
                    break;
                int distance = current - st.top() - 1;
                int bounded_height = min(height[current], height[st.top()]) - height[top];
                ans += distance * bounded_height;
            }
            st.push(current++);
        }
        return ans;
    }
};