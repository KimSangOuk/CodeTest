# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

# 출력
# 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

# 난이도 : Gold4
# 풀이시간 : 적정

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]


for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))


def dijkstra(start):
  q=[]
  distance = [INF] * (n + 1)
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

mid1,mid2=map(int,input().split())
array1=[1,mid1,mid2,n]
array2=[1,mid2,mid1,n]

sum=0
sum1=0
for i in range(0,len(array1)-1):
  sum+=dijkstra(array1[i])[array1[i+1]]
  # print(sum)
  # print(dijkstra(array1[i])[array1[i+1]])
  

for j in range(0,len(array2)-1):
  sum1+=dijkstra(array2[j])[array2[j+1]]
  # print(sum1)
  # print(dijkstra(array2[j])[array2[j+1]])

answer=min(sum,sum1)
if answer<INF:
  print(answer)
else:
  print(-1)