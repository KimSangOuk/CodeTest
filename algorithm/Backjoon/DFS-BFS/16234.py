# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

# 오늘부터 인구 이동이 시작되는 날이다.

# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# 출력
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

# 난이도 : Gold5
# 풀이시간 : over

import sys
from collections import deque
import copy

# N - 땅의 크기, l, r - 두 나라 인구 차이 L이상 R이하 일때 국경선 개방
n,l,r = map(int,sys.stdin.readline().split()) 

# a - 나라별 인구 분포
a=list()
for _ in range(n):
  a.append(list(map(int,sys.stdin.readline().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 경신
def bfs(x,y,k):
  # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
  united=[]
  united.append((x,y))
  # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
  q=deque()
  q.append((x,y))
  check[x][y]=k # 현재 연합의 번호 할당
  count=1 # 전체 연합의 국가 수
  summary=a[x][y] # 현재 연합의 전체 인구 수
  # 큐가 빌 때까지 반복(BFS)
  while q:
    x,y=q.popleft()
    # 현재 위치에서 4가지 방향을 확인하며
    for t in range(4):
      cx=x+dx[t]
      cy=y+dy[t]
      # 바로 옆에 있는 나라를 확인하여
      if cx<0 or cy<0 or cx>=n or cy>=n:
        continue
      # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
      if not l<=abs(a[x][y]-a[cx][cy])<=r:
        continue
      if check[cx][cy]==-1:
        # 연합에 추가
        check[cx][cy]=k
        q.append((cx,cy))
        summary+=a[cx][cy]
        count+=1
        united.append((cx,cy))

  # 연합 국가끼리 인구를 분배
  for i,j in united:
    a[i][j]=summary//count
  return count

# bfs(a,check)

day=0
# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
  check = [[-1]*n for _ in range(n)]
  k=0
  for i in range(n):
    for j in range(n):
      if check[i][j]==-1: # 해당 나라가 아직 처리되지 않았다면
        bfs(i,j,k)
        k+=1
  # 모든 인구 이동이 끝난 경우
  if k==n*n:
    break
  day+=1

# 인구 이동 횟수 출력
print(day)