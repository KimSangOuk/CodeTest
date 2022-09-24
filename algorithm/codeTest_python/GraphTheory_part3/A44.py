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

plant=[]

for i in range(n):
  x,y,z=map(int,input().split())
  plant.append((i+1,x,y,z))

parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

edges=[]

for k in range(1,4):
  plant.sort(key=lambda x:x[k])
  for i in range(n-1):
    edges.append((plant[i+1][k]-plant[i][k],plant[i][0],plant[i+1][0]))
# for i in range(0,n-1):
#   for j in range(i+1,n):
#     value=min(abs(plant[i][0]-plant[j][0]),abs(plant[i][1]-plant[j][1]),abs(plant[i][2]-plant[j][2]))
#     edges.append((value,i+1,j+1))

edges.sort()
# print(edges)
result=0

for edge in edges:
  c,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=c

print(result)