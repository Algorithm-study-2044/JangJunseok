# 상수 공간 복잡도를 사용하는 방법에 대해서..

# 비트 연산을 활용한다. XOR.
# 근데 어떻게 XOR을 활용한다는 생각을 하지 ㅅ발?
# 그 이유는. 겹치는 애들같은 경우에는 XOR을 하면 0이 되어서 사라지기 때문이다.

# 그렇기 때문에 거기까지 오면. 그나마 해야할것은, bit_pos_dif를 생각하는것이 될 것이다.

# 2 3 2 이렇게 있으면 2가 남지 않아야 한다고 하지만.
# 1 10 -> 11 이렇게 되네. 음.. 그러면 결국 3이 남긴 하느눅나.
# XOR 연산에 대해서는, 결합법칙이 성립한다.

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        overall_xor = 0
        for n in nums:
            overall_xor ^= n

        first_group_xor = 0
        second_group_xor = 0

        bit_pos_dif = 0

        # 여기에는 두 숫자가 xor 되어있음.
        # 만약에 1이다? 그럼 두 숫자가 같은거고.
        # 0이다? 그럼 두 숫자가 다른거임.

        # 그렇기 때문에 숫자를 구분할 수 있는 비트까지 bit_pos_dif를 땡겨주고.
        # 그 다음에 그걸 가지고 두 숫자를 구분ㅎ주는거임.
        while (overall_xor >> bit_pos_dif) & 1 != 1:
            bit_pos_dif += 1

        # num을 두가지 그룹으로 구분하려고 함. 어떻게 구분할건데?
        # 특히 이 구분에 따라서 하나만 있는 두개의 숫자가 서로 구분이 되어야 함.

        for num in nums:
            if (num >> bit_pos_dif) & 1 == 1:
                first_group_xor ^= num
            else:
                second_group_xor ^= num

        return [first_group_xor, second_group_xor]