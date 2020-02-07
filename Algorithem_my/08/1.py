import sys

sys.stdin = open('1.txt')

def rotate_90(arr, N):
    arr2 = [[0 for j in range(N)] for i in range(N)]
    for x in range(N):
        for y in range(N):
            arr2[y][N-1-x] = arr[x][y]
    return arr2
def change(arr, N):
    newarr=[]
    for j in range(len(arr)):
        temp = []
        for i in range(len(arr) - 1):
            # 다음숫자와 숫자가 같은 경우
            if arr[i][j] == arr[i + 1][j]:
                total = arr[i][j] + arr[i + 1][j]
                temp.append(total)
                arr[i + 1][j] = -1
            # 숫자가 0일 경우
            elif arr[i][j] == 0:
                count = 0
                for k in range(i + 1, len(arr)):
                    if arr[k][j] != 0:
                        if i != 0 and arr[i - 1][j] == arr[k][j]:  #####
                            del temp[-1]
                            temp.append(arr[i - 1][j] + arr[k][j])
                            arr[k][j] = -1
                        break
                    else:
                        count += 1
                if count == len(arr) - i - 1:
                    temp.append(arr[i][j])
                    arr[i][j] = -1  ###
            # 다음숫자와 현재 숫자가 다를 경우
            elif arr[i][j] != arr[i + 1][j] and arr[i][j] > 0:
                temp.append(arr[i][j])
        if arr[-1][j] >= 0:
            temp.append(arr[-1][j])
        if len(temp) < N:
            for i in range(N - len(temp)):
                temp.append(0)
        newarr.append(temp)
    return newarr


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N, direction = map(str, input().split())
    arr = []
    N = int(N)
    for i in range(N):
        arr.append(list(map(int, input().split())))
    #Up일때
    if direction == "left":
        arr = rotate_90(arr, N)
    print(arr)
    
    arr2= change(arr,N)
    arr3 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(arr2[i][j])
        arr3.append(temp)
    for i in arr3:
        print(*i)

    # print(arr)
    