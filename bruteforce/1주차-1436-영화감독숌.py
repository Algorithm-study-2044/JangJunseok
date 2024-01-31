start = 0
cnt = 0
last = 0
n = int(input())

while cnt != n:
    start += 1
    if "666" in str(start):
        cnt += 1
        last = start
    
print(last)