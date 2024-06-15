# 5:38. 882ms. 7.98% beats. 30분 정도 소요.
# 다시 고쳐서. 804ms. 94% beats. 가장 적은 인덱스만 기록해주면 된다.

# good subarray가 있기만 하면 되는거다.
# 원래대로라면. [23,2,4,6,7]에서
# 23 2, 23 2 4, 23 2 4 6 하고
# 근데 이것도 마찬가지다. 23 2 4 6 까지 봤을때, 2 4 6도 볼 수 있다는 것이다. 어떻게? prefix_sumd을 활용해서
# 그런데 하나 알아야 할 것은, length가 적어도 두개 이상이어야 한다는 것.
# 그렇게 하려면. idx까지 같이 기록해줘서, prefix_sum % k == 3 이다. 근데 3뺄 수 있나요?
# ㅇㅇ 그런데 idx차이가 2이상인가요? -> 그러면 true를 return 하자는것.

# 어디서 막혔나면. 이게 배수라서. k=0도 된다는 점이었고.
# 그래서 5 0 0 0 같은 테스트케이스에서 막혔었음. 왜? idx가 같아서 계속 업데이트해주어서. 
# 그러니까 코드가 조금 잘 못되었따는점,

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        prefix_sum = 0
        prefix_dict = {0:-1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum % k in prefix_dict and i - prefix_dict[prefix_sum % k] >= 2:
                return True
            
            if prefix_sum % k not in prefix_dict:
                prefix_dict[prefix_sum % k] = i

        return False