class Solution {

  public int maxProfit(int[] prices) {
    // 1. 초기값 설정: 첫 번째 날의 가격을 일단 최솟값으로 잡습니다.
    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.length; i++) {
      // 2. 현재 가격이 지금까지의 최솟값보다 작으면 갱신
      if (prices[i] < minPrice) {
        minPrice = prices[i];
      }
      // 3. 현재 가격에서 최솟값을 뺀 값이 현재 최대 이익보다 크면 갱신
      else if (prices[i] - minPrice > maxProfit) {
        maxProfit = prices[i] - minPrice;
      }
    }

    return maxProfit;
  }
}
