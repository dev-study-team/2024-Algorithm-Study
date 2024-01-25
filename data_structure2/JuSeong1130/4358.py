사전에 넣고 그대로 출력하면 되는문제였다.

import sys

d = dict()
total = 0
while True :
   word = sys.stdin.readline().rstrip()
   if word == '' :
      break
   total += 1
   if word in d :
      d[word] = d[word] + 1
   else :
      d[word] = 1
      

sdic = dict(sorted(d.items()))

for word in sdic :
   num = sdic[word]
   per = (num / total * 100)
   print("%s %.4f" %(word, per))

      
"""
float에 대한 round() 의 동작은 예상과 다를 수 있습니다: 예 들어, round(2.675, 2) 는 2.68 대신에 2.67 을 제공합니다. 이것은 버그가 아닙니다: 대부분의 십진 소수가 float로 정확히 표현될 수 없다는 사실로부터 오는 결과입니다. 

"""



