T = 10
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(100):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][-1-i]
    result.append(diagonal_1)
    result.append(diagonal_2)

    for i in range(len(arr)):
        row_temp = 0
        col_temp = 0
        for j in range(len(arr)):
            row_temp += arr[i][j]
            col_temp += arr[j][i]
        result.append(row_temp)
        result.append(col_temp)
      
    print('#{} {}'.format(n, max(result)))
