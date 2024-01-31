n = int(input())

start = n // 5
noFlag = False

while start >= 0:
    if (n - start * 5) % 3 == 0:
        print(start + (n-start * 5) // 3)
        noFlag = True
        break
    
    start -= 1

if not noFlag:
    print(-1)

