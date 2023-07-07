import sys
input=sys.stdin.readline

s=input()
start=s[0]
now=start
result=0  
for i in s[1:len(s)-1]: 
  if now!=i:
    result+=1
    now=i

if start!=now:
  result=result//2+1
else:
  result=result//2

print(result)