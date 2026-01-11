// 3:37 -> 50. 13분. 56.2% 난이도. 42.04% beats.

// 포인트 입장에서, 가장 최대값은. 왼쪽에서 가장 작은 값이다.
// 매 점마다 왼쪽으로 전부 순회할 필요 있나.
// 그 값을 재활용 가능하다.
// 그래서 다 구한다음에, max 값을 구해주면 된다!

class Solution {

  public int maxProfit(int[] prices) {
    int n = prices.length;
    int[] dp = new int[n];
    dp[0] = prices[0];
    for (int i = 1; i < n; i++) {
      dp[i] = Math.min(dp[i - 1], prices[i]);
      // 참고할때는 -1 값을 참고하면 된다.
    }
    int max_val = Integer.MIN_VALUE;
    for (int i = 1; i < n; i++) {
      max_val = Math.max(max_val, prices[i] - dp[i - 1]);
    }
    return Math.max(max_val, 0);
  }
}
