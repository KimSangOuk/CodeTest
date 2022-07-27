# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.

# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 난이도 : Silver2
# 풀이시간 : 적정

import sys

# 좌표의 개수
n = int(sys.stdin.readline())

array1=list(map(int,sys.stdin.readline().split()))
array=sorted(array1)

num=0
answer=dict()
# 크기 순으로 증가시켜서 딕셔너리에 기록
for i in range(n-1):
  answer[array[i]]=num
  num+=1
  if array[i]==array[i+1]:
    num-=1

# 마지막 수 처리
answer[array[len(array)-1]]=num

# 딕셔너리에서 숫자대로 꺼내서 출력
for i in range(n):
  print(answer[array1[i]])