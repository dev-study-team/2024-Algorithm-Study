n = int(input())
oper = input()

num = [] 
for _ in range(n):
    num.append(int(input()))

stack = []

for elem in oper:
    if elem.isalpha():
        stack.append(num[ord(elem)-ord('A')])
    elif elem in ['*','/','+','-']:
        a = stack.pop()
        b = stack.pop()

        result = 0
        if elem == '*':
            result = b * a
        elif elem == '/':
            result = b / a
        elif elem == '+':
            result = b + a
        elif elem == '-':
            result = b - a
        
        stack.append(result)

print('%.2f' %stack[0])	
