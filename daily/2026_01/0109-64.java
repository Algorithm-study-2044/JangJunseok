// 10분. 63%. 경계선 처리 방법 배움. in-place 관련해서 좀 더 생각해볼 수 있음.
// 일차원 배열로도 해결 가능.

class Solution {

  public int minPathSum(int[][] grid) {
    int m = grid.length;
    int n = grid[0].length;
    int[][] dp = new int[m + 1][n + 1];

    for (int i = 0; i < m + 1; i++) {
      for (int j = 0; j < n + 1; j++) {
        if (i == 0 || j == 0) dp[i][j] = Integer.MAX_VALUE;
      }
    }

    for (int i = 1; i < m + 1; i++) {
      for (int j = 1; j < n + 1; j++) {
        if (i == 1 && j == 1) {
          dp[i][j] = grid[i - 1][j - 1];
          continue;
        }
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1];
      }
    }
    return dp[m][n];
  }
}
