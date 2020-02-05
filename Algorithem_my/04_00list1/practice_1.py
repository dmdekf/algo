import random
# 연습문제 1
m = n = 5
arr = [[0]*m]*n
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] = random.choice(range(25))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result_list = []
# 7 : [1, 1]
# 2: [ 0,1], 6:[1, 0], 8 [1, 2], 12 : [2, 1]
print(arr)
for x in range(len(arr)):
    for y in range(len(arr[0])):
        result = 0
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < 5 and 0 <= temp_y < 5:
                result += abs(arr[temp_x][temp_y]-arr[x][y])
        result_list.append(result)
