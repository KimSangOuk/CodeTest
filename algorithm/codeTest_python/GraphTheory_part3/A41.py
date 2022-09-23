import sys
input=sys.stdin.readline

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n=int(input())
m=int(input())
parent=[0]*(n+1)

for i in range(n+1):
  parent[i]=i

for i in range(1,n+1):
  tmp=list(map(int,input().split()))
  for j in range(i,n+1):
    if tmp[j-1]==1:
      union_parent(parent,i,j)

result=True
check_list=list(map(int,input().split()))
for i in range(len(check_list)-1):
  if find_parent(parent,check_list[i])!=find_parent(parent,check_list[i+1]):
    result=False

if result==True:
  print('YES')
else:
  print('NO')