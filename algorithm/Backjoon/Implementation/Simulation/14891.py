from collections import deque

gears_state=list()
for i in range(4):
  tmp=input()
  tmp_deque=deque()
  for j in range(len(tmp)):
    tmp_deque.append(int(tmp[j]))
  gears_state.append(tmp_deque)

k=int(input())
info_turns=list()
for _ in range(k):
  info_turns.append(tuple(map(int,input().split())))

# 제일 처음이 12시 방향이라 했을 때 회전 관련 함수
# -1 : 반시계 / 1 : 시계
def gear_turn(gear_state,rotate_dir):
  if rotate_dir==1:
    gear_state.rotate(-1)
  else:
    gear_state.rotate(1)

  return gear_state

check_order=[[(0,1),(1,2),(2,3)],[(0,1),(1,2),(2,3)],[(2,3),(1,2),(0,1)],[(2,3),(1,2),(0,1)]]
for info_turn in info_turns:
  # 회전 당 해당 톱니바퀴와 회전 방향
  info=info_turn[0]
  rotate_dir=info_turn[1]

  # effect_teeth=list()
  # effect_teeth.append(gears_state[0][2])
  # effect_teeth.append(gears_state[1][6])
  # effect_teeth.append(gears_state[1][2])
  # effect_teeth.append(gears_state[2][6])
  # effect_teeth.append(gears_state[2][2])
  # effect_teeth.append(gears_state[3][6])
  # turn_state=[False,False,False]
  # # 맞물린 지점 확인
  # for i in range(0,6,2):
  #   if effect_teeth[i]==effect_teeth[i+1]:
  #     turn_state[i//2]=False
  #   else:
  #     turn_state[i//2]=True
  # turn_ok=[[0,0],[0,0],[0,0],[0,0]]
  # turn_ok[info][0]=1
  # for i in range(3):
  #   if turn_state[check_order[info][i][0]]==True and (turn_ok[check_order[info][i][0]][0]==1 or turn_ok[check_order[info][i][1]][0]==1):
  #     turn_ok[check_order[info][i][0]][0]=1
  #     turn_ok[check_order[info][i][1]][0]=1
  #     if turn_ok[check_order[info][i][0]][1]!=0:
  #       turn_ok[check_order[info][i][1]][0]=-turn_ok[check_order[info][i][0]][1]
  #     elif turn_ok[check_order[info][i][1]][1]!=0:
  #       turn_ok[check_order[info][i][0]][0]=-turn_ok[check_order[info][i][1]][1]

  # for i in range(4):
  #   if turn_ok[i][0]==1:
  #     print(i, turn_ok[i][1])
  #     gear_turn(gears_state[i],turn_ok[i][1])
  
# 최종 점수 계산
s_score=[1,2,4,8]
n_score=[0,0,0,0]
total_score=0
for i in range(4):
  if gears_state[i][0]==0:
    total_score+=n_score[i]
  else:
    total_score+=s_score[i]