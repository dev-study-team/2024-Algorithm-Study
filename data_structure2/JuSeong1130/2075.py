우선순위 큐를 이용하면 되는 문제였다.
우선순위큐를 이용해 값을 넣고

방식 1
한줄씩 읽어나가면서 우선순위큐에 N개의 큰값만 남기면 되는 문제다.

import heapq

N = int(input())

heap = []
for i in range(N):
    nums = list(map(int, input().split()))
    if i == 0:
        for num in nums:
            heapq.heappush(heap, num)
    else :
        for num in nums:
            if heap[0] < num :
                 heapq.heappop(heap)
                 heapq.heappush(heap, num)

print(heap[0])

방식2 그냥 넣고 뒤에서 부터 순서를 세서 구하면되는 문제다.

import sys, heapq


N = int(sys.stdin.readline().rstrip())

heap = []
for i in range(N) :
    nums = list(map(int,sys.stdin.readline().split()))
    for num in nums :
        heapq.heappush(heap, -num)
print(abs(heap[N-1]))

