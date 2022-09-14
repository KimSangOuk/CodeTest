import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

x=[0,0,-1,1]
y=[-1,1,0,0]

def dijkstra(distance,graph,start,n):
  q=[]
  heapq.heappush(q,(graph[start[0]][start[1]],start))
  distance[start[0]][start[1]]=0
  while q:
    dist,now=heapq.heappop(q)
    if dist<distance[now[0]][now[1]]:
      continue

    for i in range(4):
      if now[0]+x[i]>=0 and now[0]+x[i]<n and now[1]+y[i]>=0 and now[1]+y[i]<n:
        cost=dist+graph[now[0]+x[i]][now[1]+y[i]]
        if cost<distance[now[0]+x[i]][now[1]+y[i]]:
          distance[now[0]+x[i]][now[1]+y[i]]=cost
          heapq.heappush(q,(cost,(now[0]+x[i],now[1]+y[i])))

  # for i in range(n):
    # print(distance[i])

t=int(input())

for i in range(t):
  n=int(input())
  graph=[[]*n for _ in range(n)]
  start=(0,0)
  
  distance=[[INF]*n for _ in range(n)]

  for a in range(n):
    tmp=list(map(int,input().split()))
    for b in range(n):
      graph[a].append(tmp[b])

  dijkstra(distance,graph,start,n)
  print(distance[n-1][n-1])