from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
min_h, max_h = [], []
d = {}
for _ in range(n):
    p, l = map(int, input().split())
    heappush(min_h, [l, p])
    heappush(max_h, [-l, -p])
    d[p] = True

M = int(input())
for _ in range(M):

    command = input().split()

    if command[0] == 'recommend':
        if command[1] == '1':
            while not d[-max_h[0][1]]:
                heappop(max_h)
            print(-max_h[0][1])
        else:
            while not d[min_h[0][1]]:
                heappop(min_h)
            print(min_h[0][1])

    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        while not d[-max_h[0][1]]:
            heappop(max_h)
        while not d[min_h[0][1]]:
            heappop(min_h)
        d[p] = True
        heappush(max_h, [-l, -p])
        heappush(min_h, [l, p])
    else:
        d[int(command[1])] = False