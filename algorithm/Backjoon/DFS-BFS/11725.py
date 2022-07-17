# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 난이도 : Silver2
# 풀이시간 : 부적절

import sys
from collections import deque

# 노드의 개수
n=int(sys.stdin.readline())
# 그래프
graph=list()
for i in range(n+1):
  graph.append(list())
# 쌍방향 연결이기 때문에 그래프 생성
for i in range(1,n):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# 탐색함수
def bfs(start):
  q=deque()
  # 탐색이 되었는지 체크
  check=[False]*(n+1)
  parent=[0]*(n+1)
  q.append(start)
  check[start]=True
  # q가 빌때까지 반복
  while q:
    v=q.popleft()
    for i in graph[v]:
      # 다음 탐색이 가능할 때
      if not check[i]:
        q.append(i)
        check[i]=True
        # 부모를 찾는대로 등록
        parent[i]=v
  # 정답 출력
  for i in range(2,n+1):
    print(parent[i])
  
bfs(1)
