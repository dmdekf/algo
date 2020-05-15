def backtrack(selected, idx, input):
    # selected : 각 노드의 선택여부를 판단하는 배열
    # idx : 깊이
    # input : 목표 집합 개수
    candidates = [0] * 2  # 선택할 수 있는 선택지는 선택 O/X 두가지
    if idx == input:
        for i in range(input):
            if selected[i]:
                print(i, end=" ")
                print(arr[i], end=" ")
        print()
        return
    else:
        n_candidate = make_candidate(candidates)
        for i in range(n_candidate):
            selected(idx) = candidates[i]
            backtrack(selected, idx+1, input)


def make_candidate(cadidates):
    candidates[0] = 1
    candidates[1] = 0
    return 2


arr = ["a", 'b', 'c', 'd', 'e']
N = 5
backtrack([0]*N, 0, 5)
