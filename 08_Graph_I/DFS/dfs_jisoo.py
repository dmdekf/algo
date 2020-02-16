node, line = map(int, input().split())
visited = []
stack = []
lines = [list(map(int, input().split())) for _ in range(line)]
 # 시작 노드 잡기!
stack += lines[0]
visited += lines[0]
lines.pop(0)
while len(visited) != node:
    for l in lines:
        if l[0] == stack[-1] and l[1] not in visited:
            visited.append(l[1])
            stack.append(l[1])
            lines.remove(l)
            break
    else:
        if stack:
            stack.pop()
print(*visited)