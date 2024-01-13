https://www.acmicpc.net/problem/1935


"""
생각
복잡하게 생각할 필요 없이 하나하나 처리해주면 되는 문제였다.

어려웠던점
후위 표기식 특성상 연산자가 등장하면 앞의 피연산자들을 뒤부터 계산하는 방식이다
이걸 몰라서 못풀었다.


"""
import re

def calculation(num1, num2, operator) :
    if operator == "+" :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == "*" :
        return num1 * num2
    elif operator == "/" :
        return num1 / num2


N = int(input())
result = 0
arr = []
num = []
word = input()

for i in range(N) :
    num.append(int(input()))

for i in word :
    if 'A' <= i <= 'Z' :
        arr.append(num[ord(i) - 65])
    else :
        num2 = arr.pop()
        num1 = arr.pop()
        arr.append(calculation(num1, num2, i))

print("{:.2f}".format(arr.pop()))
