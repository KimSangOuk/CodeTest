# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 난이도 : Silver4
# 풀이시간 : 적정

import sys

# 듣지도 못한 사람 n, 보지도 못한 사람 m
n,m=map(int,sys.stdin.readline().split())

# 듣지도 못한 사람 리스트 array1
array1=set()
for i in range(n):
  array1.add(sys.stdin.readline())

# 듣지도 못한 사람 리스트 array2
array2=set()
for i in range(m):
  array2.add(sys.stdin.readline())

# 중복되는 이름을 리스트화 하여 정렬
answer=sorted(list(array1&array2))

# 정답 출력
print(len(answer))
for i in answer:
  print(i,end='')