import sys

t = int(sys.stdin.readline())
for i in range(t):
  n, m = map(int, sys.stdin.readline().split())
  array=list(map(int,sys.stdin.readline().split()))
  mine=[[0]*(m+2) for _ in range(n+2)]
  answer = list()
  for k in range(0,len(array)):
    mine[k//m+1][k%m+1]=array[k]

  d=[[0]*(m+2) for _ in range(n+2)]
  for a in range(1,m+1):
    for b in range(1,n+1):
      d[b][a]=mine[b][a]+max(d[b-1][a-1],d[b][a-1],d[b+1][a-1])

  for j in range(1,n+1):
    answer.append(d[j][m])

  print(max(answer))
      