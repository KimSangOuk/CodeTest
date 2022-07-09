from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split()) # 정점, 간선

# 정점의 개수 만큼 그래프 늘리기
graph=list()
for i in range(n+1):
  graph.append(list())

# 간선을 그래프에 반영
for i in range(m):
  u,v=map(int,sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(n+1):
  graph[i].sort()

visited=[False]*(n+1)

def dfs(graph,v,visited):
  q=deque()
  visited[v]=True
  q.append(v)
  while q:
    v=q.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i]=True
        q.append(i)

# 정점 중 탐색이 안된 정점이 있다면
count=0
for i in range(1,n+1):
  if not visited[i]:
    dfs(graph,i,visited)
    count+=1

print(count)