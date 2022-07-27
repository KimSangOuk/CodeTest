# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

# 입력
# N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

# 출력
# 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

# 난이도 : Silver4
# 풀이시간 : 적정

import sys

n = sys.stdin.readline()
length=len(n)-1
array=list()
for i in range(length):
  array.append(int(n[i]))

# 30의 배수가 되기 위해서는 0이 한자리 필요
if not 0 in array:
  print(-1)
else:
  # 큰수를 구하기 위해 역순 배열을 하고
  array.sort(reverse=True)
  # 합이 3이 되지 않을경우 3의 배수가 되지 않기 때문에
  if sum(array[0:length-1])%3!=0:
    print(-1)
  else:
    for i in array:
      print(i,end='')