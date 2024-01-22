"""
단순하게 배열에 넣어서 탐색할 때 index() 메서드의 탐색으로 인한 시간초과가 나게 됐다.

단순 배열보다 딕셔너리를 사용해서 key를 탐색해서 찾는 방식이 훨씬 빠른 방법이었다.

"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])