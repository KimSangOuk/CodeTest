n=5
# build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

# 기둥과 보의 상태
answer = [[]]
# 기둥과 보를 쌓을 전체 도면
data=[[0]*n for _ in range(n)]
    
build_list=list()

def test_data(build_list):
    ok=False
    complete=0
    for i in range(len(build_list)):
      if build_list[i][4]==0:
        if build_list[i][1]==0:
            complete+=1
        else:
          for j in range(len(build_list)):
            if build_list[j][4]==1 and ((build_list[i][0]==build_list[j][0] and build_list[i][1]==build_list[j][1]) or (build_list[i][0]==build_list[j][2] and build_list[i][1]==build_list[j][3])):
              complete+=1
            elif build_list[j][4]==0 and (build_list[i][0]==build_list[j][2] and build_list[i][1]==build_list[j][3]):
              complete+=1
      else:
        for j in range(len(build_list)):
          if build_list[j][4]==0 and ((build_list[i][0]==build_list[j][2] and build_list[i][1]==build_list[j][3]) or (build_list[i][2]==build_list[j][2] and build_list[i][3]==build_list[j][3])):
            complete+=1
          elif build_list[j][4]==1 and ((build_list[i][0]==build_list[j][2] and build_list[i][1]==build_list[j][3]) and (build_list[i][2]==build_list[j][0] and build_list[i][3]==build_list[j][1])):
            complete+=1

    if complete==len(build_list):
      ok=True
    return ok

for order in build_frame:
  # 명령의 x,y 좌표
  x=order[0]
  y=order[1]
  # 명령의 x,y 이어지는 좌표
  next_x=0
  next_y=0
  # 명령의 타입 : 0-기둥, 1-보
  build_type=order[2]
  # 명령의 설치 or 제거 : 0-제거, 1-삭제
  install=order[3]
  # 타입별 이어지는 좌표
  if build_type==0:
    next_x=x
    next_y=y+1
  else:
    next_x=x+1
    next_y=y
  order_build=[x,y,next_x,next_y,build_type]
  print(order_build)

  # 설치나 제거
  if install==1:
    build_list.append(order_build)
  else:
    if order_build in build_list:
      build_list.remove(order_build)
                
  isok=test_data(build_list)
  print(build_list)
  print(isok)
  if isok==False:
    if install==1:
      build_list.remove(order_build)
    else:
      build_list.append(order_build)

