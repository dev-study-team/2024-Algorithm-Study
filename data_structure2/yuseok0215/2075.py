"""

"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    # tmp = 

    for elem in list(map(int, input().split())):
        heapq.heappush(heap, -elem)


for i in range(n):
    if i == n-1:
        print(-heapq.heappop(heap))
        break
    heapq.heappop(heap)
    
 