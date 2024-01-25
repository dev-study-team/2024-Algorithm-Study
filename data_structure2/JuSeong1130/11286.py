

"""
만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 


"""
import heapq,sys

N = int(sys.stdin.readline())

heap = []

for i in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else : 
        heapq.heappush(heap, (abs(x), x)) # 절대값과 원래 값을 넣어야 하는 문제였다.

