def f(n, k, s, M, rs):
    global cnt
    global fcnt
    fcnt += 1
    if n == k:
        if s == M:
            cnt += 1
    elif s > M:
        return
    elif s+rs < M:  # 부분집합에 포함된 원소와 남은 모든 원소의 합 비교
        return
    else:
        f(n+1, k, s, M, rs-arr[n])  # arr[n]미포함
        f(n+1, k, s+arr[n], M, rs-arr[n])  # arr[n] 포함


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 55
K = len(arr)
a = [0]*K
cnt = 0
fcnt = 0
f(0, K, arr[0],  M, sum(arr))

print(cnt, fcnt)
