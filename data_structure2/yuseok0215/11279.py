"""
heapq를 이용한 최대값 구하기 
최소값만 구할 수 있어서 부호를 바꿔서 뽑아내야했다.
"""

import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if len(heap) >= 1:
            max_result = -heapq.heappop(heap)
            print(max_result)
            continue
        else:
            print(0)

    heapq.heappush(heap, -x)



  
