# 문제
#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

# 난이도 : gold 5
# 풀이시간 초과

from collections import deque

n=int(input()) # 보드의 크기 N
k=int(input()) # 사과의 위치의 갯수 k

# 사과의 위치의 갯수 k 개 입력 -> apple
apples=list()
for i in range(k):
  apples.append(tuple(map(int,input().split())))

# 뱀의 방향전환 시점과 방향 입력 -> direction
l=int(input())
direction=list()
for i in range(l):
  a,b=input().split()  
  direction.append((int(a),str(b)))

second=0 # 뱀의 이동 시간
x,y = 0,0 # 뱀의 머리 처음 위치
board = [[0]*n for _ in range(n)] # 보드판
# 사과 위치시키기
for apple in apples:
  board[apple[0]-1][apple[1]-1]=3
# 뱀 위치시키기
snake_dir=0
# 뱀 몸통 이동 리스트
snake_body_move=deque()
snake_body=deque()

# 뱀 방향
dir=[(0,1),(1,0),(0,-1),(-1,0)]

# 뱀 방향 함수
def change_direction(num,right_left):
  if right_left=='D':
    if num<3:
      num+=1
    else:
      num=0
  else:
    if num>0:
      num-=1
    else:
      num=3
  return num

# 뱀 이동
while True:
  # 머리 이동
  dx=dir[snake_dir][0]
  dy=dir[snake_dir][1]
  nx=x+dx
  ny=y+dy
  # print(nx,ny)
  if nx>=0 and ny>=0 and nx<n and ny<n and [nx,ny] not in snake_body: # 이동할 위치가 보드판 내 or 이동할 위치가 뱀의 몸이 아닐때
    deque_body_plus=deque()
    # deque_body_plus.appendleft((0,0)) # 처음에는 이동을 안해도 됨(그자리 그대로)
    if board[nx][ny]==3: # 이동할 위치에 사과가 있다면
      # 사과가 없어지고
      board[nx][ny]=0      
      # 원래 머리가 있던 자리는 몸길이가 늘어나 몸통으로
      snake_body.appendleft([x,y])
      # 추가된 몸체의 앞으로의 이동방향
      snake_body_move.appendleft(deque_body_plus)
    # 몸통이 있다면 이동
    elif len(snake_body)!=0:
      for i in range(len(snake_body)):
        last=snake_body_move[i].popleft()
        snake_body[i][0]+=last[0]
        snake_body[i][1]+=last[1]

    # 머리는 이동할 위치로
    x,y=nx,ny
        
    # 몸통도 후에 이동할 위치 기록
    for i in range(len(snake_body_move)):
      snake_body_move[i].append((dx,dy))

    #확인 코드(차후 삭제)
    # print(snake_body)
    # print(snake_body_move)
    #시간 증가
    second+=1

    #시간이 지난 후 방향 전환
    for i in range(len(direction)):
      if direction[i][0]==second:
        snake_dir=change_direction(snake_dir,direction[i][1])
  else: # 이동할 위치가 보드판 밖이라면
    break
      
    

print(second+1)