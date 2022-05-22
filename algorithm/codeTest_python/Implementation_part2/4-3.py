# 현재 나이트의 위치 입력받기
chess=input()
x=ord(chess[0])-96
y=int(chess[1])

# 나이트가 이동할 수 있는 8가지 방향 정의
cases=[(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1),(2,1),(1,2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count=0
for case in cases:
  dx=case[0]
  dy=case[1]
  nx=x+dx
  ny=y+dy
  if nx>=1 and nx<=8 and ny>=1 and ny<=8:
    count+=1

print(count)