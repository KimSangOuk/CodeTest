n=int(input())
data=list(map(int,input().split()))

data.sort()

result=0
i=0
s=0
count=1

while i!=n:
  s=data[i] # for 문의 리스트를 하나씩 불러오도록 for i in data 등으로 간략화 가능
  if s==count:
    result+=1
    count=1
  else:
    count+=1
  i+=1

# 간략화가 되었다면 s,i 등의 변수가 필요없음, count 등의 정리가 눈에 들어옴

print(result)