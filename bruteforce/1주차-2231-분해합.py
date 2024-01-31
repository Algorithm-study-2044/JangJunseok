#1차시도. pass.

def get_each_sums(num):
    result = 0
    cal = 10
    while num != 0:
        month = (num % cal) / (cal / 10)
        result += month
        num -= num % cal
        cal *= 10
    return int(result)

n = int(input())
creator = 0
start = 0

while start < n:
    start += 1
    val = get_each_sums(start)
    if val + start == n:
        creator = start
        break

print(creator)