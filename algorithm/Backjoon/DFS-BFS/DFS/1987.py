import sys

# r - 세로, c - 가로
r,c=map(int,sys.stdin.readline().split())

# board - 보드판
board=list()
for i in range(r):
  tmp=sys.stdin.readline()
  board.append(list())
  for j in range(c):
    board[i].append(tmp[j])

# for i in range(r):
#   print(board[i])

# 지나간 흔적을 담는 리스트
result=0
trace=list()
def dfs(x,y,graph):
  result=0
  if x<0 or y<0 or x>=r or y>=c:
    return 0
  if graph[x][y] in trace:
    result=len(trace)
    return result
  trace.append(graph[x][y])
  result=max(dfs(x+1,y,graph),result)
  result=max(dfs(x,y+1,graph),result)
  result=max(dfs(x-1,y,graph),result)
  result=max(dfs(x,y-1,graph),result)
  # print(result)
  # print(trace)
  # print(trace)
  trace.pop(len(trace)-1)
  return result
  

# 최댓값 결과를 결과값으로 return
result=dfs(0,0,board)
print(result)