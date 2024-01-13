https://www.acmicpc.net/problem/1966


"""
1.Task라는 클래스를 만들고 여기에 중요도와 인덱스를 넣은 리스트를 만들어 놓는다.
2. 중요도에 관한 것을 정렬한 리스트를 만들어 놓고 테스크리스트에서 첫번째꺼를 비교하여 같거나 크다면 print하는 방법으로 실행했다

어려웠던점
파이썬에서 클래스를 쓰는 방법을 몰라 갓피티에 물어봤다.

"""
from queue import PriorityQueue
import copy
class Task:
    def __init__(self, importance, index):
        self.importance = importance
        self.index = index

N = int(input()) # 테스트케이스의 수

for i in range(N) :
    result = 0
    m, k = map(int, input().split()) # 문서의 개수, 궁금한 문서가 몇번쨰 위치한지
    arr = list(map(int, input().split())) # 문서의 중요도가 차례대로
    tasks = [Task(importance, index) for index, importance in enumerate(arr)]

    sortArr = copy.deepcopy(arr)
    sortArr.sort()
    while len(tasks) > 0 :
        if tasks[0].importance >= sortArr[-1] :
            result += 1
            if tasks[0].index == k :
                break
            del tasks[0]
            sortArr.pop()
             
        else :
            tasks.append(tasks[0])
            del tasks[0]    
    print(result)



"""
https://develop247.tistory.com/340
두개의 배열을 놨둔다.
1. index에 관한 배열 
2. 우선순위에 관한 배열 이를 가지고 구현하게 된다.
위 방법보다 그냥 합쳐놓은 list를 구현하는게 더좋을듯?

https://velog.io/@greene/%EB%B0%B1%EC%A4%80-1966%EB%B2%88-%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC
Task란 객체를 쓰지않고 list에 표현하였다.


https://hongcoding.tistory.com/42
m이라는 현재위치값을 가지고 0이됬을때 count 값을 비교하도록 구현하였다.
"""



