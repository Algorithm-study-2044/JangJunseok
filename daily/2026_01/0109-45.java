// 난-42.3%. 풀이-35.25%
// 아이디어는 그리디하게 접근.
// 그러나 n-1에서 break되도록 해서 계속 무한루프가 났었다. 결국 gpt에게 물어보고. 그 부분 고쳐서 해결.

class Solution {

  public int jump(int[] nums) {
    int hopCount = 0;
    int start = 0;
    int n = nums.length;
    while (start < n - 1) {
      int max_val = Integer.MIN_VALUE;
      int max_idx = start;
      // 근데 여기서 i + nums[start]가 n-1보다 클수도 있다.
      for (int i = 1; i <= nums[start]; i++) {
        if (start + i >= n - 1) {
          // 이러면 넘었다는 것.
          max_idx = start + i;
          break;
        }
        if (nums[start + i] + i > max_val) {
          max_val = nums[start + i] + i;
          max_idx = start + i;
        }
      }
      start = max_idx;
      hopCount++;
    }
    return hopCount;
  }
}
