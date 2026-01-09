// 5시 37분.

// n 입장에서,
// dp[n-1]을 n-1을 포함한 largest sum subarray라고 한다면.
// dp[n]은, dp[n-1] + nums[i] 와 nums[i]를 비교해서,
// 모두 dp를 구한 다음에, 한번 순회해서 max값을 구해준다.

// 근데 이거는 암기식이다. 왜 dp인지부터 생각해보자.
// 그러면 마이너스가 보이면, 거기서 끊고 다시 시작해야한다. 왜냐하면 마이너스가 있는 순간부터, 그 왼쪽거보다는 항상 작을테니까.

// 근데 마이너스를 감수하고 오른쪽을 먹어야 하는 상황도 있지않나. 5 -3 4
// 그래서 총합을 보는거다.

// 처음에 -2부터 시작.
// [-2, 1, -2, 4, 3, 5, ]
// -2를 가져갈래? 아니면 그냥 거기서 시작할래.

import java.util.Arrays;

class Solution {

  public int maxSubArray(int[] nums) {
    int n = nums.length;
    int[] dp = new int[n];
    for (int i = 0; i < n; i++) {
      if (i == 0) {
        dp[i] = nums[i];
        continue;
      }
      dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
    }
    return Arrays.stream(dp).max().getAsInt();
  }
}
