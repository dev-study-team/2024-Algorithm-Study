Map 두개를 이용해 구현하면 되는 문제다.


import sys

N, K = map(int,sys.stdin.readline().split())

num_dict = dict()
name_dict = dict()

for i in range(1,N+1) :
   input_str = sys.stdin.readline().rstrip()
   name_dict[input_str] = str(i)
   num_dict[str(i)] = input_str

for i in range(K) :
   findValue = sys.stdin.readline().rstrip()
   if findValue.isdigit() :
      print(num_dict[findValue])
   else :
      print(name_dict[findValue])
