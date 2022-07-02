import sys
from collections import deque
import copy

# N - 땅의 크기, l, r - 두 나라 인구 차이 L이상 R이하 일때 국경선 개방
n,l,r = map(int,sys.stdin.readline().split()) 

# a - 나라별 인구 분포
a=list()
for _ in range(n):
  a.append(list(map(int,sys.stdin.readline().split())))

# 연합국을 구분해서 탐색한 부분을 표시할 배열
check=[[0]*n for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(a,check):
  tmp_a=copy.deepcopy(a)
  tmp_check=copy.deepcopy(check)
  k=1
  for i in range(n):
    for j in range(n):
      if tmp_check[i][j]==0:
        q=deque()
        tmp_check[i][j]=k
        q.append((i,j))
        while q:
          vx,vy=q.popleft()
          for t in range(4):
            cx=vx+dx[t]
            cy=vy+dy[t]
            if cx<0 or cy<0 or cx>=n or cy>=n:
              continue
            if not l<=abs(tmp_a[vx][vy]-tmp_a[cx][cy])<=r:
              continue
            if tmp_check[cx][cy]==0:
              tmp_check[cx][cy]=k
              q.append((cx,cy))
        k+=1

  sum=[0]*k
  count=[0]*k
  for i in range(n):
    for j in range(n):
      for t in range(k):
        if tmp_check[i][j]==t:
          sum[t]+=tmp_a[i][j]
          count[t]+=1
  for i in range(n):
    for j in range(n):
      for t in range(k):
        if tmp_check[i][j]==t:
          tmp_a[i][j]=int(sum[t]/count[t])
  return tmp_a

day=0
while True:
  day+=1
  next=True
  tmp_a=bfs(a,check)
  for i in range(n):
    for j in range(n):
      if a[i][j]!=tmp_a[i][j]:
        next=False
  if next==True:
    break

  a=tmp_a

print(day-1)