
https://www.acmicpc.net/problem/1158

"""
내 생각
원으로 연결된걸 진짜 연결된거 처럼 어떻게 표현해야할까? 생각하다가 최대가 지나면 0으로 초기화되게 구성하면되겠다라는 생각으로 진행하였다.

어려웠던 점
삭제가 되면 인덱스가 원 위치에서 -1이 된것이 현재 인덱스가 되는것이였는데 이는 많이 생각해보지 않은 탓에 런타임이 되어야 알 수 있었다. 
돌아가는 방식에 대해 많이 생각해보고 문제에 들어가는것이 좋을 것 같다.

"""
# 내풀이
n, k = input().split()
n = int(n)
k = int(k)

# 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6

# 1 2 4 5 6 7
# 0 1 2 3 4 5  원래 2의 위치였다면 1에서 + 3의 위치를 찾아야함

idx = k - 1
arr = [] 
result = []
for i in range(n) :
    arr.append(i+1)

while len(arr) > 0 :
    result.append(arr[idx])
    arr.pop(idx)
    idx -= 1 # pop됨으로 인해 index값 - 1 해줘야 됨 
    for i in range(k) :
        idx += 1
        if(idx > len(arr) - 1) :
            idx = 0

# 유석님께서는 나처럼 idx -1 한 이후에 이동이 아니라 그냥 idx -= k -1로 이동 시킨 이후에 idx = idx % len(arr)을 통해 현재 위치를 조정해 주셨다
https://infinitt.tistory.com/213

https://velog.io/@thguss/%EB%B0%B1%EC%A4%80-1158.-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-with.-Python-%ED%81%90-%EB%AC%B8%EC%A0%9C%EC%97%90%EC%84%9C-deque%EB%8A%94-%ED%95%84%EC%88%98-%EB%B3%84%EA%BC%AC%EB%A6%AC-%EB%95%85%EB%95%85
deque를 이용해서 구현도 가능하다
k위치 전까지 값을 앞에서부터 꺼내 뒤로 보내주고 이후 result에 넣어주는 방식으로 진행하면 된다.



#0 1 2 3 4 5 6
#1 2 3 4 5 6 7
#1 2 4 5 6 7 
#1 2 4 5 7
#1 4 5 7 
print(f"<{', '.join(map(str, result))}>")
