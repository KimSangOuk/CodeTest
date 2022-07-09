# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 난이도 : Silver2
# 풀이시간 : 적정

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