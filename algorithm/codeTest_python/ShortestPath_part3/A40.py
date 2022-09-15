import sys
import heapq
input=sys.stdin.readline
INF=(1e9)

n,m=map(int,input().split())
graph=[[]*(n+1) for _ in range(n+1)]
distance=[INF]*(n+1)
start=1

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(distance)
min_num=INF
array=list()
for i in distance:
  if i==INF:
    min_num=0
  else:
    min_num=max(i,min_num)

print(min_num)
for i in range(1,n+1):
  if distance[i]==min_num:
    array.append(i)

array.sort()
print(array)
print(array[0],min_num,len(array))