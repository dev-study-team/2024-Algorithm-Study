from itertools import combinations

n = int(input())
power = []

person = n//2

for _ in range(n):
    power.append(list(map(int, input().split())))

idx = [i for i in range(n)]

comb = list(combinations(idx, person))
# 0 1 2 3 4 5
# (0 1 4 // 2 3 5) ( // ) ( // ) ( )

team = []

for elem in comb:
    p = 0
    for temp_team in elem:
        for x,y in list(combinations(temp_team,2)):
            p += abs(power[x][y]-power[y][x])
        team    
