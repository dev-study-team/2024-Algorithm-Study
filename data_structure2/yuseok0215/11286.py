"""
heapq에 튜플 형태로 push해서 답을 구해야 했던 묹네

"""


import sys
import heapq

abs_heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(abs_heap, (abs(num), num))
	else:
		if abs_heap:
			print(heapq.heappop(abs_heap)[1])
		else:
			print(0)

# heap = []
# for _ in range(n):
#     x = int(input())

#     flag = 0
#     if x < 0:
#         flag = 1
#         heapq.heappush(heap, (-x, flag))   
#     elif x > 0:
#         heapq.heappush(heap, (x, flag))    

#     elif x == 0:
#         if len(heap) >= 1:
#             k,f = heapq.heappop(heap)

#             if f == 1:
#                 k = -k
#             print(k)
#         else:
#             print(0)

    
    
