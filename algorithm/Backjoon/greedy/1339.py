import sys
input=sys.stdin.readline

n=int(input())
array=list()
for i in range(n):
  array.append(input().strip())

array.sort(key=len,reverse=True)

answer=''

while True:
  if array[0]=='':
    break
  
  k=array[0][0]
  print(k)
  array[0]=array[1:]
  if k in answer:
    continue

  answer+=k
  # array.sort(key=len,reverse=True)
    



# answer=''.join(dict.fromkeys(answer))
print(answer)