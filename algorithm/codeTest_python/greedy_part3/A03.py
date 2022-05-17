s=list(input())
count=0
result=0

for i in range(0,len(s)-1):
  if s[i]!=s[i+1]:
    count+=1

if count%2==0:
  result=count/2
else:
  result=(count+1)/2

print(int(result))