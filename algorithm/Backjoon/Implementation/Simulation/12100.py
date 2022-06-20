from itertools import combinations_with_replacement
import copy

# n*n 보드의 크기
n=int(input())

# 게임판의 초기 상태
board=list()
for _ in range(n):
  board.append(list(map(int,input().split())))

# 방향
direction=['up','down','left','right']
# 방향이 나올 수 있는 경우의 수
cases=list(combinations_with_replacement(direction,5))

# board에서 case대로 이동
def move_2048_board(tmp_board,case):
  board=copy.deepcopy(tmp_board)
  for dir in case:
    if dir=='up':
      for j in range(len(board)):
        # 0을 제외한 리스트
        tmp_line=list()
        for i in range(len(board)):
          # 0이 아닐 경우
          if board[i][j]!=0:
            tmp_line.append(board[i][j])
        k=0
        i=0
        # 다시 재 배치
        while True:
          if k<len(tmp_line)-1:
            if tmp_line[k]==tmp_line[k+1]:
              board[i][j]=2*tmp_line[k]
              k+=2
              i+=1
            elif tmp_line[k]!=tmp_line[k+1]:
              board[i][j]=tmp_line[k]
              i+=1
              k+=1
          elif k==len(tmp_line)-1:
            board[i][j]=tmp_line[k]
            i+=1
            k+=1
          elif i<len(board):
            board[i][j]=0
            i+=1
            k+=1
          elif i>=len(board):
            break
    elif dir=='down':
      for j in range(len(board)):
        # 0을 제외한 리스트
        tmp_line=list()
        for i in range(len(board)-1,-1,-1):
          # 0이 아닐 경우
          if board[i][j]!=0:
            tmp_line.append(board[i][j])
        k=0
        i=len(board)-1
        # 다시 재 배치
        while True:
          if k<len(tmp_line)-1:
            if tmp_line[k]==tmp_line[k+1]:
              board[i][j]=2*tmp_line[k]
              k+=2
              i-=1
            elif tmp_line[k]!=tmp_line[k+1]:
              board[i][j]=tmp_line[k]
              i-=1
              k+=1
          elif k==len(tmp_line)-1:
            board[i][j]=tmp_line[k]
            i-=1
            k+=1
          elif i>=0:
            board[i][j]=0
            i-=1
            k+=1
          elif i<0:
            break
    elif dir=='left':
      for i in range(len(board)):
        # 0을 제외한 리스트
        tmp_line=list()
        for j in range(len(board)):
          # 0이 아닐 경우
          if board[i][j]!=0:
            tmp_line.append(board[i][j])
        k=0
        j=0
        # 다시 재 배치
        while True:
          if k<len(tmp_line)-1:
            if tmp_line[k]==tmp_line[k+1]:
              board[i][j]=2*tmp_line[k]
              k+=2
              j+=1
            elif tmp_line[k]!=tmp_line[k+1]:
              board[i][j]=tmp_line[k]
              j+=1
              k+=1
          elif k==len(tmp_line)-1:
            board[i][j]=tmp_line[k]
            j+=1
            k+=1
          elif j<len(board):
            board[i][j]=0
            j+=1
            k+=1
          elif j>=len(board):
            break
    elif dir=='right':
      for i in range(len(board)):
        # 0을 제외한 리스트
        tmp_line=list()
        for j in range(len(board)-1,-1,-1):
          # 0이 아닐 경우
          if board[i][j]!=0:
            tmp_line.append(board[i][j])
        k=0
        j=len(board)-1
        # 다시 재 배치
        while True:
          if k<len(tmp_line)-1:
            if tmp_line[k]==tmp_line[k+1]:
              board[i][j]=2*tmp_line[k]
              k+=2
              j-=1
            elif tmp_line[k]!=tmp_line[k+1]:
              board[i][j]=tmp_line[k]
              j-=1
              k+=1
          elif k==len(tmp_line)-1:
            board[i][j]=tmp_line[k]
            j-=1
            k+=1
          elif j>=0:
            board[i][j]=0
            j-=1
            k+=1
          elif j<0:
            break
  
  # 이동 마친 보드 값 출력
  return board

# 보드 중의 최댓값
max_value=-1
for case in cases:
  # 실제로 이동
  tmp_board=list()
  tmp_board=move_2048_board(board,case)

  # print(case)
  # for i in range(len(board)):
    # print(tmp_board[i])
  
  # print()
  # case에서의 최댓값 갱신
  for i in range(n):
    max_value=max(max_value,max(tmp_board[i]))

# 답 출력
print(max_value)