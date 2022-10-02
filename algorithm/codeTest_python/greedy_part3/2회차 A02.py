import sys
input=sys.stdin.readline

s=input()
result=0
for i in s[0:len(s)-1]:
  if i=='0' or i=='1' or result<=1:
    result+=int(i)
  else:
    result*=int(i)

print(result)