n=int(input())
i=0
result=0
while True:
  result+=i
  if result>=n:
    break
  i+=1
print(result)