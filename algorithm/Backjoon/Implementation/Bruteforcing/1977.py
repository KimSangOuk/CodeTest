n=int(input())
m=int(input())

i=1
data=list()
while True:
  if i*i>=n and i*i<=m:
    data.append(i*i)
  elif i*i>m:
    break
  i+=1

if len(data)>0:
  print(sum(data))
  print(data[0])
else:
  print(-1)