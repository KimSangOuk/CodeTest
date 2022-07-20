import sys

# 입력 갯수
n=int(sys.stdin.readline())

array=list()
for i in range(n):
  data=sys.stdin.readline().split()
  array.append((data[0],int(data[1])))

array.sort(key=lambda x:x[1])

for i in range(n):
  print(array[i][0],end=' ')