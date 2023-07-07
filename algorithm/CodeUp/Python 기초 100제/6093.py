n=int(input())
array=list(map(int,input().split()))

array.reverse()
for i in range(0,n):
  print(array[i],end=' ')