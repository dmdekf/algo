c, r = map(int, input().split())
num_of_stores = int(input())
store_location = []
for i in range(num_of_stores):
    store_location.append(list(map(int, input().split())))
my_location = list(map(int,input().split()))
if my_location[0] == 1:
    my_pos = [0, my_location[1]]
elif my_location[0] == 2:
    my_pos = [r, my_location[1]]
elif my_location[0] == 3:
    my_pos = [my_location[1], 0]
elif my_location[0] == 4:
    my_pos = [my_location[1], c]
total = 0
for each in store_location:
    if each[0] == 1:
        store_pos = [0, each[1]]
        if my_pos[0] == r:
            one = my_pos[0] + my_pos[1] + store_pos[1]
            two = my_pos[0] + c-my_pos[1] + c- store_pos[1]
            if one>two:
                total += two
            else:
                total += one
        else:
            total += abs(my_pos[0]-store_pos[0]) + abs(my_pos[1]-store_pos[1])
    elif each[0]== 2:
        store_pos = [r, each[1]]
        if my_pos[0] == 0:
            one = store_pos[0] + my_pos[1] + store_pos[1]
            two = store_pos[0] + c - my_pos[1] + c - store_pos[1]
            if one > two:
                total += two
            else:
                total += one
        else:
            total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])
    elif each[0] == 3:
        store_pos = [each[1],0]
        total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])
    elif each[0]==4:
        store_pos = [each[1],c]
        total += abs(my_pos[0] - store_pos[0]) + abs(my_pos[1] - store_pos[1])
print(total)