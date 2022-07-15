# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# 예를 들어, 그림이 아래와 같은 경우에

# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

# 둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

# 난이도 : Gold5
# 풀이시간 : 적절

import sys
from collections import deque

# 그림의 크기, n
n=int(sys.stdin.readline())

# 그림과 색약자의 인식 그림 구별
picture=list()
false_picture=list()
for i in range(n):
  tmp=sys.stdin.readline()
  picture.append(list())
  false_picture.append(list())
  for j in range(n):
    # 그냥 그림
    picture[i].append(tmp[j])
    # 색약자 그림
    if tmp[j]!='B':
      false_picture[i].append('O')
    else:
      false_picture[i].append(tmp[j])

# for i in range(n):
#   print(false_picture[i])

dx=[0,0,1,-1]
dy=[1,-1,0,0]
# 색깔에 따른 탐색
def bfs(c,picture,i,j):
  q=deque()
  q.append((i,j))
  picture[i][j]='0'
  while q:
    v=q.popleft()
    x,y=v
    for i in range(4):
      cx=x+dx[i]
      cy=y+dy[i]
      if cx<0 or cy<0 or cx>=n or cy>=n:
        continue
      # 색깔에 따른 분류
      if picture[cx][cy]!=c:
        continue
      q.append((cx,cy))
      picture[cx][cy]='0'
  

color=['R','G','B','O']
count=0
false_count=0
for i in range(n):
  for j in range(n):
    # 그냥 그림의 탐색
    if picture[i][j] in color:
      count+=1
      bfs(picture[i][j],picture,i,j)
    # 색약자 그림 탐색
    if false_picture[i][j] in color:
      false_count+=1
      bfs(false_picture[i][j],false_picture,i,j)

# 결과 출력
print(count)
print(false_count)