n, m = map(int,input().split())
a, b, d = map(int,input().split())


array=list()

for i in range(n):
  array.append(list(map(int,input().split())))

count=1
na, nb = 0, 0
while True:
  for _ in range(4):
    if d==0:
      d=3
    else:
      d-=1

    da=0
    db=0
    if d==0:
      da=-1
    elif d==1:
      db=1
    elif d==2:
      da=1
    elif d==3:
      db=-1
    na=a+da
    nb=b+db

    if na>=0 and na<=n and nb>=0 and nb<=m and array[na][nb]==0:
      break

  if na==a and nb==b:
    break

  count+=1
  a=na
  b=nb
  array[a][b]=3

print(count)

  
