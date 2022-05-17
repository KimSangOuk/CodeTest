s=list(input())
result=0

for t in s:
  if int(t)==0:
    continue
  elif int(t)==1 or result==0 or result==1:
    result+=int(t)
  else:
    result*=int(t)

print(result)