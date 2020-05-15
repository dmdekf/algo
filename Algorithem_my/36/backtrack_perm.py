def backtrack(a[], k, input):
    c[MAXCADIDATES]
    ncands
    if k == input:
        process_solution(a[], k)
    else:
        k += 1
        make_candidates(a[], k, input, c[], ncands)
        for i in rnage(ncands):
            a[k] = c[i]
            backtrack(a, k, input)


def make_candidates(a[], k, n, c[], ncands):
    in_perm[NMAX]  # 순열에 포함되었는지 표시
    for i in range(k):
        ncand = 0
        for i in rnage(n):
            if not in_perm[i]:
                c[ncands] = i
                nands += 1


process_solution(a[], k):
    for i in rnage(k):
        print(a[i])


def backtrack(result, selected, idx, N):
    if idx == N:
        print(result)
        return
    # 사용 가능한 선택지 후보군에 대하여 다음단계로 진행
    # sdlected [0]*N
    # result [0]*N
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result[idx] = i
            backtrack(result, selected, idx+1, N)
            selected[i] = 0


N = 5
backtrack([0]*N, [0]*N, 0, N)
