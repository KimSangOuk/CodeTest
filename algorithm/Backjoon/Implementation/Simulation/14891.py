# 문제
# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.



# 이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.





# 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 예를 들어, 아래와 같은 경우를 살펴보자.



# 두 톱니바퀴의 맞닿은 부분은 초록색 점선으로 묶여있는 부분이다. 여기서, 3번 톱니바퀴를 반시계 방향으로 회전했다면, 4번 톱니바퀴는 시계 방향으로 회전하게 된다. 2번 톱니바퀴는 맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되고, 1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다. 따라서, 아래 그림과 같은 모양을 만들게 된다.



# 위와 같은 상태에서 1번 톱니바퀴를 시계 방향으로 회전시키면, 2번 톱니바퀴가 반시계 방향으로 회전하게 되고, 2번이 회전하기 때문에, 3번도 동시에 시계 방향으로 회전하게 된다. 4번은 3번이 회전하지만, 맞닿은 극이 같기 때문에 회전하지 않는다. 따라서, 아래와 같은 상태가 된다.



# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

# 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

# 난이도 : Gold5

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
    gear_state.rotate(1)
  else:
    gear_state.rotate(-1)

  return gear_state

# print(gears_state[0])
# print(gear_turn(gears_state[0],1))
check_order=[[(0,1),(1,2),(2,3)],[(0,1),(1,2),(2,3)],[(2,3),(1,2),(0,1)],[(2,3),(1,2),(0,1)]]
for info_turn in info_turns:
  # 회전 당 해당 톱니바퀴와 회전 방향
  info=info_turn[0]-1
  rotate_dir=info_turn[1]

  effect_teeth=list()
  effect_teeth.append(gears_state[0][2])
  effect_teeth.append(gears_state[1][6])
  effect_teeth.append(gears_state[1][2])
  effect_teeth.append(gears_state[2][6])
  effect_teeth.append(gears_state[2][2])
  effect_teeth.append(gears_state[3][6])
  turn_state=[False,False,False]
  # 맞물린 지점 확인
  for i in range(0,6,2):
    if effect_teeth[i]==effect_teeth[i+1]:
      turn_state[i//2]=False
    else:
      turn_state[i//2]=True

  turn_ok=[[0,0],[0,0],[0,0],[0,0]]
  turn_ok[info][0]=1
  turn_ok[info][1]=rotate_dir

  for i in range(3):
    if turn_state[check_order[info][i][0]]==True and (turn_ok[check_order[info][i][0]][0]==1 or turn_ok[check_order[info][i][1]][0]==1):
      turn_ok[check_order[info][i][0]][0]=1
      turn_ok[check_order[info][i][1]][0]=1
      if turn_ok[check_order[info][i][0]][1]!=0:
        turn_ok[check_order[info][i][1]][1]=-turn_ok[check_order[info][i][0]][1]
      elif turn_ok[check_order[info][i][1]][1]!=0:
        turn_ok[check_order[info][i][0]][1]=-turn_ok[check_order[info][i][1]][1]
  # print(turn_ok)

  for i in range(4):
    if turn_ok[i][0]==1:
      # print(i, turn_ok[i][1])
      gear_turn(gears_state[i],turn_ok[i][1])
  
# 최종 점수 계산
s_score=[1,2,4,8]
n_score=[0,0,0,0]
total_score=0
for i in range(4):
  # print(gears_state[i])
  if gears_state[i][0]==0:
    total_score+=n_score[i]
  else:
    total_score+=s_score[i]

print(total_score)