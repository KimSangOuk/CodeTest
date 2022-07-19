import sys

# 수의 개수
n = int(sys.stdin.readline())

array=list()
for i in range(n):
  array.append(int(sys.stdin.readline()))

array.sort(reverse=True)
for i in range(n):
  print(array[i],end=' ')