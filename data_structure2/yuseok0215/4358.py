"""
딕셔너리로 빈도 수를 구하는 문제
튜플로도 가능할듯..!?

"""

import sys

input = sys.stdin.readline

dict = {}

cnt = 0

while True:
    s = input().rstrip()
    if not s:
        break
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1
    cnt += 1

for elem in sorted(dict.keys()):
    r = round(dict[elem]/cnt*100, 4)
    print('%s %.4f' % (elem,r))