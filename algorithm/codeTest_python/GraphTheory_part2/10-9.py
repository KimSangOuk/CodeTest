import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]

for k in range(1,n+1):
  input_list=list(map(int,input().split()))
  cost=input_list[0]
  if k==1:
    graph[0].append((1,cost))
  for i in range(1,len(input_list)-1):
    graph[input_list[i]].append((k,cost))
    indegree[k]+=1

# print(indegree)

def topology_sort():
  result=[0]*(n+1)
  q=deque()

  for i in range(0,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i[0]]-=1
      result[i[0]]=result[now]+i[1]
      if indegree[i[0]]==0:
        q.append(i[0])
  print(result)

topology_sort()
      
    
    