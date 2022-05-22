n=int(input())
plan=input().split()

x=1
y=1
for s in plan:
  if s=='L' and y>1:
    y-=1
  elif s=='R' and y<n:
    y+=1
  elif s=='U' and x>1:
    x-=1
  elif s=='D' and x<n:
    x+=1

print(x,y)