n=int(input())
answer=0
i=1
while True:
  answer+=i
  if answer>=n:
    break
  i=i+1

print(i)