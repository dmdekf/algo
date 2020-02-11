h, v = map(int,input().split())
N = int(input())
store = []
for n in range(N):
    s = list(map(int, input().split()))
    store.append(s)
d_p, dis = map(int, input().split())
sum0 = 0
for n in range(N):
    if d_p == 1:
        if store[n][0] == 3:
            short = store[n][1]+dis
        elif store[n][0] == 4:
            short = store[n][1]+(h-dis)
        elif store[n][0] == 2:
            short = min(store[n][1] + dis + v, 2*h - store[n][1] - dis + v)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 2:
        if store[n][0] == 3:
            short = v-store[n][1]+dis
        elif store[n][0] == 4:
            short = v-store[n][1]+(h-dis)
        elif store[n][0] == 1:
            short = min(store[n][1] + dis + v, 2*h - store[n][1] - dis + v)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 3:
        if store[n][0] == 1:
            short = store[n][1]+dis
        elif store[n][0] == 2:
            short = store[n][1]+(v-dis)
        elif store[n][0] == 4:
            short = min(store[n][1] + dis + h, 2*v - store[n][1] - dis + h)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 4:
        if store[n][0] == 1:
            short = h-store[n][1] + dis
        elif store[n][0] == 2:
            short = h-store[n][1] + (v - dis)
        elif store[n][0] == 3:
            short = min(store[n][1] + dis + h, 2 * v - store[n][1] - dis + h)
        else:
            short = abs(store[n][1] - dis)
    sum0 += short
print(sum0)