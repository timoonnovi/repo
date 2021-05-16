def dfs(i):
    if 2*i+1 < len(mass):
        if mass[2*i+1] > mass[i]:
            print('NO')
            exit()
        dfs(2*i+1)
    if 2*i+2 < len(mass):
        if mass[2*i+2] > mass[i]:
            print('NO')
            exit()
        dfs(2*i+2)
#################################


n = int(input())

mass = list(map(int, input().split()))

dfs(0)

print('YES')
