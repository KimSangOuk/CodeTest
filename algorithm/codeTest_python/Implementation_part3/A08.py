s=input()

num=list()
for i in range(10):
  num.append(str(i))

sum=0
new = list()
for i in range(len(s)):
  if s[i] in num:
    sum+=int(s[i])
  else:
    new.append(s[i])

new.sort()
result=''
for i in new:
  result+=i

if result!=0:
  result+=str(sum)

print(result)