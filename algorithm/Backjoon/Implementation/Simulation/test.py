# n*n 보드의 크기
n=int(input())

# 게임판의 초기 상태
board=list()
for _ in range(n):
  board.append(list(map(int,input().split())))

case=['left']
# board에서 case대로 이동
def move_2048_board(board,case):
  for dir in case:
    if dir=='left':
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
  return board

print(move_2048_board(board,case))