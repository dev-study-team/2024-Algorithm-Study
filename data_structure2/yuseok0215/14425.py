"""
딕셔너리의 해시 테이블을 이용한 키 기반 탐색! But 메모리를 더 사용함
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

dict = {}
for _ in range(n):
    word = input()
    dict[word] = True

cnt  = 0
for _ in range(m):
    word = input()
    if word in dict:
        cnt += 1

print(cnt)

