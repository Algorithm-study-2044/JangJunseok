# 2차시도. 성공. 13분 소요. 40ms.

# 15*p + a이고 28*q + b이고 19*r + c이다.
# 15*p + a = 28*q + b = 19*r + c = year
# year - a는 15의 배수여야하고, year - b는 28의 배수여야하고, year - c는 19의 배수여야한다.

# 그럼 최소 min(a,b,c)에서 시작해서, year가 이 3 조건을 만족하는지를 체크.

a,b,c = map(int,input().split())
year = min(a,b,c)

while True:
    
    if (year-a) % 15 == 0 and (year-b) % 28 == 0 and (year-c) % 19 == 0:
        break

    year += 1

print(year)


#1차시도. 시간초과.

a,b,c = map(int,input().split())


year = 0
q,w,e = 0,0,0

while True:
    year += 1

    q += 1
    w += 1
    e += 1

    if q > 15:
        q = 1
    if w > 28:
        w = 1
    if e > 20:
        e = 1
    
    if q == a and w == b and e == c:
        break

print(year)

