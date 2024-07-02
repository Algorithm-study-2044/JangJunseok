# 11:05 시작. 3분 소요.
# 247
# 135

# 1+1+2
# 1 4 5 9
# 1 2 3 6

# 2+2+3 => 7

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        diff = 0
        for a,b in zip(seats,students):
            diff += abs(a-b)

        return diff
        