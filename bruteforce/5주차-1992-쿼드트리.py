
# 10시 40분 시작. 1차시도 실패. 틀렸다고 함.

# 어디서 시간을 많이 썼냐면.. 일단 len(arr[0]) // 2이렇게 해야하는데, 그걸 안해서 한번
# 그리고 map(int,str) 여기서 한번
# 그리고 subarray == 0 할때 array의 구조를 잘못 생각해서, 헷갈려서 한번.

# 0 (0011) (0(0111)01) 1
# 이렇게 네개의 부분으로 나뉜다는 것.

# DFS로, 계속 계속 들어가면서, 
# 주어진 array를 4분할로 나누는 함수가 필요.

# [[8],[8],[8],[8]..]
# -> [[4],[4],[4],[4]] and [[4],[4],[4],[4]] and 
# [[0],[0],[1],[0]]

# 문제는, 이렇게 나눴을때, 이 친구가 다 0이면, 굳이 이거를
# 하위로 나누지 않고, 바로 return 하면 됨.

# DFS

# 4분할 전에, 4분할이 안되는 single element의 경우,
# 그냥 그 각각의 값을 return 해준다.

# 4분할 한다.
# 4분할 값이 모두 같다? 그러면 0 or 1을 return 한다.
# 4분할 값을 DFS로 돌린다. 그리고 그 값을 ()로 


def make_half(arr):
    p1 = []
    p2 = []
    for item in arr:
        p1.append(item[0:len(arr[0])//2])
        p2.append(item[len(arr[0])//2:])
    
    return (p1,p2)
    

def DFS(arr):
    if len(arr) == 1:
        return arr[0][0]

    first_half = arr[0:len(arr)//2]
    second_half = arr[len(arr)//2:]

    f1, f2 = make_half(first_half)
    f3, f4 = make_half(second_half)

    total = [f1, f2, f3, f4]

    if all([all([sub == 0 for sub in item[0]]) for item in total]):
        return 0

    elif all([all([sub == 1 for sub in item[0]]) for item in total]):
        return 1

    res = "("
    res += str(DFS(f1))
    res += str(DFS(f2))
    res += str(DFS(f3))
    res += str(DFS(f4))
    res += ")"

    return res


n = int(input())

df = []
for _ in range(n):
    a = input()
    df.append(list(map(int,a)))

print(DFS(df))



# 2차시도. 다른 사람의 풀이 참고.

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


# 처음에 0,0 체크한다. 다 똑같은 1이다? 그러면 1 출력.
# 다 똑같은 0이다? 그러면 0 출력.

# 만약 다르다? 글면 4분할로 나눈다.

def dnc(x, y, n):
    check = graph[x][y]

    # 하나라도 check != graph[i][j] 이면, check를 -1로 바꾼다.
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dnc(x, y, n)  # 오른쪽 위
        dnc(x, y + n, n)  # 왼쪽 위
        dnc(x + n, y, n)  # 오른쪽 아래
        dnc(x + n, y + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dnc(0, 0, n)



# 3차시도. 다른 사람의 풀이 적용.

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

def DFS(x,y,n):

    check = graph[x][y]
    for i in range(x,x+n):
        #그러면 x+n+1해야하는거 아닌가? 이게 변의 길이가 n이니까.
        #아 근데 영상의 크기 n이라는게, 숫자 8개가 주어진다는 말임. 그러니까 인덱스번호는 0부터 n-1까지 해서 n개가 되겠지.
        for j in range(y,y+n):
            if graph[i][j] != check:
                check = -1
                break

    if check == -1:
        k = n//2
        print("(",end="")
        DFS(x,y,k)
        DFS(x,y+k,k)
        DFS(x+k,y,k)
        DFS(x+k,y+k,k)
        print(")",end="")
    elif check == 1:
        print(1,end="")
    elif check == 0:
        print(0,end="")

DFS(0,0,n)


    



    # what to return. 
    # 다 똑같은 1이면 1
    # 다 똑같은 0이면 0
    # 다르면, 4분할로 나눠서 재귀호출.