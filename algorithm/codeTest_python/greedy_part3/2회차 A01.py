import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
data.sort()

result=0
x=0
num=0
for i in data:
  x=i
  num+=1
  if x==num:
    result+=1
    num=0

print(result)