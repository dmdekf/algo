T = int(input())
for tc in range(1, T+1):
    d = input()
    dlen = len(d)
    l1 = '.' 
    l2 = '.'  
    l3 = '#'

    l1 +='.#..'*dlen
    l2 +='#.#.'*dlen
    for i in d:
        l3 +='.'+ i + '.#'
        
    print(l1)
    print(l2)
    print(l3)
    print(l2)
    print(l1)