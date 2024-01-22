"""
메모리 초과가 나는 문제였다.

메모리 초과를 피하려면 n번째 큰수를 구하는 동안 배열의 크기를 n으로 가둬놓고
대소비교를 통해 메모리의 길이를 유지해야했다.
pop -> push

"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
    
 