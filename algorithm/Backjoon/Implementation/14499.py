n,m,x,y,k=map(int,input().split())
data_map=list()
for _ in range(n):
  data_map.append(list(map(int,input().split())))

orders=list(map(int,input().split()))

def dice_turn(top,bottom,left,right,front,back,dir_go):
  # 동쪽
  if dir_go==1:
    tmp=right
    right=top
    top=left
    left=bottom
    bottom=tmp
  elif dir_go==2:
    tmp=left
    left=top
    top=right
    right=bottom
    bottom=tmp
  elif dir_go==3:
    tmp=top
    top=back
    back=bottom
    bottom=front
    front=tmp
  elif dir_go==4:
    tmp=top
    top=front
    front=bottom
    bottom=back
    back=tmp

  return top,bottom,left,right,front,back

x,y=y,x
ddir=[(1,0),(-1,0),(0,-1),(0,1)]
top,bottom,left,right,front,back=0,0,0,0,0,0
for order in orders:
  dx=x+ddir[order-1][0]
  dy=y+ddir[order-1][1]
  # 이동할 곳의 자표가 맵을 벗어나면 명령 무시함
  if dx<0 or dx>=m or dy<0 or dy>=n:
    continue

  # 주사위 위치 이동
  x=dx
  y=dy
  # 주사위 굴리기
  top,bottom,left,right,front,back=dice_turn(top,bottom,left,right,front,back,order)

  # 만약 주사위가 이동한 칸 숫자가 0이라면
  if data_map[dy][dx]==0:
    data_map[dy][dx]=bottom
  # 0이 아니라면
  else:
    bottom=data_map[dy][dx]
    data_map[dy][dx]=0

  print(top)