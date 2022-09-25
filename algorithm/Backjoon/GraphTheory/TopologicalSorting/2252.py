# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

# 학생들의 번호는 1번부터 N번이다.

# 출력
# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

# 난이도 : Gold3
# 풀이시간 : 적정

from collections import deque
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for _ in range(v+1)]

for _ in range(e):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  q=deque()
  result=[]

  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    result.append(now)

    for i in graph[now]:
      # result[i]=result[now]+1
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)

  for i in range(0,v):
    print(result[i],end=" ")

topology_sort()