"""

"""

import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if x == 0:
        max_result = -heapq.heappop(heap)
        print(max_result)
        continue

    heapq.heappush(heap, -x)



  
