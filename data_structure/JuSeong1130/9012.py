# https://www.acmicpc.net/problem/9012

"""
내생각
()를 없애다보면 답이 나오지 않을까란 생각에 그렇게 진행했다.

어려웠던점
readline에 개행문자가 들어가 공백이 들어가게 되었고 이를 몰라 헤매게 되었다.
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    findStr = sys.stdin.readline().strip()  # 개행 문자 제거
    while "()" in findStr :
        findStr = findStr.replace("()", "") # 여러개 바꾸는거찾아보기
    if not findStr:  # 빈 문자열인 경우
        print("YES")
    else :
        print("NO")

"""
import re

input_string = "Hello, world! Hello, Python!"

# "Hello"를 "Hi"로 대체
output_string = re.sub(r'Hello', 'Hi', input_string)

print(output_string)
"""





"""
다른 사람 풀이

1. 유석님은 다른 생각으로 구현하셨는데
int 변수를 한개 놨두고 (는 + )는 -로 더하게 된다 그때 -가 되면 바로 멈추게하고 이후 확인했을때 0이라면 yes 아니라면 no를 출력하게 하셨다.

2. https://wookcode.tistory.com/49 stack을 이용해서 (면 append 아니라면 pop을 이용해 구현해도 된다.



"""
