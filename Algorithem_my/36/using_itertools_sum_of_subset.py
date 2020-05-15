from itertools import combinations
arr = [i for i in range(1, 11)]
for i in range(len(arr)+1):
    for p in combinations(arr, i):
        if sum(list(p)) == 55:
            print(list(p))
