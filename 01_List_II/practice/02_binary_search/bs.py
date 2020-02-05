def find(total, target):
    cnt = 1
    start = 1
    end = total
    # middle = int(end + start / 2) == end + start // 2
    middle = (end + start) // 2
    # 1~9까지의 숫자 중 target이 3일 경우
    # m :5
    #target = 3
    while middle != target:
        if target > middle:
            start = middle
        else:
            end = middle
        middle = (end + start) // 2
        cnt +=1
        # print(cnt)

    return cnt

print(find(10,3))
