"""
경우의 수는 n! + 1 이다

괄호의 쌍을 제거하는 경우의 수 n! + 1 만큼 출력하자
"""

import sys

input = sys.stdin.readline

arr = input()

cnt = 0
for elem in arr: # 괄호의 개수 구하기
    if elem == '(':
        cnt += 1

case  = []
for i in range(cnt):
    for i
