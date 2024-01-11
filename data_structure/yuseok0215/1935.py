n = int(input())
oper = input()

num = []
for _ in range(n):
    num.append(int(input()))

stack = []
num_idx = 0
for elem in oper:
    if elem.isalpha():
        stack.append(num[ord(elem)-ord('A')])
        num_idx += 1
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
