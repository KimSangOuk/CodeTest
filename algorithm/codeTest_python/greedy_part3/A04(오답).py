n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)

i=0
while True:
  i+=1
  if i in data:
    continue
  j=i
  for k in data:
    if j>=k:
      j-=k
  if j!=0:
    result=i
    break

print(result)

#최솟값을 구하기 위해서는 while이 들어가서 하나씩 찾아야한다고 생각했음
#그렇다보니 아이디어를 생각해내지 못함