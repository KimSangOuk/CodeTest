from collections import deque

n, m = map(int,input().split())

maze_map=list()
for _ in range(n):
  tmp=""
  tmp=input()
  tmp_list=list()
  for i in range(m):
    tmp_list.append(int(tmp[i]))
  maze_map.append(tmp_list)

# for i in range(n):
#   print(maze_map[i])

def bfs(maze_map):
  # 출발 좌표
  start=(0,0)
  queue=deque()
  queue.append(start)
  maze_map[start[1]][start[0]]=1
  while queue:
    v=queue.popleft()
    # print(v)
    vx=v[0]
    vy=v[1]
    # 오른쪽
    if vx+1>=0 and vx+1<m and vy>=0 and vy<n and maze_map[vy][vx+1]==1:
      queue.append((vx+1,vy))
      maze_map[vy][vx+1]=maze_map[vy][vx]+1
    # 왼쪽
    if vx-1>=0 and vx-1<m and vy>=0 and vy<n and maze_map[vy][vx-1]==1:
      queue.append((vx-1,vy))
      maze_map[vy][vx-1]=maze_map[vy][vx]+1  
    # 위
    if vx>=0 and vx<m and vy-1>=0 and vy-1<n and maze_map[vy-1][vx]==1:
      queue.append((vx,vy-1))
      maze_map[vy-1][vx]=maze_map[vy][vx]+1
    # 아래
    if vx>=0 and vx<m and vy+1>=0 and vy+1<n and maze_map[vy+1][vx]==1:
      queue.append((vx,vy+1))
      maze_map[vy+1][vx]=maze_map[vy][vx]+1

bfs(maze_map)
print(maze_map[n-1][m-1])