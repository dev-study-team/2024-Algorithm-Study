heapq 즉 우선순위 큘르 이용하면 되는 문제였다

import heapq, sys

N = int(sys.stdin.readline().rstrip())

heap = []

for i in range(N) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
         if not heap :
              print(0)
         else :
              print(abs(heapq.heappop(heap)))
    else :
         heapq.heappush(heap, -x)

