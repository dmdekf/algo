def backtrack(arr, idx, selected, sum_num):
    global targetsum_num
    if sum_num > targetsum_num:
        return

    if idx == len(arr):
        # 총합이 10인 경우에만 , 출력
        if sum_num == targetsum_num:
            for i in range(len(arr)):
                if selected[i]:
                    print(arr[i], end=" ")
            print()
        return

    selected[idx] = 1
    backtrack(arr, idx+1, selected, sum_num+arr[idx])

    selected[idx] = 0
    backtrack(arr, idx+1, selected, sum_num)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_len = len(arr)
targetsum_num = 10
backtrack(arr, 0, [0]*arr_len, 0)
