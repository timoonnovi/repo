def circle(i, m):
    h = i + 1
    if h >= m:
        h = h % m
    return h

n = list(map(int, input().split()))
dist = dict()
lol = []

for i in range(n[0]):
    g = input().split()
    dist[i] = g[0]
    lol.append([0]*2)
    lol[i][0] = int(g[1])
    lol[i][1] = 1

m = int(input())

c = 0
count = n[0]
xyu = n[1]

while m > 0:
    if lol[c][1] == 0:
        if count > 1:
            c = circle(c, n[0])
        else:
            break
    else:
        if lol[c][0] == 0:
            if xyu == 0:
                xyu = 1
                lol[c][0] = 1
            else:
                xyu = 0
        elif lol[c][0] == 1:
            if xyu == 0:
                lol[c][1] = 0
                count -= 1
        c = circle(c, n[0])
        m -= 1

for i in range(n[0]):
    if lol[i][1] == 1:
        print(dist[i], lol[i][0])
