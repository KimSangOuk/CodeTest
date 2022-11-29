import sys
input=sys.stdin.readline()

n=int(input())
array=list(map(int,input().split()))

target=1
for i in array:
  if target<i:
    break
  target+=i

print(target)