# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 북쪽에서부터 r번째, 서쪽에서부터 c번째로 위치한 칸은 (r, c)로 나타낼 수 있다.

# 로봇 청소기는 다음과 같이 작동한다.

# 현재 위치를 청소한다.
# 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
# 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면, 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우, 왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
# 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우, 바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
# 입력
# 첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

# 둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

# 셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

# 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

# 출력
# 로봇 청소기가 청소하는 칸의 개수를 출력한다.

# 난이도 : Gold5

n,m = map(int,input().split())
r,c,d = map(int,input().split())
data_map=list()

for i in range(n):
  data_map.append(list(map(int,input().split())))

x=c
y=r
count=0
cur_dir=d
dir_go=[(0,-1),(1,0),(0,1),(-1,0)]
block_count=0
while True:
  if block_count==4:
    block_count=0
    # 만약 뒤가 벽으로 막혀있다면
    if cur_dir==0:
      dx=x+dir_go[2][0]
      dy=y+dir_go[2][1]
    elif cur_dir==1:
      dx=x+dir_go[3][0]
      dy=y+dir_go[3][1]
    elif cur_dir==2:
      dx=x+dir_go[0][0]
      dy=y+dir_go[0][1]
    elif cur_dir==3:
      dx=x+dir_go[1][0]
      dy=y+dir_go[1][1]

    if data_map[dy][dx]==1:
      break
    # 뒤가 벽이 아니라면
    elif data_map[dy][dx]==0 or data_map[dy][dx]==2:
      x=dx
      y=dy
      dx=0
      dy=0
  
  # 현재 위치 청소 - 청소가 안되어있을 경우
  if data_map[y][x]==0:
    data_map[y][x]=2
    # print(x,y,cur_dir)
    count+=1

  # 현재 위치에서 바로 왼쪽 탐색
  if cur_dir==0:
    cur_dir=3
  elif cur_dir==1:
    cur_dir=0
  elif cur_dir==2:
    cur_dir=1
  elif cur_dir==3:
    cur_dir=2

  # 만약 왼쪽이 비었다면
  dx=x+dir_go[cur_dir][0]
  dy=y+dir_go[cur_dir][1]
  if data_map[dy][dx]==0:
    x=dx
    y=dy
    dx=0
    dy=0
    block_count=0
  # 만약 왼쪽이 막혀있다면
  elif data_map[dy][dx]==1 or data_map[dy][dx]==2:
    block_count+=1
    # print(block_count)

print(count)