# import sys

# # r - 세로, c - 가로
# r,c=map(int,sys.stdin.readline().split())

# # board - 보드판
# board=list()
# for i in range(r):
#   tmp=sys.stdin.readline()
#   board.append(list())
#   for j in range(c):
#     board[i].append(tmp[j])

# # for i in range(r):
# #   print(board[i])

# dx=[0,0,-1,1]
# dy=[-1,1,0,0]

# # 지나간 흔적을 담는 리스트
# trace=list()
# def dfs(x,y,graph,length):
#   global result
#   result=max(length,result)
#   trace.append(graph[x][y])
#   for i in range(4):
#     cx=x+dx[i]
#     cy=y+dy[i]
#     if cx<0 or cy<0 or cx>=r or cy>=c:
#       continue
#     if graph[cx][cy]==graph[x][y]:
#       continue
#     if graph[cx][cy] in trace:
#       continue
#     dfs(cx,cy,graph,length+1)
#     trace.pop()
  

# # 최댓값 결과를 결과값으로 return
# result=0
# dfs(0,0,board,1)
# print(result)

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
# 	graph.append(list(sys.stdin.readline().rstrip()))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs():
# 	result = 1
# 	q = set([(0, 0, graph[0][0])])
# 	while q:
# 		# print(q)
# 		x, y, visit = q.pop()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if nx < 0 or ny < 0 or nx >= n or ny >= m:
# 				continue
# 			if graph[nx][ny] == graph[x][y]:
# 				continue
# 			if graph[nx][ny] not in visit:
# 				q.add((nx, ny, visit + graph[nx][ny]))
# 				result = max(result, len(visit + graph[nx][ny]))
# 	return result


# print(bfs())